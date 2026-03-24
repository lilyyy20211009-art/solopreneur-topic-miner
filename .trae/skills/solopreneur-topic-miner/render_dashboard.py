#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime

BASE_DIR = "/Users/y/oversea-project/内容创作"
SKILL_DIR = os.path.join(BASE_DIR, ".trae/skills/solopreneur-topic-miner")
HTML_PATH = os.path.join(BASE_DIR, "daily_topic_dashboard.html")
PROFILE_PATH = os.path.join(SKILL_DIR, "user_profile.json")
TOPICS_PATH = os.path.join(SKILL_DIR, "latest_topics.json")
RAW_DATA_PATH = os.path.join(SKILL_DIR, "latest_raw_data.json")

def load_json(path, default_val):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except:
                pass
    return default_val

def render_html():
    profile = load_json(PROFILE_PATH, {"track": "未知领域", "target_audience": "大众"})
    raw_data = load_json(RAW_DATA_PATH, {})
    topics = load_json(TOPICS_PATH, [])
    
    # 如果没有找到任何选题数据，给个提示
    if not topics:
        print("未找到选题数据 latest_topics.json，将使用空面板。")

    # 1. 生成 Topics HTML
    topics_html = ""
    for i, t in enumerate(topics):
        color = t.get('color_theme', 'indigo')
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
        
        alt_titles = t.get('alt_titles', [])
        alt_titles_li = "".join([f"<li>{title}</li>" for title in alt_titles])
        
        card_html = f"""
        <!-- Topic Card {i+1} -->
        <div class="glass-card rounded-2xl p-6 transition transform hover:-translate-y-1 hover:shadow-xl relative overflow-hidden">
            <div class="absolute top-0 right-0 {c['bar']} text-white text-xs font-bold px-3 py-1 rounded-bl-lg">TOP {i+1}</div>
            <div class="mb-4">
                <span class="inline-block px-2.5 py-1 rounded-full text-xs font-semibold {c['bg']} {c['text']} mb-3">{t.get('tag', '精选')}</span>
                <h3 class="text-lg font-bold text-dark leading-snug mb-2">{t.get('title', '未命名标题')}</h3>
                <p class="text-sm text-gray-500"><i class="fas fa-fire {c['icon']} mr-1"></i> 熱點源：{t.get('source', '全网监测')}</p>
            </div>
            <div class="space-y-3 mb-5 bg-gray-50 p-4 rounded-xl">
                <div><div class="flex justify-between text-xs font-medium text-gray-600 mb-1"><span>📈 趨勢爆發</span><span>{t.get('trend_score', 8)}/10</span></div><div class="score-bar"><div class="score-fill bg-orange-500" style="width: {t.get('trend_score', 8)*10}%"></div></div></div>
                <div><div class="flex justify-between text-xs font-medium text-gray-600 mb-1"><span>⚔️ 藍海競爭</span><span>{t.get('comp_score', 8)}/10</span></div><div class="score-bar"><div class="score-fill bg-yellow-500" style="width: {t.get('comp_score', 8)*10}%"></div></div></div>
                <div><div class="flex justify-between text-xs font-medium text-gray-600 mb-1"><span>🎯 受眾匹配</span><span>{t.get('rel_score', 8)}/10</span></div><div class="score-bar"><div class="score-fill bg-green-500" style="width: {t.get('rel_score', 8)*10}%"></div></div></div>
            </div>
            <div class="space-y-4 text-sm">
                <div><h4 class="font-bold text-gray-800 flex items-center gap-1.5 mb-1"><i class="fas fa-lightbulb text-yellow-400"></i> 差異化切入點</h4><p class="text-gray-600 leading-relaxed">{t.get('angle', '')}</p></div>
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
                <p class="text-sm text-gray-800 font-medium truncate-2-lines" title="{art.get('title', '')}">{art.get('title', '')}</p>
                <a href="{art.get('link', '#')}" target="_blank" class="text-xs text-blue-500 mt-1 cursor-pointer hover:underline block">點擊閱讀原文</a>
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
                li_html += f'<li class="flex gap-2"><span class="{color_class} font-bold w-4">{i+1}</span><span class="truncate">{item.get("title", "")}</span></li>'
                
            trends_html += f"""
            <div class="bg-gray-50 rounded-xl p-4">
                <h3 class="text-sm font-bold text-gray-600 mb-3 flex items-center gap-2"><i class="{icon}"></i> {title}</h3>
                <ul class="space-y-2 text-sm text-gray-700">
                    {li_html}
                </ul>
            </div>
            """

    # 4. 讀取並替換模板
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
                【{profile.get('track', 'AI')}】監控報告：大盤熱點已全面匯總，您的 <strong>WeWeRSS 專屬雷達</strong> 今日截獲 {wewerss_count} 篇高質量競品推文。已為您執行“同行降維提取”策略。
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
    print("HTML Dashboard Rendered successfully!")

if __name__ == "__main__":
    render_html()
