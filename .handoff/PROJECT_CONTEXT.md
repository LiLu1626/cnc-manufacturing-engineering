# Project Context — cnc-manufacturing-engineering

> ChatGPT 开工前必读。这里记录了项目的设计系统、目录结构、写作规范。
> Doubao 每次大改后应更新本文件。

## 项目是什么

CNC & Manufacturing Engineering 知识平台，GitHub Pages 静态站。
- URL: https://lilu1626.github.io/cnc-manufacturing-engineering/
- 仓库: LiLu1626/cnc-manufacturing-engineering，main 分支，从 /docs 发布
- 作者: Li Lu，有实际车间经验，目标读者是新人 machinist 和初级工程师
- 语言: 英文（全站）

## 目录结构（docs/ 下）

```
docs/
├── index.html              首页
├── robots.txt
├── sitemap.xml
├── assets/
│   ├── css/
│   │   ├── site.css        全站样式（导航、卡片、按钮、布局）
│   │   └── article.css      长文阅读样式（h1/h2/h3/p/table）
│   └── js/                 计算器逻辑
├── engineering-tools/      35 个计算器 + 首页
├── knowledge-base/         14 章知识库
├── machine-systems/        机器系统
├── cnc-programming/        CNC 编程教程（23 篇）
├── about/
├── cutting-tool-technology/   (规划中)
├── workholding-fixtures/     (规划中)
├── cnc-macro-programming/     (规划中)
├── ai-manufacturing/          (规划中)
└── engineering-case-studies/ (规划中)
```

## 设计系统（必须遵守）

### 颜色（CSS 变量，在 site.css :root）
```
--ink:            #17242f   正文
--muted:          #5c6872   次要文字
--surface:        #ffffff
--accent:         #0b766e   主色（青绿）
--accent-dark:    #07574f   标题/强调
--accent-light:   #e6f4f2   背景高亮
--border:         #cfdbd8
--radius:         18px
```

### 字体
- Inter, system-ui sans-serif
- 正文 1.6 line-height

### 布局容器
- 页面内容宽度：`min(100% - 32px, 1080px)`（板块首页/卡片页）
- 长文阅读宽度：`min(100% - 32px, 780px)`（.article）

### 全局导航（每个页面必须有）
```html
<nav class="site-nav">
  <div class="site-nav-inner">
    <div class="site-nav-brand">Li Lu <span>·</span> CNC Eng</div>
    <ul class="site-nav-links">
      <li><a href="/cnc-manufacturing-engineering/">Home</a></li>
      <li><a href="/cnc-manufacturing-engineering/engineering-tools/">Engineering Tools</a></li>
      <li><a href="/cnc-manufacturing-engineering/knowledge-base/">Knowledge Base</a></li>
      <li><a href="/cnc-manufacturing-engineering/machine-systems/">Machine Systems</a></li>
      <li><a href="/cnc-manufacturing-engineering/cnc-programming/">CNC Programming</a></li>
      <li><a href="/cnc-manufacturing-engineering/about/">About</a></li>
    </ul>
  </div>
</nav>
```
注意：用绝对路径 `/cnc-manufacturing-engineering/...` 保证子目录也能正确跳转。

### 返回按钮规范
每个二级页面（板块内文章）左上角必须有返回链接，**返回对应板块首页**，不是网站首页：
```html
<a class="back-link" href="/cnc-manufacturing-engineering/cnc-programming/">← Back to CNC Programming</a>
```
- 01 章文章 → 返回到 01 章首页，文字 `← Back to 01 · Machining Fundamentals`
- 以此类推

### 文章页结构
```html
<link rel="stylesheet" href="/cnc-manufacturing-engineering/assets/css/site.css">
<link rel="stylesheet" href="/cnc-manufacturing-engineering/assets/css/article.css">
...
<main class="article">
  <a class="back-link" href="...">← Back to ...</a>
  <h1>文章标题</h1>
  <p class="lead">导语</p>
  <h2>小节</h2>
  ...
</main>
<footer class="site-footer">Designed by Li Lu · CNC &amp; Manufacturing Engineering</footer>
```

### 计算器页结构
- 表单输入 → 实时计算结果 → 公式说明 → 举例 → 常见错误
- JS 放 `assets/js/` 或页面内 `<script>`
- 复用 site.css 的 `.card`、`.calculator` 等 class

## SEO 规范（每个新页面必须有）

```html
<title>页面标题 — CNC & Manufacturing Engineering</title>
<meta name="description" content="150 字以内描述页面内容">
<link rel="canonical" href="https://lilu1626.github.io/cnc-manufacturing-engineering/路径/">
```
新页面写完后，必须手动加到 `docs/sitemap.xml`。

## 写作规范

- **面向新人**：每个概念先讲"是什么、为什么重要"，再讲怎么用
- **必须举例**：抽象概念配具体数字例子（如"Ø10mm 铣刀，S=2000 RPM，进给=..."）
- **必须配图/示意图**：用 SVG 或 ASCII 图，不要留"这里放图"占位
- **工程数据要准确**：切削参数、公差、公式必须来自标准手册，不要编
- **结构统一**：Concept → Why → How → Example → Common Mistakes → Practice
- 长度：基础文章 800-1500 词，重点文章 2000-3000 词

## 技术栈

- 纯静态 HTML/CSS/JS，无框架，无构建步骤
- GitHub Pages 自动部署 main 分支
- 不引入外部 JS 库（保持轻量、加载快）
- 计算器用 vanilla JS，addEventListener + 实时更新

## 已完成模块清单（2026-09-24）

- Engineering Tools: 35 个计算器
- Knowledge Base: 14 章 42 篇
- Machine Systems: 13 章
- CNC Programming: 23 篇（01-31 学习路线）
- About
- SEO: robots.txt, sitemap.xml (125 URLs), Google Search Console 已验证
