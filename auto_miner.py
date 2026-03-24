#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import subprocess
from datetime import datetime
import urllib.request
import urllib.parse

# 配置项
BASE_DIR = "/Users/y/oversea-project/内容创作"
SKILL_DIR = os.path.join(BASE_DIR, ".trae/skills/solopreneur-topic-miner")
HTML_PATH = os.path.join(BASE_DIR, "daily_topic_dashboard.html")
FETCH_SCRIPT = os.path.join(SKILL_DIR, "fetch_trends.py")
PROFILE_PATH = os.path.join(SKILL_DIR, "user_profile.json")

# ==========================================
# 請替換為您自己的 OpenAI 或其他大模型 API Key
# 建議將 API_KEY 設置為環境變數，這裡為了演示方便直接預留位置
# ==========================================
API_KEY = os.environ.get("OPENAI_API_KEY", "your-api-key-here") 
API_BASE = "https://api.openai.com/v1/chat/completions" # 如果使用代理請修改
MODEL_NAME = "gpt-4o" # 或 gpt-4-turbo, claude-3-opus 等

def load_profile():
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "track": "AI 效率工具",
        "target_audience": "对 AI 有需求或想学习 AI 的普通人",
        "monitoring_sources": {"official_accounts": ["all"]}
    }

def fetch_data(niche):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 開始抓取全網熱點及 WeWeRSS 數據...")
    cmd = ["python3", FETCH_SCRIPT, "--niche", niche, "--scope", "domestic", "--wechat", "all"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except Exception as e:
        print(f"數據抓取失敗: {e}")
        return None

def call_llm_for_topics(profile, raw_data):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 正在呼叫大模型進行 3D 評分與選題生成...")
    
    # 準備給大模型的 prompt
    system_prompt = """
你是一個資深的「爆款選題主編」。請根據提供的【全網熱點及競品數據】，為用戶篩選並生成 6 個最值得動筆的降維打擊選題。
請嚴格按照以下 JSON 格式返回，不要包含任何其他多餘文字或 markdown 標記（確保可以被 json.loads 解析）：
[
  {
    "title": "太離譜了！我用阿里新出的 AI，30 分鐘白嫖了一家網店",
    "source": "「量子位」今日推送",
    "tag": "降維打擊 · 商業實戰",
    "trend_score": 9,
    "comp_score": 8,
    "rel_score": 10,
    "angle": "量子位的文章太硬核，我們把它降維成“普通人如何開無貨源網店”的保姆級教程。主打“大廠背書 + 搞錢痛點”。",
    "alt_titles": ["副業天花板！用阿里 AI 工具 30 分鐘開一家網店", "別只拿 AI 聊天了，大廠教你如何“一鍵生成賺錢機器”"],
    "color_theme": "indigo"
  }
]
color_theme 可選值: indigo, emerald, blue, purple, teal, pink, orange, red。保證 6 個選題的主題色盡量不同。
"""
    
    user_prompt = f"""
用戶賽道：{profile['track']}
目標受眾：{profile['target_audience']}

今日原始抓取數據：
{json.dumps(raw_data, ensure_ascii=False)[:3000]} # 限制長度避免 token 溢出

請根據上述數據，生成 Top 6 選題（JSON 格式）：
"""
    
    # 調用 OpenAI API (原生 urllib 實現，無需安裝第三方庫)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.7
    }
    
    req = urllib.request.Request(API_BASE, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    
    try:
        if API_KEY == "your-api-key-here":
            print("⚠️ 警告: 未配置 API KEY，將使用模擬生成的選題數據渲染看板。")
            return get_mock_topics()
            
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode('utf-8'))
            content = result['choices'][0]['message']['content']
            # 清理可能的 markdown 標記
            content = content.replace("```json", "").replace("```", "").strip()
            return json.loads(content)
    except Exception as e:
        print(f"大模型呼叫失敗: {e}，將使用模擬數據兜底。")
        return get_mock_topics()

def get_mock_topics():
    # 兜底的模擬數據
    return [
        {
            "title": "太離譜了！我用阿里新出的 AI，30 分鐘白嫖了一家網店",
            "source": "「量子位」今日推送",
            "tag": "降維打擊 · 商業實戰",
            "trend_score": 9, "comp_score": 8, "rel_score": 10,
            "angle": "量子位的文章太硬核，我們把它降維成“普通人如何開無貨源網店”的保姆級教程。主打“大廠背書 + 搞錢痛點”。",
            "alt_titles": ["副業天花板！用阿里 AI 工具 30 分鐘開一家網店", "別只拿 AI 聊天了，大廠教你如何“一鍵生成賺錢機器”"],
            "color_theme": "indigo"
        },
        {
            "title": "接上微信就能起飛？盤點那些把 AI 接入微信的離譜玩法",
            "source": "「卡爾的AI沃茨」今日推送",
            "tag": "信息差獵奇",
            "trend_score": 8, "comp_score": 9, "rel_score": 9,
            "angle": "普通人最關心的就是“能不能在微信裡用”。整理這批 Clawbot 項目，挑出 3 個能當客服/陪聊的，教他們如何免費接入。",
            "alt_titles": ["太卷了！我把 AI 接進微信後，群友都以為我是神仙", "2026 最火玩法：手把手教你擁有一個微信 AI 小助手"],
            "color_theme": "emerald"
        },
        {
            "title": "你的 API 被調包了？1個詞測出你買的 AI 模型是真是假",
            "source": "「量子位」今日防騙預警",
            "tag": "避坑指南",
            "trend_score": 7, "comp_score": 9, "rel_score": 8,
            "angle": "利用“避坑/防騙”情緒。把原文章中複雜的技術原理簡化為一個“魔法測試詞”，讓大家複製去測套殼軟體。",
            "alt_titles": ["充錢買套殼 AI 前必看！一個詞測出它的真假", "揭秘 API 供應商黑幕：你用的可能是降級殘血版"],
            "color_theme": "blue"
        },
        {
            "title": "告別鬼畫符！用 AI 一行指令“復活”王羲之，連筆排版絕了",
            "source": "「量子位」開源項目推薦",
            "tag": "趣味玩法",
            "trend_score": 8, "comp_score": 8, "rel_score": 9,
            "angle": "主打“手殘黨福音”。不需要懂代碼，教普通人怎麼用這個開源工具生成以假亂真的名家書法，可以用來做自媒體素材或賀卡。",
            "alt_titles": ["絕了！用 AI 一行代碼“復活”王羲之，網友：比我手寫的還好看", "普通人也能玩！AI 寫毛筆字帶連筆，手殘黨有救了"],
            "color_theme": "purple"
        },
        {
            "title": "單顯卡就能跑“世界模型”！LeCun 新絕招讓 AI 門檻再降",
            "source": "「量子位」技術突破",
            "tag": "前沿科普",
            "trend_score": 9, "comp_score": 7, "rel_score": 7,
            "angle": "弱化論文裡的公式，強調“算力平民化”。告訴讀者未來我們可能在自己的破電腦上也能跑頂級 AI 模型了，激發期待感。",
            "alt_titles": ["AI 大佬出大招！單卡跑世界模型，普通人離 AGI 更近了？", "算力平民化！LeCun 的新模型讓小玩家也能上桌"],
            "color_theme": "teal"
        },
        {
            "title": "一年一度 AI 榜單啟動！2026 普通人必須關注的 AI 風向標",
            "source": "「量子位」年度盛會",
            "tag": "趨勢盤點",
            "trend_score": 7, "comp_score": 8, "rel_score": 9,
            "angle": "借著行業榜單評選的熱度，幫普通人梳理今年最實用、最有搞錢潛力的 3-5 個 AI 工具或賽道，做個信息差匯總。",
            "alt_titles": ["2026 搞錢必看！這份 AI 榜單裡藏著普通人的新風口", "別只當旁觀者了，今年最值得關注的 AI 趨勢全在這"],
            "color_theme": "pink"
        }
    ]

def render_html(topics, raw_data, profile):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 正在渲染 HTML 看板...")
    
    # 1. 生成 Topics HTML
    topics_html = ""
    for i, t in enumerate(topics):
        color = t.get('color_theme', 'indigo')
        # 顏色映射表
        color_map = {
            'indigo': {'bg': 'bg-indigo-100', 'text': 'text-indigo-800', 'bar': 'bg-indigo-500', 'icon': 'text-indigo-500'},
            'emerald': {'bg': 'bg-emerald-100', 'text': 'text-emerald-800', 'bar': 'bg-emerald-500', 'icon': 'text-emerald-500'},
            'blue': {'bg': 'bg-blue-100', 'text': 'text-blue-800', 'bar': 'bg-blue-500', 'icon': 'text-blue-500'},
            'purple': {'bg': 'bg-purple-100', 'text': 'text-purple-800', 'bar': 'bg-purple-500', 'icon': 'text-purple-500'},
            'teal': {'bg': 'bg-teal-100', 'text': 'text-teal-800', 'bar': 'bg-teal-500', 'icon': 'text-teal-500'},
            'pink': {'bg': 'bg-pink-100', 'text': 'text-pink-800', 'bar': 'bg-pink-500', 'icon': 'text-pink-500'},
            'orange': {'bg': 'bg-orange-100', 'text': 'text-orange-800', 'bar': 'bg-orange-500', 'icon': 'text-orange-500'},
            'red': {'bg': 'bg-red-100', 'text': 'text-red-800', 'bar': 'bg-red-500', 'icon': 'text-red-500'},
        }
        c = color_map.get(color, color_map['indigo'])
        
        alt_titles_li = "".join([f"<li>{title}</li>" for title in t['alt_titles']])
        
        card_html = f"""
        <!-- Topic Card {i+1} -->
        <div class="glass-card rounded-2xl p-6 transition transform hover:-translate-y-1 hover:shadow-xl relative overflow-hidden">
            <div class="absolute top-0 right-0 {c['bar']} text-white text-xs font-bold px-3 py-1 rounded-bl-lg">TOP {i+1}</div>
            <div class="mb-4">
                <span class="inline-block px-2.5 py-1 rounded-full text-xs font-semibold {c['bg']} {c['text']} mb-3">{t['tag']}</span>
                <h3 class="text-lg font-bold text-dark leading-snug mb-2">{t['title']}</h3>
                <p class="text-sm text-gray-500"><i class="fas fa-fire {c['icon']} mr-1"></i> 熱點源：{t['source']}</p>
            </div>
            <div class="space-y-3 mb-5 bg-gray-50 p-4 rounded-xl">
                <div><div class="flex justify-between text-xs font-medium text-gray-600 mb-1"><span>📈 趨勢爆發</span><span>{t['trend_score']}/10</span></div><div class="score-bar"><div class="score-fill bg-orange-500" style="width: {t['trend_score']*10}%"></div></div></div>
                <div><div class="flex justify-between text-xs font-medium text-gray-600 mb-1"><span>⚔️ 藍海競爭</span><span>{t['comp_score']}/10</span></div><div class="score-bar"><div class="score-fill bg-yellow-500" style="width: {t['comp_score']*10}%"></div></div></div>
                <div><div class="flex justify-between text-xs font-medium text-gray-600 mb-1"><span>🎯 受眾匹配</span><span>{t['rel_score']}/10</span></div><div class="score-bar"><div class="score-fill bg-green-500" style="width: {t['rel_score']*10}%"></div></div></div>
            </div>
            <div class="space-y-4 text-sm">
                <div><h4 class="font-bold text-gray-800 flex items-center gap-1.5 mb-1"><i class="fas fa-lightbulb text-yellow-400"></i> 差異化切入點</h4><p class="text-gray-600 leading-relaxed">{t['angle']}</p></div>
                <div><h4 class="font-bold text-gray-800 flex items-center gap-1.5 mb-1"><i class="fas fa-pen-nib text-blue-500"></i> 備選標題</h4><ul class="list-disc pl-5 text-gray-600 space-y-1">{alt_titles_li}</ul></div>
            </div>
        </div>
        """
        topics_html += card_html

    # 2. 生成 WeWeRSS 列表 HTML
    wewerss_html = ""
    wewerss_count = 0
    if raw_data and "全局监控" in raw_data:
        articles = raw_data["全局监控"].get("data", [])
        wewerss_count = len(articles)
        for art in articles[:15]: # 最多顯示 15 篇
            wewerss_html += f"""
            <div class="bg-white p-3 rounded-lg shadow-sm border border-green-50">
                <p class="text-sm text-gray-800 font-medium truncate-2-lines" title="{art['title']}">{art['title']}</p>
                <a href="{art['link']}" target="_blank" class="text-xs text-blue-500 mt-1 cursor-pointer hover:underline block">點擊閱讀原文</a>
            </div>
            """

    # 3. 生成平台熱榜 HTML
    platforms = [
        ("微博", "fab fa-weibo text-red-500", "微博熱搜"),
        ("知乎", "fab fa-zhihu text-blue-600", "知乎熱榜"),
        ("抖音", "fab fa-tiktok text-black", "抖音熱門"),
        ("B站", "fab fa-bilibili text-pink-500", "B站熱門"),
        ("百度", "fas fa-paw text-blue-500", "百度熱搜"),
        ("今日头条", "far fa-newspaper text-red-600", "今日頭條")
    ]
    
    trends_html = ""
    for key, icon, title in platforms:
        if raw_data and key in raw_data:
            items = raw_data[key].get("data", [])[:10]
            li_html = ""
            for i, item in enumerate(items):
                color_class = "text-red-500" if i == 0 else "text-orange-500" if i == 1 else "text-yellow-500" if i == 2 else "text-gray-400"
                li_html += f'<li class="flex gap-2"><span class="{color_class} font-bold w-4">{i+1}</span><span class="truncate">{item["title"]}</span></li>'
                
            trends_html += f"""
            <div class="bg-gray-50 rounded-xl p-4">
                <h3 class="text-sm font-bold text-gray-600 mb-3 flex items-center gap-2"><i class="{icon}"></i> {title}</h3>
                <ul class="space-y-2 text-sm text-gray-700">
                    {li_html}
                </ul>
            </div>
            """

    # 4. 讀取並替換模板 (為了避免過於複雜，這裡直接寫入完整的 HTML 結構)
    final_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>爆款選題監控看板</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <script>
        tailwind.config = {{ theme: {{ extend: {{ colors: {{ primary: '#4F46E5', secondary: '#10B981', dark: '#111827' }}, fontFamily: {{ sans: ['system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'] }} }} }} }}
    </script>
    <style>
        body {{ background-color: #F3F4F6; }}
        .glass-card {{ background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2); box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); }}
        .gradient-text {{ background: linear-gradient(to right, #4F46E5, #10B981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .score-bar {{ height: 6px; border-radius: 3px; background-color: #E5E7EB; overflow: hidden; }}
        .score-fill {{ height: 100%; border-radius: 3px; }}
        .truncate-2-lines {{ display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }}
    </style>
</head>
<body class="text-gray-800 antialiased font-sans">
    <nav class="bg-dark text-white shadow-lg sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <div class="flex items-center gap-3">
                    <div class="bg-gradient-to-tr from-primary to-secondary p-2 rounded-lg"><i class="fas fa-robot text-xl"></i></div>
                    <span class="font-bold text-xl tracking-tight">AI 主編 <span class="font-normal text-gray-400 text-sm ml-2">v2.0</span></span>
                </div>
                <div class="text-sm font-medium text-gray-300 flex items-center gap-2" id="current-time-display">
                    <i class="far fa-clock"></i> 載入中...
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-7xl mx-auto py-8 space-y-8">
        <header class="text-center space-y-3 px-4">
            <h1 class="text-3xl md:text-4xl font-extrabold text-dark tracking-tight">
                <span id="greeting-text">老闆好</span>，今日 <span class="gradient-text">專屬爆款選題</span> 已就緒。
            </h1>
            <p class="text-gray-500 text-base md:text-lg max-w-2xl mx-auto">
                【{profile['track']}】監控報告：大盤熱點已全面匯總，您的 <strong>WeWeRSS 專屬雷達</strong> 今日截獲 {wewerss_count} 篇高質量競品推文。已為您執行“同行降維提取”策略。
            </p>
        </header>

        <section class="px-4">
            <div class="flex items-center gap-2 mb-6">
                <i class="fas fa-trophy text-yellow-500 text-2xl"></i>
                <h2 class="text-2xl font-bold text-dark">今日推薦 Top 6 (基於私有號池挖掘)</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {topics_html}
            </div>
        </section>

        <section class="px-4 pb-8">
            <div class="glass-card rounded-2xl p-6">
                <div class="flex items-center justify-between mb-6 border-b border-gray-100 pb-4">
                    <div class="flex items-center gap-2"><i class="fas fa-satellite-dish text-primary text-xl"></i><h2 class="text-xl font-bold text-dark">全網大盤熱點與私有雷達數據面板</h2></div>
                    <span class="text-xs bg-gray-200 text-gray-600 px-2 py-1 rounded" id="data-update-time">實時更新</span>
                </div>
                
                <div class="mb-8 bg-green-50 rounded-xl p-5 border border-green-100">
                    <div class="flex items-center justify-between mb-4">
                        <div class="flex items-center gap-2"><i class="fab fa-weixin text-green-600 text-lg"></i><h3 class="text-base font-bold text-green-800">專屬號池 (WeWeRSS 全局同步)</h3></div>
                        <span class="text-xs bg-green-200 text-green-800 px-2.5 py-1 rounded font-bold">{wewerss_count} 篇上新</span>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 max-h-64 overflow-y-auto pr-2" style="scrollbar-width: thin;">
                        {wewerss_html}
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {trends_html}
                </div>
            </div>
        </section>
    </main>

    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const now = new Date();
            const hour = now.getHours();
            let greeting = "晚上好";
            if (hour >= 5 && hour < 12) greeting = "早上好";
            else if (hour >= 12 && hour < 14) greeting = "中午好";
            else if (hour >= 14 && hour < 18) greeting = "下午好";
            document.getElementById('greeting-text').innerText = greeting;

            const padZero = (num) => String(num).padStart(2, '0');
            const dateStr = `${{now.getFullYear()}}-${{padZero(now.getMonth() + 1)}}-${{padZero(now.getDate())}} ${{padZero(now.getHours())}}:${{padZero(now.getMinutes())}}`;
            document.getElementById('current-time-display').innerHTML = `<i class="far fa-clock"></i> 更新時間：${{dateStr}}`;
            document.getElementById('data-update-time').innerText = `更新時間：${{dateStr}}`;
        }});
    </script>
</body>
</html>
"""
    
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] HTML 看板已成功更新: {HTML_PATH}")

def push_notification():
    # 這裡預留發送 Open Claw / Webhook 的邏輯
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 執行完成！如果配置了 Webhook，此時應推播到手機。")

if __name__ == "__main__":
    print(f"========== 啟動自動化選題挖掘引擎 ==========")
    profile = load_profile()
    raw_data = fetch_data(profile.get("track", "AI"))
    topics = call_llm_for_topics(profile, raw_data)
    render_html(topics, raw_data, profile)
    push_notification()
    print(f"========== 任務結束 ==========")
