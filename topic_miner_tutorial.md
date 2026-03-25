# 選題 Agent：每天自動挖掘爆款選題 — 圖文手冊

## 🎯 你還在靠感覺想選題嗎？

每天打開手機刷一圈，看看同行寫什麼，再腦力激盪一番——等你想出三個選題，半天過去了。更慘的是：想出來的選題沒人搜、寫出來的文章沒人看。

問題不是你不努力，而是你在用體力做一件 AI 可以幫你做的事。

這節課教你用 Trae (或 Claude Code) 搭一個 **爆款選題 Agent (Solopreneur Topic Miner)**：每天早上自動監控競品、分析數據、評分篩選，直接推給你 **6 個可以立刻動筆的降維打擊選題**。

---

## 💡 這個 Skill 解決了什麼問題？

大多數人的選題流程是這樣的：
❌ 憑感覺 → 問 AI「幫我想 10 個選題」 → 發出去 → 沒人看 → 下次繼續靠感覺

問題在哪？AI 給你的選題，是它「以為」受歡迎的，不是數據驗證過的（這叫做 AI 幻覺）。真正的爆款選題有三個共同特徵：
1. **📈 正在發生的趨勢**（流量在上升）
2. **⚔️ 競爭沒那麼激烈**（做得到）
3. **🎯 和你的帳號方向匹配**（受眾對了）

這三件事，人腦做起來很累，但透過這個 Agent，你可以實現：
*   **全網 + 私域雙重雷達**：一鍵抓取 6 大平台熱搜與同行公眾號最新推文，告別信息差。
*   **AI 主編級思考 (CoT)**：讓大模型閱讀真實數據，從成百上千條信息中大浪淘沙，打分選出 Top 6。
*   **自動渲染精美看板**：自動生成高顏值的 HTML 數據看板，你的專屬「情報局」一眼可見。
*   **7x24 小時無人值守**：支持定時任務，每天早上 9 點自動把爆款選題推送到你的手機上。

---

## 🛠️ 第一章：如何用 Trae 創建與安裝這個選題 Skill？

我們不需要寫複雜的程式碼，只需要透過自然語言與 Trae (或 Claude Code) 對話，就能把我們的業務邏輯固化成一個自動化的 Skill。

如果你想直接使用本教程開發好的 `solopreneur-topic-miner`，請按照以下「抄作業」步驟進行安裝：

### 📥 快速安裝步驟（給學員的指南）

**Step 1: 準備專屬資料夾**
1. 打開 Trae IDE，進入你的工作目錄（例如 `我的自媒體項目`）。
2. 在左側文件樹中，創建一個隱藏資料夾路徑：`.trae/skills/solopreneur-topic-miner`。
*(注意：`.trae` 開頭的資料夾默認是隱藏的，如果看不到，請在 Trae 的設置或文件樹右鍵菜單中開啟「顯示隱藏文件」。)*

**Step 2: 複製核心代碼（Agent 的靈魂）**
請將本教程**第五章**提供的開源代碼，分別複製並保存為以下三個文件，放入剛剛創建的資料夾中：
*   📝 `SKILL.md`：直接複製貼上（這是 Agent 的「大腦」與規則）。
*   🐍 `fetch_trends.py`：直接複製貼上（這是 Agent 去全網抓取熱點的「手腳」）。
*   🎨 `render_dashboard.py`：直接複製貼上（這是幫你畫出精美 HTML 數據看板的「畫筆」）。
*(注：`user_profile.json` 不需要手動創建，Agent 首次啟動時會自動問你並生成。)*

**Step 3: 安裝環境依賴**
這個腳本去網路上抓取數據需要用到 Python 的網絡請求庫。請在 Trae 底部的「終端機 (Terminal)」中輸入並運行以下命令：
```bash
pip install requests
```

**Step 4: (強烈推薦) 安裝前端設計 Skill 以實現多智能體協作**
為了讓你的 HTML 數據看板呈現出極具科技感的 Glassmorphism（毛玻璃）高級排版，你需要讓主 Agent 能夠呼叫專業的「設計師 Agent」。
1. 在 `.trae/skills/` 目錄下，**再新建兩個資料夾**：
   *   `frontend-design`
   *   `ui-ux-pro-max-skill`
2. 將這兩個 Skill 的核心 `SKILL.md` 文件（老師會提供）分別放入對應的資料夾中。
*這一步能完美展現 AI 時代的高階玩法：**多智能體協作 (Multi-Agent Collaboration)**。你的主 Agent 會變成一個「項目經理」，自動把畫網頁的活兒派發給這兩個專業的設計師 Agent！*

**Step 5: 一鍵啟動！**
所有文件就位後，回到 Trae 的 AI 對話框，輸入你的召喚指令：
```bash
啟動 solopreneur-topic-miner
```
Agent 就會立刻甦醒，並親切地問你：“請告訴我你的創作賽道和目標受眾是什麼？” —— 恭喜你，你的專屬爆款選題情報局正式上線！

---

## 🛠️ 第二章：進階挑戰 —— 如何從零打造你自己的專屬 Agent Skill？

如果你不滿足於「抄作業」，想自己親手用 Trae 從零捏出一個類似 `solopreneur-topic-miner` 這樣強大的專屬 AI 助手，請跟著以下步驟走。這也是掌握 Agent 開發最核心的邏輯！

### Step 1: 構思你的 Agent「靈魂」
在寫任何代碼之前，先想清楚這個 Agent 要解決什麼問題：
*   **它的角色是什麼？**（例如：一個資深的「爆款選題主編」）
*   **它需要什麼輸入？**（例如：用戶的賽道和受眾）
*   **它要執行什麼動作？**（例如：抓熱搜 → 打分 → 寫大綱）
*   **它的輸出長什麼樣？**（例如：6 個帶分數的選題卡片）

### Step 2: 在 Trae 中建立 Skill 框架
1. 打開 Trae IDE，進入右側的 AI 對話框。
2. 對 Trae 說出你的需求：**「我想創建一個名為 `my-custom-agent` 的 Skill，用於（描述你的需求）。請幫我初始化 Skill 框架。」**
3. Trae 的 `skill-creator` 工具會自動在你的專案中建立 `.trae/skills/my-custom-agent/SKILL.md` 文件。

### Step 3: 編寫「主編大腦」(SKILL.md 核心 Prompt)
打開生成的 `SKILL.md`，這是 Agent 的大腦。你需要把 Step 1 的構思，變成 AI 能看懂的「強制指令」。一個好的 Skill Prompt 必須包含：
*   **🎯 身份與目標**：明確告訴它「你是誰，你要做什麼」。
*   **⚙️ 工作流 (Workflow)**：用 Step 1, Step 2 的方式，把任務拆解成具體的步驟。例如：「Step 1：調用搜索工具尋找熱點；Step 2：進行三維打分...」
*   **📝 輸出格式**：嚴格規定它最後怎麼回答你，最好給出 Markdown 或 JSON 範例。
*   **⚠️ 紅線/負面清單**：告訴它「絕對不能做什麼」（例如：絕對禁止捏造假新聞）。

### Step 4: 賦予 Agent「手腳」(編寫底層腳本)
如果你的 Agent 只需要聊天，Step 3 就夠了。但如果你想讓它像 `solopreneur-topic-miner` 一樣能抓取全網數據、能畫網頁，就需要給它配備 Python 腳本：
1. 在對話框中讓 Trae 幫你寫代碼：「請幫我寫一個 Python 腳本，調用 60s.viki.moe 的 API 抓取微博熱搜，並保存為 JSON。」
2. Trae 會自動為你寫好類似 `fetch_trends.py` 的腳本。
3. **最關鍵的一步：將腳本與大腦連接！** 回到 `SKILL.md`，在工作流中加上一句強制指令：「**你必須使用終端工具執行 `python fetch_trends.py` 來獲取數據，然後根據腳本輸出的結果來回答用戶。**」

### Step 5: 測試與反覆迭代
1. 在對話框輸入 `啟動 my-custom-agent`。
2. 觀察它的表現。如果它「幻覺」了，或者沒有按你的格式輸出，就回到 `SKILL.md` 中修改 Prompt，把規則寫得更死、更具體。
3. 不斷重複這個過程，直到它能 100% 穩定地輸出你想要的結果。這就是「Prompt Engineering（提示詞工程）」的魅力！

---

## 🎮 玩家指南：如何日常使用這個 Agent？

安裝完成後，日常使用非常簡單，它就像你僱傭的一個 24 小時在線的數字主編。

### 場景一：在編輯器裡“隨叫隨到”
1. **喚醒主編**：每天早上坐在電腦前，打開 Trae，在對話框輸入 `啟動 solopreneur-topic-miner`。
2. **靜候佳音**：Agent 會自動讀取你的賽道記憶，然後去全網（微博、知乎、抖音等）和私域（WeWeRSS）拉取最新數據。
3. **查收報告**：大約 1 分鐘後，它會在對話框裡直接輸出 6 個為你量身定製的爆款選題，每個選題都自帶：
   *   `熱點來源`（怎麼火的）
   *   `三維打分`（為什麼值得寫）
   *   `差異化切入點`（別人沒寫過的角度）
   *   `3個爆款標題`（直接拿去用）
   *   `內容大綱`（照著填空就能出稿）
4. **瀏覽看板**：同時，它會在你的資料夾裡自動更新 `daily_topic_dashboard.html`。你可以直接在瀏覽器打開它，享受極具科技感的可視化數據面板。

### 場景二：升級為“全自動無人值守”模式
如果你連每天打字喚醒都懶得做，可以讓它每天定時發送到你的手機上！（詳細配置請看**第四章：自動化工作流**）
1. 配置好 `auto_miner.py` 和定時任務（如 Cron 或 Open Claw）。
2. 每天早上 9 點，你還在通勤地鐵上，手機就會收到一條微信/飛書推送：“老闆早，今日 Top 6 專屬爆款選題已就緒...”
3. 點開附帶的網頁鏈接，一目了然看遍全網熱點。

---

## 🧠 第二章：Agent 的「大腦」設計（底層邏輯）

這個 Skill 徹底拋棄了不靠譜的「通用網頁搜尋」，而是採用了一套 **確定性的工程化架構**。它的核心邏輯分為四步：

### 第一步：監控兩類核心來源（拒絕幻覺，只要真數據）
Agent 會在後台執行腳本，精準抓取過去 24 小時內的真實數據：
1. **大盤情緒雷達（社交媒體）**：透過 API 自動抓取 **百度、微博、知乎、抖音、B站、今日頭條** 等平台的 Top 10 實時熱榜，看大眾當前在關心什麼。
2. **私有競品雷達（微信公眾號）**：為了打破微信生態的封閉，我們整合了 **免費開源工具：WeWeRSS**。
   * *原理：只要你在本地或伺服器部署了 WeWeRSS 並訂閱了同賽道的頭部帳號，Agent 就能透過 RSS 節點，100% 精準、免費地將昨夜今晨的所有競品文章全部拉取過來，作為選題素材庫。*

### 第二步：主編級三維漏斗評分 (Decision)
拿到幾十上百條熱點後，AI 大模型會化身資深主編，對每個話題進行 0-10 分的三維打分：
*   **趨勢分 (Trend)**：是爆發期還是已過氣？
*   **競爭分 (Competition)**：是被大 V 壟斷還是有素人紅利？
*   **匹配分 (Relevance)**：與你的賽道和受眾是否高度契合？
最終，嚴格淘汰低分項，只留下 **Top 6** 最硬核的選題。

### 第三步：差異化包裝與網頁版呈現 (Presentation)
針對選出的 Top 6，Agent 不只給個標題，它會：
*   提供**爆款標題備選**（極具網感的標題）。
*   提供**差異化切入點**（例如：把深奧的技術論文，降維成普通人的搞錢教學）。
*   **視覺化網頁呈現**：Agent 會自動生成並渲染出一個極具科技感的 HTML 數據看板（`daily_topic_dashboard.html`）。看板內包含智慧問候語、Top 6 選題卡片（含雷達圖評分），以及全網大盤和 WeWeRSS 的底層數據列表。

---

## 🚀 第三章：學員如何使用這個 Skill？

當你（或你的學員）配置好這個 Skill 後，日常使用非常簡單：

### Step 1: 配置 WeWeRSS 公眾號監控
在使用 Agent 之前，我們需要先讓它能「看見」微信裡的文章。
1. 在你的電腦或伺服器上透過 Docker 部署免費開源項目 **WeWeRSS**。
2. 登入 WeWeRSS 後台，添加你賽道內的 5-10 個頭部競品公眾號。
3. 獲取你的全局訂閱源地址（例如：`http://127.0.0.1:4000/feeds/all.atom`），Agent 會自動讀取這個地址來獲取最新推文。

### Step 2: 啟動 Agent 與初始化設定
在 Trae IDE 終端或對話框中輸入以下指令喚醒 Agent：
```bash
啟動 solopreneur-topic-miner
```
如果是第一次使用，Agent 會主動詢問：
1. **你的創作賽道**（例如：AI 效率工具）
2. **你的目標受眾**（例如：對 AI 有需求的普通人）
*(Agent 會將這些資訊寫入 `user_profile.json` 永久記住，下次不再詢問。)*

### Step 3: 接收你的專屬情報局
喝杯咖啡的功夫，Agent 就會調用 API 和 WeWeRSS 獲取數據、完成打分。
接著，它會直接在本地打開那個美觀的 **爆款選題監控看板 (HTML)**，你只需要挑選最心儀的那個 Top 6 選題，直接開始創作！

---

## 📱 第四章：進階玩法 —— 每天早上 9 點自動推播到手機！

既然是 Agent，就不能每次都手動點。我們可以透過自動化工具，讓它每天早上醒來就已經把選題準備好。

這裡提供兩種自動化方案：

### 方案 A：本地 Cron 定時刷新網頁看板
如果你有一台常開機的 Mac 或伺服器：
1. 讓 Agent 為你寫一個 `auto_miner.py` 腳本。
2. 打開終端機，輸入 `crontab -e`，添加定時任務：
   `0 9 * * * /usr/bin/python3 /你的路徑/auto_miner.py`
3. 每天早上 9 點，系統會在後台默默運行大模型，並刷新你的 HTML 網頁看板。

### 方案 B：使用 Open Claw 定時調用 Skill 並推播到手機（推薦）
如果你想直接在微信或飛書裡收到選題通知，結合 **Open Claw** 這樣的自動化工作流平台是最佳選擇：
1. **登入 Open Claw**：創建一個新的自動化 Workflow。
2. **設置觸發器 (Trigger)**：選擇「定時觸發 (Schedule)」，設定為每天早上 09:00。
3. **添加動作 (Action) - 調用 Agent**：
   * 選擇「CLI 命令」或相應的 Agent 執行節點。
   * 輸入執行命令：`trae-cli run solopreneur-topic-miner`（或透過 API 呼叫該腳本）。
4. **添加動作 (Action) - 發送訊息**：
   * 將上一步 Agent 輸出的 Top 6 選題結果，透過企業微信機器人、飛書機器人或 Bark 節點發送出去。
   * *(可選：附上你剛才自動生成的 HTML 看板連結。)*
5. **發布上線**：完成！以後每天早上通勤時，打開手機就能直接看到 AI 主編為你準備的今日爆款選題了。


## 📁 第五章：Agent 核心程式碼開源

為了方便你直接複製使用，以下是 `solopreneur-topic-miner` 的三個核心檔案原始碼。

### 1. 核心指令檔案 (`SKILL.md`)
這是 Agent 的「大腦」，定義了它的工作流、紅線和輸出格式。

```markdown
---
name: "solopreneur-topic-miner"
description: "自动挖掘并筛选爆款选题。包含热点监控、数据分析、三维评分过滤，最终推荐 6 个可执行的选题及切入大纲。适合自媒体创作者日常寻找爆款灵感。"
---

# 爆款选题挖掘 Agent (Solopreneur Topic Miner)

你是一个资深的“爆款选题主编 Agent”。你的任务是根据用户提供的【创作赛道】和【目标受众】，利用网络搜索工具获取实时热点，并通过多维数据分析，为用户自动挖掘出**最值得动笔的 6 个爆款选题**。

你的工作流严格遵循《爆款选题挖掘三大特征》的底层逻辑。

## 🎯 启动与记忆 (Memory Initialization)

**当用户召唤本 Skill 时，你必须首先检查本地是否存在用户配置文件（这代表了 Agent 的长期记忆）：**

1.  **静默检查**：使用文件读取工具检查是否存在 `.trae/skills/solopreneur-topic-miner/user_profile.json` 文件。
2.  **有记忆（老用户）**：如果存在，直接读取其中的【创作赛道】、【目标受众】和【专属监控源】，并向用户致意：“欢迎回来，老板！我已经调取了您的专属赛道信息（XX赛道）。正在为您自动拉取今天的热点...”然后直接进入核心工作流。
3.  **无记忆（新用户）**：如果不存在，你需要主动询问以下核心信息，并在用户回答后，**使用文件写入工具自动生成 `user_profile.json` 文件永久保存下来**：
    *   **创作赛道/领域**（例如：AI 效率工具、自媒体运营、数码测评等）
    *   **目标受众定位**（例如：职场新人、全职宝妈、高净值人群等）
    *   **【核心配置】你的专属监控源**：
        *   **对标公众号**：请提供 3-5 个对标账号。*(高阶提示：本系统已整合开源的 `WeWeRSS` 引擎。如果您在本地部署了 WeWeRSS，我将能 100% 精准、免费地抓取这些公众号的每日全文！)*
        *   **行业 RSS 链接**：提供您必看的特定网站订阅源。

## ⚙️ 核心工作流 (Workflow)

收到用户输入后，你需要严格按照以下三个步骤执行（注意：你需要主动调用搜索工具来完成任务）：

### Step 1: 感知层 —— 全网热点监控与发散 (Information Gathering)
【最高红线】：**绝对禁止使用通用搜索引擎（如直接搜索“小红书 AI效率工具”）去猜数据！绝对禁止捏造（幻觉）文章标题！**

为了保证数据的绝对真实性和工程化稳定性，你必须按照以下三种不同的方式获取你的核心数据源：

1. **① 社交媒体热点（必须调用本地 API 脚本）**
   *   **操作指令**：你必须使用终端工具（RunCommand）执行本 Skill 目录下的 Python 脚本来获取各平台的实时热搜。
   *   **执行命令**：如果用户配置了具体的对标公众号，将它们作为参数传入：`--wechat "账号1,账号2"`。如果用户希望**全局同步 WeWeRSS 中的所有订阅**（或用户配置了"all"），则必须使用命令：`python3 .trae/skills/solopreneur-topic-miner/fetch_trends.py --niche "[用户赛道]" --scope domestic --wechat "all"`。
   *   **数据处理**：该脚本会直接调用公共 API (`60s.viki.moe` 和私有 `WeWeRSS`) 并返回格式化的 JSON 数据。你需要读取脚本输出的结果，提取出被脚本标记为高相关度（`relevance >= 6` 或带有 🔥 标记）的今日真实话题，**以及抓取到的微信公众号最新推文。**

2. **② 行业新闻 RSS（必须使用确定的 XML/Atom 链接）**
   *   **操作指令**：如果用户未提供专属 RSS，你必须通过 `WebFetch` 直接读取开源的优质 RSS 源（参考 `https://github.com/weekend-project-space/top-rss-list` 中的链接，如 36氪、少数派的真实 RSS feed）。
   *   **时间过滤**：读取 XML 后，**必须校验 `<pubDate>` 字段**，只提取发布时间在过去 24 小时内的文章。

3. **③ 竞品公众号/对标账号（已整合进 API 脚本）**
   *   *注：微信公众号的监控已交由 `fetch_trends.py` 中的 RSSHub 模块自动完成。如果 API 返回“抓取失败”，你必须如实记录，绝对禁止自己去网上盲搜捏造。*

*   **目标**：结合脚本输出的 API 热点数据、RSS 深度数据和公众号竞品数据，汇总出一个包含 8-10 个绝对属于过去 24 小时内的真实话题池。
*   *要求*：不要只看表面的热搜词，要深入寻找正在讨论的具体事件或痛点。

### Step 2: 决策层 —— 多维爆款特征漏斗筛选 (Scoring & Filtering)
不要直接把找出来的热点丢给用户。你需要扮演主编，对这 8-10 个话题进行**三维打分（满分 10 分/项）**，并淘汰低分项：
1.  **📈 趋势分 (Trend)**：该话题是正在爆发（流量上升期），还是已经过气？（正在发生、被广泛讨论的得分高）
2.  **⚔️ 竞争分 (Competition)**：该话题下是否已经被头部大 V 垄断？普通素人或中小号切入是否还有流量红利空间？（竞争越小，得分越高）
3.  **🎯 匹配分 (Relevance)**：该话题与用户的【创作赛道】和【目标受众】的契合度有多高？受众是否真的关心？（高度匹配得分高）

*动作*：计算每个话题的总分，**只保留总分排名前 6 的话题**。

### Step 3: 执行层 —— 差异化包装与输出 (Output Generation)
针对脱颖而出的 Top 6 选题，你必须给出详细的执行建议，而不是一个干瘪的词条。

## 📝 最终输出格式与自动渲染网页 (Output & Dashboard)

对于每一个入选的 Top 6 选题，请先在对话框中使用以下结构输出文字报告给用户：

### 🏆 选题一：[用一句话概括话题核心内容]
*   **🔥 热点来源与现状**：简述这个热点是怎么火的，目前在哪些平台讨论度高。
*   **📊 数据诊断得分**：
    *   趋势分：X/10 (理由: ...)
    *   竞争分：X/10 (理由: ...)
    *   匹配分：X/10 (理由: ...)
*   **💡 差异化切入点（Angle）**：为这个话题提供 2 个别人没写过的、能引发情绪共鸣或提供极大价值的切入视角。
*   **✍️ 爆款标题备选**：提供 3 个具有极强网感（吸引眼球、直击痛点）的备选标题。
*   **📝 内容大纲速写**：
    *   引言（Hook）：...
    *   核心观点（Body）：...
    *   行动呼吁（CTA）：...

**【强制动作】：在输出完文字后，你必须将这 6 个选题的数据写入本地，以自动更新 HTML 看板！**
1. 将你刚才生成的 6 个选题，按照以下 JSON 格式使用文件写入工具保存到 `.trae/skills/solopreneur-topic-miner/latest_topics.json`：
```json
[
  {
    "title": "话题标题",
    "source": "热点来源",
    "tag": "分类标签（如：降维打击）",
    "trend_score": 9,
    "comp_score": 8,
    "rel_score": 10,
    "angle": "差异化切入点说明",
    "alt_titles": ["备选标题1", "备选标题2", "备选标题3"],
    "color_theme": "indigo"
  }
]
```
*(注：color_theme 可以在 indigo, emerald, blue, purple, teal, pink, orange, red 中随机选择)*
2. **判断用户本地是否已存在看板及所需 Skill**：
   - 检查本地是否已存在 `daily_topic_dashboard.html` 文件。
   - 如果**不存在**（说明是新用户首次运行）：
     - 你需要告诉用户：“正在为您调用专业 UI/UX 设计 Agent 创建专属看板...”
     - 你必须在你的工具列表中，尝试调用名为 `frontend-design` 和 `ui-ux-pro-max-skill` 的 Skill（如果可用），要求它们：“根据当前赛道生成一个包含 Top 6 选题卡片和全网热点列表的现代 Glassmorphism 风格数据看板，使用 TailwindCSS。”
     - 如果无法直接调用这两个 Skill，你必须亲自**模仿** `ui-ux-pro-max-skill` 的高级设计标准，编写并生成一个极具科技感、支持深浅色模式、包含动画过渡的 `daily_topic_dashboard.html` 模板，并确保后续步骤可以更新它。
3. 使用终端工具运行命令：`python3 .trae/skills/solopreneur-topic-miner/render_dashboard.py`，这会将最新数据更新到网页中。
4. **判断是否自动打开网页**：
   - 如果本次对话中你是**新建**了 `user_profile.json`（说明是第一次使用的新用户），你必须执行命令 `open daily_topic_dashboard.html` 自动在浏览器中打开网页。
   - 如果是**老用户**（已经存在 `user_profile.json`），**不需要**再次打开网页。你只需要在文字回复的末尾加上一句：“💡 您的专属网页版数据看板已同步更新，您可以随时打开 `daily_topic_dashboard.html` 查看最新情况。”

---

## 🤖 自动化订阅提醒 (Open Claw Integration)
在完整输出以上 Top 6 选题后，**你必须在对话的最后，主动向用户抛出以下“自动化订阅”邀请：**

*话术模板*：“老板，今天的选题已经汇报完毕。我看您的赛道偏好已经保存在我的记忆库中了。**如果您已经连接了 Open Claw（或其他自动化流工具），是否需要我为您生成一份定时任务配置（Cron Job / Webhook）？** 这样我每天早上 9 点会自动运行这套挖掘逻辑，并直接把爆款选题推送到您的微信/飞书上，实现真正的‘全自动情报局’！”

---

## ⚠️ 负面清单 (Negative Constraints)
在执行过程中，**绝对禁止**以下行为：
*   ❌ 推荐政治敏感、社会负面、娱乐八卦等与用户赛道无关且无长期价值的话题。
*   ❌ 未经搜索工具验证，凭空捏造虚假热点或“幻觉”数据。
*   ❌ 推荐那些虽然很火，但竞争极度红海，新号完全没机会的宽泛话题（如：单纯科普“什么是ChatGPT”）。
```

### 2. 用戶記憶文件 (`user_profile.json`)
這是 Agent 的「長期記憶」，用來儲存你的專屬設定，讓它越用越懂你。

```json
{
  "track": "AI 效率工具",
  "target_audience": "对 AI 有需求或想学习 AI 的普通人",
  "monitoring_sources": {
    "official_accounts": [
      "all"
    ],
    "rss_feeds": []
  }
}
```

### 3. 數據抓取腳本 (`fetch_trends.py`)
這是 Agent 的「手腳」，負責呼叫 API 和 WeWeRSS 獲取最新熱點數據。

```python
#!/usr/bin/env python3
"""
跨平台热点监测 - 可执行脚本
确保在 Claude Code 和 Trae 中运行结果一致
"""

import json
import sys
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# 领域关键词映射
NICHE_KEYWORDS = {
    "AI 人工智能": ["AI", "ChatGPT", "GPT", "DeepSeek", "大模型", "机器学习", "神经网络", "OpenAI", "Claude", "AIGC", "文生图", "文生视频"],
    "美妆护肤": ["美妆", "护肤", "化妆", "彩妆", "口红", "面膜", "美容", "穿搭", "时尚"],
    "科技数码": ["手机", "电脑", "数码", "AI", "芯片", "智能", "科技", "互联网", "编程"],
    "职场成长": ["职场", "工作", "求职", "面试", "晋升", "效率", "自我提升", "技能"],
    "财经投资": ["股票", "基金", "理财", "投资", "金融", "经济", "币圈", "加密货币"],
    "美食探店": ["美食", "餐厅", "探店", "食谱", "烹饪", "小吃", "网红店", "打卡"],
    "健身运动": ["健身", "运动", "瑜伽", "跑步", "减肥", "增肌", "训练", "马拉松"],
    "育儿知识": ["育儿", "宝宝", "怀孕", "亲子", "儿童", "早教", "喂养"],
    "游戏攻略": ["游戏", "电竞", "攻略", "赛季", "英雄", "皮肤", "手游", "端游"],
    "情感心理": ["情感", "心理", "恋爱", "婚姻", "情绪", "心理健康"],
    "汽车": ["汽车", "车", "新能源", "电动车", "自动驾驶", "特斯拉", "比亚迪"],
    "房产": ["房产", "房价", "买房", "租房", "房地产", "楼盘"],
    "娱乐": ["娱乐", "明星", "综艺", "电影", "电视剧", "八卦", "绯闻"],
    "体育": ["体育", "足球", "篮球", "NBA", "CBA", "奥运会", "冠军"],
    "军事": ["军事", "国防", "武器", "军演", "军队", "战机", "军舰"],
    "国际": ["国际", "外交", "美国", "欧洲", "全球", "联合国"]
}

# 领域关键词映射（英文）
NICHE_KEYWORDS_EN = {
    "AI 人工智能": ["AI", "ChatGPT", "GPT", "DeepSeek", "LLM", "machine learning", "AIGC", "OpenAI"],
    "美妆护肤": ["makeup", "skincare", "beauty", "fashion", "cosmetics"],
    "科技数码": ["tech", "AI", "smartphone", "computer", "programming", "software", "AI"],
    "职场成长": ["career", "job", "workplace", "interview", "resume", "productivity"],
    "财经投资": ["stock", "market", "invest", "finance", "crypto", "economy"],
    "美食探店": ["food", "restaurant", "recipe", "cooking", "dining"],
    "健身运动": ["fitness", "workout", "gym", "exercise", "training"],
    "育儿知识": ["parenting", "baby", "child", "pregnancy", "education"],
    "游戏攻略": ["game", "gaming", "esports", "video game", "gamer"],
    "情感心理": ["relationship", "dating", "marriage", "mental health", "psychology"],
    "汽车": ["car", "EV", "electric vehicle", "Tesla", "BYD", "auto", "automotive"],
    "房产": ["real estate", "housing", "property", "apartment"],
    "娱乐": ["entertainment", "celebrity", "movie", "tv show", "drama"],
    "体育": ["sports", "football", "basketball", "NBA", "Olympics"],
    "军事": ["military", "defense", "weapons", "army"],
    "国际": ["international", "global", "diplomacy", "US", "Europe"]
}

# 国内平台 API 端点
DOMESTIC_ENDPOINTS = {
    "微博": "https://60s.viki.moe/v2/weibo",
    "知乎": "https://60s.viki.moe/v2/zhihu",
    "百度": "https://60s.viki.moe/v2/baidu/hot",
    "抖音": "https://60s.viki.moe/v2/douyin",
    "B站": "https://60s.viki.moe/v2/bili",
    "今日头条": "https://60s.viki.moe/v2/toutiao"
}

# 免费微信公众号监控节点 (WeWeRSS 私有部署方案)
# 强烈建议在本地或服务器使用 Docker 部署 cooderl/wewerss
# 默认指向本地 WeWeRSS 服务，可以通过环境变量或参数覆盖
WEWERSS_BASE_URL = "http://127.0.0.1:4000/feeds/all.atom"

def get_wechat_articles(account_names: List[str]) -> Dict:
    """
    通过 WeWeRSS 节点获取最新文章。
    如果 account_names 包含 'all'，则不进行账号过滤，直接返回 WeWeRSS 订阅列表中的所有最新文章。
    """
    results = {}
    is_sync_all = 'all' in [name.lower() for name in account_names]
    
    # 初始化返回结构
    if not is_sync_all:
        for name in account_names:
             results[name] = {'platform': f'微信公众号 ({name})', 'data': [], 'error': None}
    else:
        results['全局监控'] = {'platform': 'WeWeRSS (全库同步)', 'data': [], 'error': None}

    try:
        headers = {'User-Agent': 'Trae-Agent/1.0'}
        response = requests.get(WEWERSS_BASE_URL, headers=headers, timeout=10)
        
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            is_atom = 'feed' in root.tag.lower()
            entries = root.findall('.//{http://www.w3.org/2005/Atom}entry') if is_atom else root.findall('.//item')
            
            for entry in entries:
                if is_atom:
                    title = entry.find('{http://www.w3.org/2005/Atom}title').text if entry.find('{http://www.w3.org/2005/Atom}title') is not None else ''
                    author = entry.find('.//{http://www.w3.org/2005/Atom}name').text if entry.find('.//{http://www.w3.org/2005/Atom}name') is not None else '未知公众号'
                    link = entry.find('{http://www.w3.org/2005/Atom}link').attrib.get('href', '') if entry.find('{http://www.w3.org/2005/Atom}link') is not None else ''
                else:
                    title = entry.find('title').text if entry.find('title') is not None else ''
                    author = entry.find('author').text if entry.find('author') is not None else '未知公众号'
                    link = entry.find('link').text if entry.find('link') is not None else ''
                
                # 全局同步模式：不挑食，只要是 WeWeRSS 抓到的，都记录下来
                if is_sync_all:
                    if len(results['全局监控']['data']) < 15: # 全局模式最多取 15 篇最新文章
                        results['全局监控']['data'].append({
                            'title': f"[{author}] {title}",
                            'link': link,
                            'source': 'WeWeRSS'
                        })
                else:
                    # 精确匹配模式：只记录特定的几个号
                    matched_account = None
                    for name in account_names:
                        if name.lower() in author.lower() or name.lower() in title.lower():
                            matched_account = name
                            break
                    
                    if matched_account and len(results[matched_account]['data']) < 3:
                        results[matched_account]['data'].append({
                            'title': title,
                            'link': link,
                            'source': 'WeWeRSS'
                        })
        else:
             error_msg = f'WeWeRSS 节点访问失败 (HTTP {response.status_code})。请确保您已通过 Docker 启动 WeWeRSS。'
             if is_sync_all:
                 results['全局监控']['error'] = error_msg
             else:
                 for name in account_names:
                     results[name]['error'] = error_msg

    except Exception as e:
         error_msg = f'无法连接 WeWeRSS 节点: {str(e)}。提示：这是一项需要您私有部署的高级功能。'
         if is_sync_all:
             results['全局监控']['error'] = error_msg
         else:
             for name in account_names:
                 results[name]['error'] = error_msg

    return results


def calculate_relevance_score(title: str, niche: str) -> int:
    """计算热点与用户领域的相关度得分（0-10）"""
    if not niche or niche not in NICHE_KEYWORDS:
        return 5  # 默认中等相关

    keywords = set(NICHE_KEYWORDS.get(niche, []))
    if niche in NICHE_KEYWORDS_EN:
        keywords.update(NICHE_KEYWORDS_EN[niche])

    if not keywords:
        return 5

    score = 0
    title_lower = title.lower()
    for keyword in keywords:
        if keyword.lower() in title_lower:
            score += 3
            if score >= 9:
                break

    return min(10, score)


def get_domestic_trends(platforms: List[str] = None, limit: int = 10) -> Dict:
    """获取国内热点"""
    results = {}
    if platforms is None:
        platforms = list(DOMESTIC_ENDPOINTS.keys())

    for name in platforms:
        url = DOMESTIC_ENDPOINTS.get(name)
        if not url:
            continue
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                items = []
                raw_data = data.get('data', [])

                # 解析不同平台的返回格式
                for idx, item in enumerate(raw_data[:limit], 1):
                    if isinstance(item, dict):
                        title = item.get('title', item.get('word', item.get('name', str(item))))
                        hot = item.get('hot', item.get('heat', item.get('num', '')))
                        items.append({
                            'rank': idx,
                            'title': str(title),
                            'hot': str(hot),
                            'relevance': 0  # 待计算
                        })
                    else:
                        items.append({
                            'rank': idx,
                            'title': str(item),
                            'hot': '',
                            'relevance': 0
                        })

                results[name] = {
                    'platform': name,
                    'data': items,
                    'update_time': data.get('update_time', ''),
                    'error': None
                }
            else:
                results[name] = {'platform': name, 'data': [], 'error': f'HTTP {response.status_code}'}
        except Exception as e:
            results[name] = {'platform': name, 'data': [], 'error': str(e)}

    return results


def get_overseas_trends_simulation(platforms: List[str] = None) -> Dict:
    """
    获取海外热点（模拟数据，因为需要 WebSearch）
    返回结构化提示，让 Claude 调用 WebSearch
    """
    if platforms is None:
        platforms = ['Reddit', 'TikTok', 'YouTube', 'Instagram']

    need_search = []
    for p in platforms:
        if p in ['Reddit', 'TikTok', 'YouTube', 'Instagram']:
            need_search.append(p)

    return {
        'type': 'overseas_search_needed',
        'platforms': need_search,
        'queries': {
            'Reddit': ['Reddit trending today', 'Reddit popular posts site:reddit.com'],
            'TikTok': ['TikTok trending today', 'TikTok viral videos trending'],
            'YouTube': ['YouTube trending today', 'YouTube trending videos'],
            'Instagram': ['Instagram trending hashtags today']
        },
        'message': '请使用 WebSearch 获取以下平台的热点信息'
    }


def annotate_trends_with_niche(trends: Dict, niche: str) -> Dict:
    """为热点标注相关度"""
    annotated = {}
    for platform, data in trends.items():
        if 'error' in data:
            annotated[platform] = data
            continue

        annotated_items = []
        for item in data.get('data', []):
            title = item.get('title', '')
            relevance = calculate_relevance_score(title, niche)
            item['relevance'] = relevance
            annotated_items.append(item)

        data['data'] = annotated_items
        annotated[platform] = data

    return annotated


def format_trends_for_display(trends: Dict, niche: str) -> str:
    """格式化热点数据用于展示"""
    output = []
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    output.append(f"获取时间: {timestamp}")
    output.append(f"用户领域: {niche}")
    output.append("")

    for platform, data in trends.items():
        if 'error' in data:
            output.append(f"### {platform}")
            output.append(f"获取失败: {data['error']}")
            output.append("")
            continue

        items = data.get('data', [])
        output.append(f"## {platform}")
        output.append("")
        output.append("| 排名 | 话题 | 热度 | 相关度 |")
        output.append("|------|------|------|--------|")

        for item in items:
            rank = item.get('rank', '')
            title = item.get('title', '')
            hot = item.get('hot', '')
            relevance = item.get('relevance', 0)
            fire = "🔥" if relevance >= 6 else ""
            output.append(f"| {rank} | {title} | {hot} | {relevance}/10 {fire} |")

        output.append("")

    return "\n".join(output)


def main():
    """主函数：解析参数并执行"""
    args = sys.argv[1:]

    # 默认参数
    niche = None
    scope = "all"  # domestic, overseas, all
    platforms = None
    wechat_accounts = [] # 新增微信账号参数

    # 解析参数
    i = 0
    while i < len(args):
        if args[i] == '--niche' and i + 1 < len(args):
            niche = args[i + 1]
            i += 2
        elif args[i] == '--scope' and i + 1 < len(args):
            scope = args[i + 1]
            i += 2
        elif args[i] == '--platforms' and i + 1 < len(args):
            platforms = args[i + 1].split(',')
            i += 2
        elif args[i] == '--wechat' and i + 1 < len(args):
            wechat_accounts = args[i + 1].split(',')
            i += 2
        else:
            i += 1

    # 如果没有提供领域，打印使用说明
    if not niche:
        print("请提供 --niche 参数")
        print("用法: python main.py --niche 'AI 人工智能' --scope all --wechat '卡兹克,饼干哥哥'")
        return

    # 获取热点数据
    results = {}

    # 国内热点
    if scope in ['domestic', 'all']:
        if platforms:
            domestic_platforms = [p for p in platforms if p in DOMESTIC_ENDPOINTS]
        else:
            domestic_platforms = None
        domestic_trends = get_domestic_trends(domestic_platforms)
        results.update(domestic_trends)
        
    # 微信公众号监控
    if wechat_accounts:
        wechat_trends = get_wechat_articles(wechat_accounts)
        results.update(wechat_trends)

    # 海外热点（返回搜索提示）
    if scope in ['overseas', 'all']:
        overseas_result = get_overseas_trends_simulation()
        results['__overseas__'] = overseas_result

    # 标注相关度
    annotated = annotate_trends_with_niche(results, niche)

    # 输出结果（JSON 格式供程序解析）
    json_output = json.dumps(annotated, ensure_ascii=False, indent=2)
    print(json_output)
    
    # 将最新数据保存到文件，供渲染看板使用
    try:
        import os
        base_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(base_dir, "latest_raw_data.json"), "w", encoding="utf-8") as f:
            f.write(json_output)
    except Exception as e:
        pass


if __name__ == "__main__":
    main()
```
