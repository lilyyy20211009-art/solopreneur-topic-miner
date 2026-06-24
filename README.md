
# Solopreneur Topic Miner

一个面向自媒体人和独立创作者的爆款选题挖掘 Agent。它会根据你的创作赛道和目标受众，抓取多平台热点，进行趋势、竞争、匹配三维打分，最后输出 6 个更值得动笔的选题，并同步生成本地可视化看板。

当前默认配置：

- 创作赛道：AI 效率工具
- 目标受众：职场人
- 适用场景：日常选题、内容策划、热点追踪、公众号/小红书/短视频选题准备

## 核心功能

- 多平台热点抓取：微博、知乎、百度、抖音、B 站、今日头条等。
- 微信公众号监控：支持通过 WeWeRSS / RSSHub 接入订阅源。
- 三维评分筛选：趋势分、竞争分、匹配分。
- Top 6 选题推荐：每个选题包含差异化角度、标题备选和内容方向。
- 本地 HTML 看板：自动更新 `daily_topic_dashboard.html`。
- Trae Skill 支持：可作为 `.trae/skills/solopreneur-topic-miner` 使用。

## 目录结构

```text
.
├── .trae/
│   └── skills/
│       ├── frontend-design/
│       ├── solopreneur-topic-miner/
│       │   ├── SKILL.md
│       │   ├── fetch_trends.py
│       │   ├── render_dashboard.py
│       │   ├── user_profile.json
│       │   ├── latest_topics.json
│       │   └── latest_raw_data.json
│       └── ui-ux-pro-max-skill/
├── auto_miner.py
├── daily_topic_dashboard.html
├── topic_miner_tutorial.md
└── README.md
```

## 快速开始

进入项目目录：

```bash
cd "爆款选题 Agent 安装包"
```

查看当前用户配置：

```bash
cat .trae/skills/solopreneur-topic-miner/user_profile.json
```

抓取热点并生成选题数据：

```bash
python3 .trae/skills/solopreneur-topic-miner/fetch_trends.py \
  --niche "AI效率工具" \
  --scope domestic \
  --wechat "all"
```
重新渲染看板：

```bash
python3 .trae/skills/solopreneur-topic-miner/render_dashboard.py
```

打开看板：

```bash
open daily_topic_dashboard.html
```

## 作为 Skill 使用

这个项目内置了 Trae Skill：

```text
.trae/skills/solopreneur-topic-miner/SKILL.md
```

触发方式可以类似：

```text
帮我分析今天 AI 效率工具领域的爆款选题
```

或：

```text
我想使用选题挖掘功能，我的创作赛道是 AI 效率工具，目标受众是职场人
```

Agent 会读取 `user_profile.json`，然后按以下流程执行：

1. 拉取多平台实时热点。
2. 结合赛道和受众过滤话题。
3. 对候选话题做趋势、竞争、匹配三维打分。
4. 输出 Top 6 选题。
5. 更新 `latest_topics.json`。
6. 重新生成 `daily_topic_dashboard.html`。

## 输出格式

每个推荐选题通常包含：

- 话题标题
- 热点来源
- 趋势分、竞争分、匹配分
- 差异化切入角度
- 3 个爆款标题备选
- 内容大纲建议
- 看板展示配色

选题数据会写入：

```text
.trae/skills/solopreneur-topic-miner/latest_topics.json
```

原始抓取数据会写入：

```text
.trae/skills/solopreneur-topic-miner/latest_raw_data.json
```

## 配置说明

用户配置文件：

```text
.trae/skills/solopreneur-topic-miner/user_profile.json
```

示例：

```json
{
  "niche": "AI效率工具",
  "target_audience": "职场人",
  "created_at": "2026-04-20",
  "last_updated": "2026-04-20"
}
```

如果你要换赛道，可以改成：

```json
{
  "niche": "自媒体运营",
  "target_audience": "个人创作者",
  "created_at": "2026-04-20",
  "last_updated": "2026-06-24"
}
```

## 微信公众号数据源

项目支持两类公众号数据方案：

- WeWeRSS：适合本地或服务器私有部署。
- RSSHub：适合用公开 RSS 链接或 Folo 等工具辅助订阅。

相关文档：

- `RSSHub配置指南.md`
- `RSSHub公众号添加指南.md`
- `WeWeRSS替代方案.md`

如果公众号抓取失败，Agent 应如实记录，不应凭空编造公众号文章或热点。

## 自动化建议

可以用 cron 每天早上运行一次：

```bash
0 9 * * * cd "/Users/y/oversea-project/爆款选题 Agent 安装包" && \
  python3 .trae/skills/solopreneur-topic-miner/fetch_trends.py --niche "AI效率工具" --scope domestic --wechat "all" && \
  python3 .trae/skills/solopreneur-topic-miner/render_dashboard.py
```

运行后打开：

```text
daily_topic_dashboard.html
```

## 相关文档

- `topic_miner_tutorial.md`：完整使用教程
- `公众号发布教程.md`：面向发布和推广的说明
- `RSSHub配置指南.md`：RSSHub 接入方案
- `RSSHub公众号添加指南.md`：公众号添加步骤
- `WeWeRSS替代方案.md`：公众号 RSS 替代方案
                                                     
                                                                                                                                                                                                       

                                                                                                                                                                                                       
