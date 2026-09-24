# SPEC — CNC Programming Fundamentals & Applications

日期：2026-09-24  
状态：待实施；本次仅交付方案，不改网页、不提交或发布。  
依据：`.handoff/PROJECT_CONTEXT.md`、`.handoff/SPEC_TEMPLATE.md`，以及当前仓库实际页面。方案用中文交接；最终网站正文、标题、导航、图注、练习和代码注释全部英文。

## 任务标题

重做 CNC Programming 板块，建立从零基础、手工编程到铣削/车削完整应用、验证和 CAM 衔接的完整课程：**CNC Programming Fundamentals & Applications**。

## 背景与目标

### 现状与必须修复的问题

实查 `docs/cnc-programming/` 共 23 个 HTML 文件：1 个板块首页、20 个教学内容页、Quick Reference 和 Learning Path 各 1 页。PROJECT_CONTEXT 中“23 篇”是概括口径，不应当作 23 篇完整课程。编号缺少 08、11、19–22、27–29；01 的文章比其他文章多一层目录。现有课程页 31 明确把完整车铣程序、螺纹、子程序、控制器差异和练习列为后续内容。

已逐页阅读：首页、01 入门、12 刀补、15 圆弧、17 钻孔、24 验证、31 路线；并查看 `site.css`、`article.css`。现有风格可继承，但内容不能原样搬运：

- 代表文章偏短，缺少完整的先修说明、逐步计算、错误诊断、练习答案；部分缺 description/canonical，导航没有完整 Home 项，路径多为相对路径。
- 15 的起点 (0,0)、终点 (20,20)、圆心 (0,20) 对应 G17 下从 +Z 看向原点的 **G03 逆时针 90°短弧**；原文 G02 会走同圆 270°长弧。重做须对齐代码、图、文字和角度。
- 12 的 “Machine position + Work offset + Tool length offset = Actual tool tip position” 未定义坐标和符号，不能当通用公式；“程序结束一定 G49”也不能脱离机型与当前位置使用。
- 17 把 G84 一概称为 rigid tapping，未区分设备配置；固定循环和 G98/G99 必须写明机床类别、控制器和模式。不要把钻头形状造成的孔底形状归因于 G82。
- 24 不能把 dry run、抬刀、倍率、single block 描述为能证明绝对安全的办法；仿真是否包含夹具、刀柄、机床运动学必须明确。
- `article.css` 当前段落/列表行高 1.75，与 PROJECT_CONTEXT 1.6 不同；本板块采用局部覆盖至 1.6，不扩大为全站样式重构。

### 学习成果与边界

读者无需既有 G-code 知识；学完能读懂图纸和坐标、解释模态状态、计算基本转速与进给、编写并解释三轴铣削和两轴车削训练程序、准备装夹与刀具表、查控制器手册、建立验证与首件检查记录。课程不把纸面学完等同于独立操作机床资格。

完整范围：基础 → 坐标/数学/图纸 → 编程语言 → 速度进给/刀补/工件零点 → 直线/圆弧/补偿 → 铣削与孔加工 → 车削与螺纹 → 子程序/宏入门 → 工艺与 CAM → 程序验证/故障处理 → 综合项目和评估。多轴、探测和宏只教进入后续专业学习所需的基础，不宣称覆盖完整五轴、OEM 探测循环或全部宏功能。

“CNC Programming Fundamentals & Applications”在此作为课程总标题和学习目标，不假定为某本书的目录，不复制未提供的教材。

### 教学基准

- 主线：公制、三轴立式铣床、两轴车床；示例方言选择 **Haas 官方手册可核实的 ISO 风格代码**。每个程序标明 Mill/Lathe、控制器、所需选项和坐标约定。Haas 不是所有 FANUC/Siemens 的代名词。
- 基础数学与原理可跨控制器；专有代码及参数不能跨机型照搬。FANUC/Siemens 只在差异页引用具体型号/版本手册后写语法；无法取得来源时只讲需核查的差异，不编造对照代码。
- 尺寸是明确标识的教学设计值；切削速度、每齿进给等若为算术假设，写 “Assumed for this calculation; not a cutting recommendation”。生产推荐值必须有对应材料、刀具牌号/几何、工况和厂商数据出处。
- 所有文章必须按 **Concept → Why → How → Example → Common Mistakes → Practice** 六段顺序组织；可在 How/Example 下加英文 H3。前置 lead、学习目标和先修，末尾答案、来源、上一课/下一课。
- 基础篇 B：800–1500 英文词；重点篇 K：2000–3000 英文词。统计可读正文，不靠代码、导航、来源表凑数。Reference 等服务页按 B 深度撰写，首页不受文章词数约束。

## 交付物清单

### 页面文件（完整清单，无省略路径）

M = 保留现有 URL 并全面重写；N = 新建。编号是稳定资源 ID，**不是强制阅读顺序**；页面展示模块和课名，阅读顺序以下文课程表为准。保留全部 23 个旧 URL，无需重定向。

| ID | 操作 | 页面文件 | 英文标题 | 深度 |
|---|---|---|---|---|
| 00 | M | `docs/cnc-programming/index.html` | CNC Programming Fundamentals & Applications | 首页 |
| 01 | M | `docs/cnc-programming/01-getting-started/what-is-cnc-programming/index.html` | What Is CNC Programming? | B |
| 02 | M | `docs/cnc-programming/02-machine-fundamentals/index.html` | Machine Fundamentals for Programmers | B |
| 03 | M | `docs/cnc-programming/03-coordinate-systems/index.html` | Coordinate Systems and Positioning | K |
| 04 | M | `docs/cnc-programming/04-program-structure/index.html` | Reading and Structuring a CNC Program | B |
| 05 | M | `docs/cnc-programming/05-gcode-fundamentals/index.html` | G-Code Fundamentals | B |
| 06 | M | `docs/cnc-programming/06-modal-codes/index.html` | Modal State and Program Execution | K |
| 07 | M | `docs/cnc-programming/07-plane-units/index.html` | Planes, Units, and Numeric Conventions | B |
| 08 | N | `docs/cnc-programming/08-programming-math/index.html` | Practical Mathematics for CNC Programming | K |
| 09 | M | `docs/cnc-programming/09-mcode-fundamentals/index.html` | M-Codes and Machine Functions | B |
| 10 | M | `docs/cnc-programming/10-spindle-feed/index.html` | Spindle Speed and Feed Programming | K |
| 11 | N | `docs/cnc-programming/11-controller-dialects/index.html` | Controller Dialects and Manual Reading | B |
| 12 | M | `docs/cnc-programming/12-tool-offsets/index.html` | Tool Length, Geometry, and Wear Offsets | K |
| 13 | M | `docs/cnc-programming/13-work-offsets/index.html` | Work Offsets and Datum Setting | K |
| 14 | M | `docs/cnc-programming/14-linear-interpolation/index.html` | Rapid Positioning and Linear Interpolation | K |
| 15 | M | `docs/cnc-programming/15-circular-interpolation/index.html` | Circular and Helical Interpolation | K |
| 16 | M | `docs/cnc-programming/16-cutter-compensation/index.html` | Cutter Radius Compensation | K |
| 17 | M | `docs/cnc-programming/17-drilling-cycles/index.html` | Drilling, Pecking, and Boring | K |
| 18 | M | `docs/cnc-programming/18-canned-cycles/index.html` | Canned-Cycle State and Hole Patterns | K |
| 19 | N | `docs/cnc-programming/19-turning-fundamentals/index.html` | Turning Coordinates and Basic Toolpaths | K |
| 20 | N | `docs/cnc-programming/20-turning-cycles/index.html` | Turning Roughing and Finishing Cycles | K |
| 21 | N | `docs/cnc-programming/21-grooving-parting-boring/index.html` | Grooving, Parting, and Internal Turning | K |
| 22 | N | `docs/cnc-programming/22-threading/index.html` | Single-Point Thread Programming | K |
| 23 | M | `docs/cnc-programming/23-program-safety/index.html` | Safe Program Start, Retraction, and Restart | K |
| 24 | M | `docs/cnc-programming/24-verification/index.html` | Program Verification and First-Article Checks | K |
| 25 | M | `docs/cnc-programming/25-troubleshooting/index.html` | Diagnosing CNC Program Problems | K |
| 26 | M | `docs/cnc-programming/26-common-mistakes/index.html` | Common Beginner Mistakes and Corrections | B |
| 27 | N | `docs/cnc-programming/27-turning-project/index.html` | Worked Project: A Stepped Shaft | K |
| 28 | N | `docs/cnc-programming/28-milling-project/index.html` | Worked Project: A Pocketed Mounting Plate | K |
| 29 | N | `docs/cnc-programming/29-subprograms/index.html` | Subprograms and Repeated Features | K |
| 30 | M | `docs/cnc-programming/30-reference/index.html` | CNC Programming Quick Reference | B |
| 31 | M | `docs/cnc-programming/31-learning-path/index.html` | Learning Path and Progress Checkpoints | B |
| 32 | N | `docs/cnc-programming/32-drawings-process-planning/index.html` | From Engineering Drawing to Process Plan | K |
| 33 | N | `docs/cnc-programming/33-milling-strategies/index.html` | Facing, Slots, Pockets, and Contours | K |
| 34 | N | `docs/cnc-programming/34-tapping-thread-milling/index.html` | Tapping and Thread Milling | K |
| 35 | N | `docs/cnc-programming/35-cad-cam-postprocessing/index.html` | CAD, CAM, and Post-Processor Verification | K |
| 36 | N | `docs/cnc-programming/36-macro-foundations/index.html` | Variables, Logic, and Macro Foundations | K |
| 37 | N | `docs/cnc-programming/37-multiaxis-probing-overview/index.html` | Rotary Axes, Multi-Axis Motion, and Probing | B |
| 38 | N | `docs/cnc-programming/38-process-optimization/index.html` | Cycle Time, Quality, and Process Improvement | K |
| 39 | N | `docs/cnc-programming/39-exercises-assessment/index.html` | Practice Projects and Final Assessment | K |
| 40 | N | `docs/cnc-programming/40-glossary-sources/index.html` | CNC Programming Glossary and Source Guide | B |

合计：41 个 HTML 页面 = 23 个重写 + 18 个新建；其中 40 个课程/服务页 + 1 个首页。不得以“Coming soon”卡片代替已列交付页。

### 支持文件与跨页修改

- 新建 `docs/assets/css/cnc-programming.css`：本板块限定作用域的代码块、表格滚动、目录、课程元信息、图例、练习、导航换行与打印样式。采用 `.cnc-programming` body class；不得改全站变量。
- 修改 `docs/sitemap.xml`：保留并核对旧 23 个 URL；加入 18 个新 canonical，去重。不要依据 PROJECT_CONTEXT 的旧全站数量强行改成某个固定总数。
- 修改 `docs/index.html`：仅校准 CNC Programming 入口文案/课程数量（若存在旧数量），链接仍指向板块首页。
- 所有图使用每页内联 SVG；不另建散落图文件。代码直接写入 HTML `<pre><code>`；此期不交付单独可下载的机床运行文件。
- 不增加 JS 文件或外部库；练习答案采用原生 `<details><summary>`，目录是普通锚点。无需进度数据库、账号、仿真器或实时机床连接。
- 本 SPEC 不要求修改 PROJECT_CONTEXT、SPEC_TEMPLATE 或其他板块正文；实际完成后的状态更新由项目既有交接流程处理。

## 页面结构 / 内容大纲

### A. 完整学习路线与先修关系

| 模块 | 英文模块名 / 首页锚点 | 顺序（ID） | 进入条件与出口作业 |
|---|---|---|---|
| 1 | Foundations / `#foundations` | 01 → 02 → 23 → 08 → 32 → 03 | 零基础；能画机床轴、说明夹具边界、列出零件坐标 |
| 2 | Language and Control / `#language` | 07 → 04 → 05 → 06 → 09 → 11 | 会读坐标；交逐行状态表和方言核查表 |
| 3 | Setup and Motion / `#setup-motion` | 10 → 13 → 12 → 14 → 15 → 16 | 状态表正确；完成坐标/刀补计算、直线和圆弧回绘 |
| 4 | Milling Applications / `#milling` | 33 → 17 → 18 → 34 → 29 | 完成基础运动；交口袋、孔阵列与螺纹方法选择 |
| 5 | Turning Applications / `#turning` | 19 → 20 → 21 → 22 | 已掌握模块 1–3；铣削代码不能直接迁移车床 |
| 6 | Verification and Projects / `#verification-projects` | 重读 23 → 24 → 25 → 26 → 28 → 27 | 完成相关分支；交两份完整程序包及检验记录 |
| 7 | CAM and Further Applications / `#cam-advanced` | 35 → 36 → 37 → 38 → 39 | 完成至少一个项目；交后处理对照、宏追踪表与总评 |
| R | Reference / `#reference` | 31、30、40 随时查阅 | 31 是课程路线；30 查代码；40 查术语与来源 |

23 先读“开始工作前的检查”和基本危险，再在项目阶段读完整启停/重启示例。前置段不要求理解尚未教学的 G-code；详细代码标“Return after Lessons 06, 12, and 13”。24 同理提供基础检查入口，可从任何运动页跳转。

首页和 31 使用同一顺序；文章上一课/下一课按上表首次出现的教学顺序串联，不按 URL 数字排序。23 的首次出口为 08，复习区另链 24；31/30/40 提供“Start the course”而不是假装是连续教学末课。每页写明具体先修 ID 对应的真实链接。

### B. 所有文章共用的内容合同

- lead 用 2–3 句回答读者将解决什么；列 3–5 条可考核目标、先修链接、B/K 阅读深度及机器/控制器适用范围。
- 下文逐页的 1–6 项分别对应六个统一 H2；每个 How 至少展开两个解释性小节。首次出现术语用一句普通英语解释，不能只给代码表。
- 每篇至少 1 个完整数字例题，含已知量、单位、推导、结果、回验；K 篇至少 2 个例题或一个完整项目加独立变式。
- 每篇至少 1 张有解释作用的实际 SVG/ASCII 图；K 篇至少 2 张不同用途的图。下文“图”是实施规格，交付页面必须画出，不允许保留占位。
- 每篇 Practice 至少“理解题 + 数值题 + 找错/应用题”三题，答案包括过程、适用前提、常见错答原因；下文给出必含的锚点题，其余两题围绕同节目标展开。39 为综合考试，数量另定。
- 每个代码框标记 **Fragment** 或 **Complete training program**。片段写所依赖的模态、起点和刀具状态；完整程序有工具/偏置表、坐标图、机型、起终状态、退刀和验证记录要求。`...` 和缺失关键段不能称完整。
- 单行注释解释“为什么”，旁边有行号—状态—位置—动作表；错误代码仅出现在明确的诊断框中，和正确代码分开。
- 页面结尾“Sources and applicability”列具体资料标题、版本/检索日期、章节或页码；公式、控制器行为和真实推荐参数附近也需有来源指向。

### C. 首页 00

1. Hero：英文总标题、课程目标、主按钮 Start with What Is CNC Programming，次按钮 View the Learning Path。
2. Before You Start：不要求先学编程；需要四则运算；说明训练程序适用机型和实机学习边界。
3. 七模块路线与 Reference：每组写学习成果，卡片给课名、基础/重点、先修简述；41 页清单中的其余 40 页全部有入口。
4. 两条应用分支：Milling 与 Turning；共享基础完成后可分别学习，综合路线要求两条都学。
5. 两个最终作品预览：100 × 80 × 12 mm 板件和 Ø40 mm 棒料阶梯轴，链接 28/27。图：并排 SVG 零件轮廓与原点，说明是教学工件。
6. Reference & Tools：31/30/40；链接已存在的 spindle-speed-calculator、feed-rate-calculator、hole-pattern-generator、printable-setup-worksheet。工具仅辅助，正文仍展示公式步骤。
7. 保留旧首页锚点 `ch01/ch05/ch10/ch14/ch17/ch23/ch30` 作为同页兼容定位点，映射到对应新模块或运动小组；可使用不可见但可定位的 span id，不制造重复 ID。

### D. 逐篇文章规格（标题和文件路径以清单为准）

#### 01 · What Is CNC Programming? — B
1. Concept：解释程序、机床、控制器、刀路的关系；区分 NC 文件与 CAM 工程文件。
2. Why：一块 60 × 40 mm 板的两个孔如何从图纸变成坐标与检验项目；不能仅说“自动化更快”。
3. How：图纸 → 工艺 → 装夹/刀具 → 代码 → 验证 → 首件；手工编程与 CAM 各适用的几何复杂度。
4. Example：孔中心 (10,10)、(50,30)，先用普通语言写动作，再解释 `X50 Y30`、S2000、F200 的不同含义；不提供未解释的完整程序。图：七步流程 SVG，附两孔板小坐标图。
5. Common Mistakes：把坐标当距离；把 S 当直线速度；认为 CAM 输出无需检查。
6. Practice：两孔位移答案 ΔX=40、ΔY=20 mm；另让读者给简单轴和自由曲面选择手工/CAM并说明理由。

#### 02 · Machine Fundamentals for Programmers — B
1. Concept：铣床刀具旋转、车床工件旋转；轴、主轴、刀库/刀塔、行程和机床参考位置。
2. Why：同样的 X20 在铣床和直径模式车床意义不同；指令坐标不等于从任意视角看到的工作台移动方向。
3. How：用刀具相对工件的正方向定义 X/Y/Z，解释右手系、回参考点和工作零点的差别；刀柄/卡盘也占空间。
4. Example：车床直径从 X40 到 X30，径向移动 5 mm；铣床 X10 到 X30 则位移 20 mm。图：铣床 XYZ 与车床 XZ 并排，标观察方向。
5. Common Mistakes：混淆 home 与零件零点、忽略刀塔/夹具包络、凭照片判断轴正负。
6. Practice：X50→X46 的车床径向位移 2 mm；解释为何同一 XYZ 坐标不保证刀柄无碰撞。

#### 03 · Coordinate Systems and Positioning — K
1. Concept：点、轴、正负号；机器坐标、工件坐标、绝对目标和增量位移分别是什么。
2. Why：一套轮廓换装夹位置为何可以保持零件坐标；错误坐标系使所有孔系统性偏移。
3. How：先画 XY 四象限，再引入 Z；G90/G91 仅按本课铣床语境；说明端点模式不自动定义圆心模式。介绍 G54/G53，具体设置移交 13。
4. Example：A(10,10)→B(40,10)→C(40,30)：绝对端点与增量 (30,0)、(0,20) 对照；简化未旋转 XY：机器零件原点 W=(-300,-200)，工件 P=(40,30)，机器 P=(-260,-170)。图：双坐标系叠图、绝对/增量两条重合轨迹。第二例返回 A 的增量 (-30,-20)。
5. Common Mistakes：忘恢复 G90、把 G53 视为持续模态、在有旋转/缩放时仍套简单平移公式。
6. Practice：A(5,8) 到 B(-5,18)，Δ=(-10,+10)；错误增量重复两次的终点推演；答案逐段追踪。

#### 04 · Reading and Structuring a CNC Program — B
1. Concept：程序号、block、address word、数值、小数点、注释及文件结束。
2. Why：一行是多种状态与动作组合，不能把每个字母当作按书写顺序独立执行。
3. How：头部/设置/换刀/定位/加工/退刀/结束；说明 O/N/T/H/D/S/F 的角色，T 与 H 的配对由设置保证。
4. Example：逐字拆解 `G01 X25. Y10. F200.`；给已知起点 (5,10)、G21/G90/G94 的片段，计算 20 mm 理想匀速段为 6 s。图：程序骨架及地址词标注。
5. Common Mistakes：N 当移动量、F/S 混淆、小数格式依赖控制器未说明、M30 当退刀动作。
6. Practice：为三个加工段补注释和缺失的模式声明；距离 30 mm、F300 的理想时间为 6 s。

#### 05 · G-Code Fundamentals — B
1. Concept：G-code 选择运动或控制功能，先分运动、坐标、单位、补偿、循环。
2. Why：认识类别比背完整代码表更能发现危险状态。
3. How：G00 与 G01 的用途，G02/G03 的圆弧含义；只概览 G17/G21/G40/G54/G80/G90，细节链到专课。
4. Example：已在安全高度 Z20，按 X0→X30 定位，再在已确认条件下讲一段 X30→X50 F100 的教学切削位移；20 mm 理想用时 12 s。图：带图例的快速虚线与进给实线，不画成保证的 G00 实际直线轨迹。
5. Common Mistakes：快速穿过毛坯、以为 F 控制快速、认为所有控制器代码含义相同。
6. Practice：给四种动作选代码；找出把 Z-2 下刀写成 G00 的问题并描述修正所需条件。

#### 06 · Modal State and Program Execution — K
1. Concept：模态是会保留的状态；非模态只作用于特定 block；启动/复位后的默认值不能猜。
2. Why：同一行 `X10` 的动作取决于前文，不应脱离上下文审程序。
3. How：按 motion/plane/units/distance/feed/offset/cycle 分栏追踪；同组冲突和 reset 行为查手册；子程序继承/改变状态。
4. Example：G90 G01 X10 F100 → X20 → G91 X5 → X5，从 X0 得 10/20/25/30；第二例 G81 后只有 XY 的行会继续孔循环（限定控制器语义）。图：四行状态时间轴、循环启用—执行—取消状态图。
5. Common Mistakes：只补 F 不看 feed mode；中途启动丢失 G54/H；以为 M30 后所有机床状态一致。
6. Practice：补全八行状态表；从 X20 误留 G91 再写 X30 得 X50，解释预期 X30 与实际差别。

#### 07 · Planes, Units, and Numeric Conventions — B
1. Concept：G17 XY、G18 XZ、G19 YZ；G20/G21；长度单位与进给模式是两件事。
2. Why：错误单位会把 1 mm 意图变成 25.4 mm；平面影响插补/补偿/循环适用性。
3. How：圆弧观察方向明确为从正法向看向原点；英制/公制换算与小数表示；不假定切单位会同步正确转换全部偏置。
4. Example：1 in=25.4 mm，0.25 in=6.35 mm；F10 in/min=254 mm/min。图：三个平面法向与带单位的同长度标尺。
5. Common Mistakes：把 G18 的视角照搬 XY 图、无单位数值、改 G21 后忽略工件/刀具偏置核查。
6. Practice：12.7 mm=0.5 in；指出同一 X1 在两种单位下的比例差。

#### 08 · Practical Mathematics for CNC Programming — K
1. Concept：四则、符号、半径/直径、勾股、角度和三角函数；假设读者未学过三角。
2. Why：坐标、孔阵列、斜线、圆弧端点都要由尺寸转成数值。
3. How：用直角三角形解释 sin/cos/tan；角度制；X=Xc+R cosθ、Y=Yc+R sinθ；保留精度后统一舍入。
4. Example：3-4-5 三角形；PCD100 的四孔 (50,0)/(0,50)/(-50,0)/(0,-50)；60°点 (25,43.301)。第二例长度 20、角度30°位移 (17.321,10)。图：三角形标边、孔圆标零角和逆时针。
5. Common Mistakes：PCD 当半径、弧度输入、负象限丢符号、过早四舍五入。
6. Practice：中心 (10,20)、半径20、90°点=(10,40)；写完整计算过程。链接现有 hole-pattern-generator 和 arc-and-chord-calculator。

#### 09 · M-Codes and Machine Functions — B
1. Concept：辅助功能及其依赖 OEM 的性质；与 G-code 分工。
2. Why：刀具/冷却/主轴状态是切削条件，不是几何代码之外可忽略的细节。
3. How：在声明的铣床语境讲 M03/M04/M05、M08/M09、M00/M01、M06、M30；M01 依赖开关，换刀动作和一块允许多少 M-code 查机床手册。
4. Example：T02、S1500、M03 的工具—主轴状态追踪；M00 用于教学检查点，强调停止不代替安全隔离。图：换刀→定位→切削→结束状态流程。
5. Common Mistakes：车床照抄 M06、M05 当轴停止/安全隔离、M30 前不退刀。
6. Practice：解释 M01 开关开/关时的两种流程；把五个动作排序并说明机床依赖项。

#### 10 · Spindle Speed and Feed Programming — K
1. Concept：Vc、n、fz、z、fn、vf，分别给名称和单位；刀具直径与车削工件直径区分。
2. Why：相同 F 在不同进给模式下完全不同；推荐切削数据需与刀具和材料匹配。
3. How：n=1000Vc/(πD)，vf=n×z×fz，vf=n×fn；铣床 G94/G95 与车床 G98/G99 分开解释；车削 G96/G97 和转速限制。
4. Example：假设 D10、Vc62.832 m/min 得 n≈2000 rpm，4齿、fz0.03 得 F240 mm/min；车削 Vc150、D50 得955 rpm，D25 得1910 rpm，教学上限1800时被限制。图：每齿进给示意与恒线速 n-D 曲线。另以 n1000、fn0.2 得200 mm/min。
5. Common Mistakes：fz 当每转进给、CSS 靠近中心不限制转速、把假设参数当材料推荐值。
6. Practice：3齿、3000 rpm、fz0.02 得180 mm/min；D20、Vc100 得1592 rpm，解释为何还要查机床/夹持限制。

#### 11 · Controller Dialects and Manual Reading — B
1. Concept：相似 G-code 表面下存在机型、系列、参数和选项差异。
2. Why：Haas 铣床的 G98/G99 与 Haas 车床同号码含义不同，足以说明跨机型复制的风险。
3. How：按“机型→软件版本→代码条目→参数单位→模态组→示例条件→设置/选项”读手册；分别建立 Haas、FANUC、SINUMERIK 的查证清单，不做未经核实的万能翻译表。
4. Example：以 n1000、车床 fn0.2 的200 mm/min，与铣孔初始 Z20/R5 的返回高度对照；数字相同的代码并非相同语义。图：找手册的决策树。
5. Common Mistakes：用品牌替代型号版本；把英制手册示例数值直接换个 G21；不核验钻孔 Q/P 单位。
6. Practice：为一段含 G98、G76、P/Q 的代码列出至少六项缺失上下文，不允许凭猜测判定安全。

#### 12 · Tool Length, Geometry, and Wear Offsets — K
1. Concept：铣床刀长 H、半径/直径 D、几何与磨损；T 是选刀，H/D 是寄存器引用，不强制天然相等。
2. Why：120 mm 与100 mm刀长混用可能造成20 mm位置误差；误差方向需看符号和测量约定。
3. How：定义主轴基准面、刀尖、Z 正方向和测量基准；G43/G49 行为按手册；演示启用前核对工具表。车床几何/磨损与刀尖方向仅概览，详见19/21。
4. Example：仅在图示简化坐标定义中，工件原点机器Z=-400、目标刀尖工件Z=10、正刀长L=100，则刀尖机器Z=-390、基准面机器Z=-290；L=120 时基准面需为-270。强调这是几何推导而非所有控制器显示值公式。第二例 T02/H07 明确绑定。图：基准面—刀尖尺寸链、工具与寄存器配对表图。
5. Common Mistakes：继承旧文通用加法公式；在靠近工件时盲目取消刀长；半径/直径寄存器混用；把几何设置误差全放进 wear。
6. Practice：L80 的同一条件基准面为-310；找出表中 T03 对应 H02 的异常并指出核验方法，而不是直接改号。

#### 13 · Work Offsets and Datum Setting — K
1. Concept：设计基准、设置基准、编程零点和 G54–G59 的关系。
2. Why：两夹位应复用局部坐标，不应到处手改刀路。
3. How：先介绍寻边/测头/量块的测量原理和半径补偿；描述“测量→记录→独立复核”，不提供未知机型的按键操作；区分工件Z和刀长，G53 仅用于机床坐标语境。
4. Example：G54 原点机器XY=(-300,-200)，G55=(-150,-200)，同一局部孔(20,10)对应(-280,-190)、(-130,-190)。第二例 Ø10寻边器接触左边时中心比边缘左5 mm，图示后推导边缘位置。图：双装夹坐标图、寻边器中心与边缘尺寸链。
5. Common Mistakes：左右边补偿符号反、重复加入刀长、把重启当重新建立零点。
6. Practice：第二工位沿机器X再平移40 mm，局部孔仍不变；计算新机器孔点(-90,-190)，并列独立检验步骤。

#### 14 · Rapid Positioning and Linear Interpolation — K
1. Concept：快速定位与切削进给；端点、路径、同步插补和包络是不同概念。
2. Why：G00 端点看似安全，中间路径/刀柄仍可能经过夹具。
3. How：先确认安全Z包络，再XY、再受控接近；G00路径依控制器，不能保证斜直线；进给长度和理想时间，区分切削与非切削动作。
4. Example：夹具顶Z12、教学横移高度Z20，图示名义间隙8 mm且仍需考虑刀柄/工件；从(0,0)到(30,40)，G01路长50 mm，F250理想12 s。第二例展示同时XYZ快速与分段退刀/横移的包络差异。图：俯视路径及夹具剖面。
5. Common Mistakes：把工件Z5当万能安全高度、认为F限制G00、退刀时先横移。
6. Practice：夹具增高到Z24，则Z20不足，不能简单沿用；由读者提出有说明的新的教学高度并重画路径。

#### 15 · Circular and Helical Interpolation — K
1. Concept：起点、终点、圆心、半径、方向、平面；G02/G03 的方向依观察法向。
2. Why：端点相同可对应长短两条弧；错方向不一定报警。
3. How：G17下I/J按本基准手册为起点到圆心的偏移；G90不等于圆心绝对模式。对比R和IJK、整圆、180°附近数值敏感性；螺旋增加Z并声明控制器支持条件。
4. Example：S(0,0)、C(0,20)、E(20,20)，I0 J20，G03短弧90°、弧长10π≈31.416 mm；G02为270°、94.248 mm。第二例圆心(10,10)、起点(20,10)，R10螺旋一圈Z0→-2；展示分段圆弧并累计Z，标明刀具允许斜坡切削。图：原错误的长短弧对照、螺旋侧视图。
5. Common Mistakes：SVG屏幕Y向下导致箭头反、IJK和端点模式混淆、起終半径不等、认为“不确定就用R”能解决几何错误。
6. Practice：S(10,0)、C(0,0)、E(0,10)得到I=-10、J=0、G03 90°；两端半径均10，答案含检验式。

#### 16 · Cutter Radius Compensation — K
1. Concept：零件轮廓与刀心轨迹；G41/G42 是沿前进方向的左/右，不是纸面固定左右。
2. Why：换刀/磨损时希望保持轮廓程序；先理解手工刀心偏移再用控制器补偿。
3. How：D寄存器格式、补偿启用/取消、引入/引出、内角半径限制；按选定控制器核查最短引入距离和允许块类型；分清 full radius 与 wear compensation。
4. Example：沿+X走Y0轮廓，刀半径5，左侧刀心Y+5、右侧Y-5；内角R3无法由R5刀切出。第二例半径改4.9时刀心偏置变化0.1 mm，磨损符号必须依据内外轮廓和控制器方式推导。图：运动箭头与左右偏置、引入引出和内角包络。
5. Common Mistakes：重复CAM偏置加全半径补偿、在轮廓上直接取消、半径与直径值混用。
6. Practice：沿-X方向时左侧在-Y；给矩形轮廓判四边刀心侧，不能死记G41=外轮廓。

#### 17 · Drilling, Pecking, and Boring — K
1. Concept：spot/drill/peck/ream/bore 的功能及孔深定义；盲孔/通孔。
2. Why：孔底目标和钻尖位置不同，排屑策略取决于刀具及材料，不能把深径比阈值编成通用规则。
3. How：G81基础钻孔、G82驻留、G83排屑、G85进给进退；R平面、Z终点、F、Q/P单位必须引用手册；G84转34讲。
4. Example：顶面Z0，R5、目标钻尖Z-15，进给段20 mm；另 Ø10、118°钻尖的几何尖高 h=5/tan59°≈3.004 mm，厚12 mm板完整直径突破需钻尖超过-15.004，额外余量另作明确工艺设计。图：钻尖/板厚剖面、G81与G83路径对照。
5. Common Mistakes：把Z-12当整个Ø10孔已通透；G82能自动生成平底孔；忽略背面夹具；将Q当绝对Z。
6. Practice：Ø6、118°尖高≈1.803 mm；8 mm板几何突破位置≈-9.803 mm，解释实际方案还需查刀具几何、毛刺和余量。

#### 18 · Canned-Cycle State and Hole Patterns — K
1. Concept：循环模态、初始平面、R平面及G80取消；与17的工艺选择区分，本篇教状态/复用。
2. Why：同一循环在每个孔持续生效，返回高度决定跨孔是否越过夹具。
3. How：在G90/G17公制铣床基准下逐阶段展开循环；G98初始高度返回、G99 R平面返回；G91与重复参数仅以单独受支持示例说明。
4. Example：孔(10,10)/(50,10)/(50,30)/(10,30)，初始Z20、R3、孔底-8；跨孔路径上夹具顶Z10时R3不足。第二例PCD40四孔使用08的计算。图：G98/G99两种高度剖面、孔序俯视图。写出G80后再移动的状态表。
5. Common Mistakes：低R跨夹具、忘记取消循环、车床G98/G99套用铣床释义、移动前只看XY端点。
6. Practice：G99返回高度3而非20；要求提出经包络核验的G98方案并指出它仍不能保证刀柄无碰撞。

#### 19 · Turning Coordinates and Basic Toolpaths — K
1. Concept：XZ、直径模式、Z0端面、负Z入工件、刀尖方向；按所选机器定义方向。
2. Why：车床X变化与径向切深相差2倍，铣床模态概念不能照搬。
3. How：端面/外径/台阶/锥面运动、刀塔和工件包络；T格式、几何与磨损、G18、固定RPM/CSS基准；G90在部分车床是循环而非铣床绝对模式。
4. Example：毛坯Ø40，车Ø30×30 mm，X40→X30是径向5 mm，不是建议一次切完。第二例从X30 Z-20到X20 Z-40，锥半角atan(5/20)≈14.036°。图：直径/半径标注和XZ轮廓；配虚拟刀尖与刀鼻圆弧图，解释锥面需正确鼻圆补偿。
5. Common Mistakes：把X当半径、刀尖方向号猜填、CSS无上限、在靠卡爪处换刀。
6. Practice：X36→X32径向2 mm；给两段轮廓列XZ端点与卡爪边界，先绘图再写片段。

#### 20 · Turning Roughing and Finishing Cycles — K
1. Concept：粗加工分层去料、留余量、精加工跟随最终轮廓；循环只是压缩动作描述。
2. Why：轮廓块被循环复用，错误端点/余量会重复执行，不能只看一行G71。
3. How：先手工展开几刀再介绍选定Haas手册的G71/G70和端面粗加工G72；写明参数的径向/直径量、P/Q引用、轮廓限制与Type I/II适用性。FANUC两行格式只作为差异提醒。
4. Example：Ø40粗至Ø30.4再精到Ø30，直径余量0.4对应径向0.2；教学径向步深1.5时说明直径每次减少3，不把此值作为推荐。第二例肩部Z-30、端面轴向留0.2的轮廓表。图：分层材料带、粗/精轮廓对比。
5. Common Mistakes：余量按错直径/半径、轮廓含不受支持凹槽、P/Q块漏写、精加工进给继承错误。
6. Practice：Ø50→Ø42.4径向总去除3.8；按最大教学步深1.5至少3层，最后一层0.8，再算0.2径向精余量。

#### 21 · Grooving, Parting, and Internal Turning — K
1. Concept：外槽、端面槽、切断、镗孔的几何及工具参考点差别。
2. Why：刀宽、悬伸、孔底和卡爪间隙决定可达性；编程终点安全不代表刀体安全。
3. How：给出槽刀左刃/中心/右刃参考定义；分步切槽与退出；镗刀孔口/孔底包络；切断接近中心的转速限制和工艺审核。
4. Example：槽Z=-20至-24、宽4，刀宽3，以左侧（更接近Z0）刃为参考，则两刀参考Z=-20/-21覆盖全宽；外径40到槽底34，径向深3。第二例镗刀最小孔径要求假设为Ø18，现有Ø16孔不可直接进入，标为教学工具约束。图：槽刀刃参考尺寸图、镗杆/盲孔剖面。
5. Common Mistakes：槽中心和刀刃混用、镗杆未退出就X快速、把最小孔径按刀尖位置估算。
6. Practice：宽6槽用宽3刀覆盖时列出边界和重叠，不接受只答“走两刀”而不定义参考点。

#### 22 · Single-Point Thread Programming — K
1. Concept：螺距、导程、牙型、单头/多头、内外螺纹和旋向；不由公称直径直接猜最终小径。
2. Why：同步进给和退尾距离决定牙型，螺纹切削不是普通G01加相似进给。
3. How：先解释单刀同步螺纹，再选Haas G76完整参数解释；查牙型标准、刀片与量规资料确定深度/公差。不同控制器G76格式不混排。
4. Example：教学M20×1.5，单头导程1.5 mm/rev，500 rpm时理想同步轴向速度750 mm/min；有效螺纹长度20 mm，额外切入/退出长度须由工艺与控制器确定，不凭空规定。第二例双头pitch1.5的lead3.0、500 rpm时1500 mm/min。图：螺距/导程展开图、切入—有效牙—退尾区域。
5. Common Mistakes：把pitch当多头lead、把牙深经验公式当最终验收尺寸、切削时任意改倍率、无退刀槽。
6. Practice：单头2 mm、400 rpm得800 mm/min；指出需要查证的螺纹标准、公差级、刀片和循环参数，答案不捏造牙底直径。

#### 23 · Safe Program Start, Retraction, and Restart — K
1. Concept：先用非代码语言讲运动边界、工件固定、正确工具、坐标和预期动作；后讲已知初始状态。
2. Why：程序正确依赖机床状态；single block/feed hold不是安全隔离或完全防撞系统。
3. How：设置表→位置/夹具检查→模式建立→工具/偏置核对→受控接近；分开讲铣/车的启动和结束；G28中间点、G53、G49不得拼成万能“安全行”。重启先回溯状态，不从任意N号直接启动。
4. Example：夹具顶Z18，教学横移高度Z30，标出12 mm名义差值及刀柄限制；第二例中途重启缺H/G54/G90的状态缺口表，逐项补齐逻辑。图：三维包络简图与重启决策流程。
5. Common Mistakes：回参考点必然安全、G49随时可取消、靠倍率挽救碰撞、开门绕过联锁。
6. Practice：给含G91遗留和低Z横移的片段找至少三项风险；答案提供验证流程而非未知机床的一键启动行。

#### 24 · Program Verification and First-Article Checks — K
1. Concept：语法、几何、状态、材料去除、机床碰撞和首件尺寸是不同验证层。
2. Why：背绘正确不代表刀柄不碰；图形通过不等于实机证明。
3. How：代码审查→坐标/单位/偏置→已建模夹具/刀具仿真→按机床规程现场试运行→首件测量；记录仿真未覆盖项。dry run可能改变进给语义，抬Z可能破坏某些循环意图，必须按控制器规程。
4. Example：板孔设计(10,10)，实测(12,10)时查X偏置；另一孔直径目标10±0.05、实测10.08为超差0.03（相对上限），不能混淆为总误差。图：验证层级覆盖矩阵、首件测量点图。
5. Common Mistakes：只看无报警、仿真没有卡盘/刀柄、螺纹/攻丝随意改倍率、没有版本记录。
6. Practice：列一份至少10项验证表；给图形通过但夹具未建模的情况，结论必须是“尚未完成碰撞验证”。

#### 25 · Diagnosing CNC Program Problems — K
1. Concept：语法报警、几何不合法、状态错误、装夹/刀补错误、工艺问题分层诊断。
2. Why：只为消除报警而改参数会掩盖根因；先记录再复现，不在机床上试错碰运气。
3. How：保存原版本和报警原文→找最小片段→对照手册→独立计算→验证修改；区分所有特征同偏与单一特征错误。
4. Example：圆心(0,0)、起点(10,0)、终点(0,12)半径10与12不等，修正必须回到图纸；第二例四孔全偏X+2查基准/偏置，只有一孔偏查坐标。图：诊断树、孔位误差向量图。
5. Common Mistakes：放宽圆弧容差“修复”错误、用磨损偏置补全零件位置、未记录就改多个变量。
6. Practice：钻孔后发生意外再次下刀，检查G80及后续运动模式；要求按证据排查，不宣称任何多余孔都是同一原因。

#### 26 · Common Beginner Mistakes and Corrections — B
1. Concept：按单位、坐标、状态、偏置、几何、工艺六类理解错误。
2. Why：建立可重复检查习惯比背“危险代码名单”有效。
3. How：列15项具体误区，每项包括错误片段/现象、原因、修正与复查点；覆盖单位、G91、plane、IJK、G41/G42、H/D、G54、G80、R平面、G00、F模式、CSS上限、车床直径、控制器方言、跳行重启。
4. Example：错误G91 X30从X20到X50；修正后目标X30；另F0.2在每转/每分钟模式完全不同。图：错误意图与实际轨迹叠图。
5. Common Mistakes：以为本清单覆盖所有机床风险、只看代码不看装夹；引导到23/24。
6. Practice：六行片段标出至少四项缺失前提/错误，并按影响给出核查顺序；附完整解答。

#### 27 · Worked Project: A Stepped Shaft — K
1. Concept：从图纸到一套车削程序包；先修19–22、23–25。
2. Why：把单独车削动作接成受约束的完整流程，学会说明未在本装夹完成的面。
3. How：定义Ø40教学棒料、成品前端Z0、Ø30段Z0至-20、Ø36段-20至-40；后续夹持区位于Z≤-50，至少保留说明过的过渡空间。图纸明确本次只加工前端轮廓、不切断、不承诺最终总长。写装夹长度、刀具/刀鼻/偏置、粗精路径、检查尺寸、版本表。
4. Example：完整Haas车床训练程序逐段解析；粗至Ø30.4/36.4后精至30/36，径向留0.2；时间估算单列假设。第二变式把前段改Ø28，列需改的轮廓/余量/验证项目。图：尺寸化轴图与卡爪区域、粗精路径和刀塔避让图。
5. Common Mistakes：只改精轮廓不改余量检查、漏肩部刀鼻补偿、把车好前端当完整最终零件。
6. Practice：交完整程序、状态表、夹持图与检验表；教学直径公差±0.05，30.03合格、36.07不合格。公差是作业设计值，不称行业默认公差。

#### 28 · Worked Project: A Pocketed Mounting Plate — K
1. Concept：综合面铣/口袋/钻孔训练项目；先修33/17/18/16及23–25。
2. Why：几何、刀具选择、工序顺序和首件检验必须相互一致。
3. How：基准为已加工100×80×12板、左下角XY0、顶面Z0；口袋边界X30–70/Y25–55，40×30、深4、角R5；4×Ø6通孔在(10,10)/(90,10)/(90,70)/(10,70)。定义夹持接触区、垫块/牺牲板及钻尖下方空间。面铣作为前置工序说明，不在未更新Z0时偷偷追加去料。
4. Example：Ø10中心切削立铣刀的圆角矩形口袋刀心边界X35–65/Y30–50，说明粗加工需完整扫除内部而非只走一圈；Z分层-2/-4为教学值须核查刀具工况。Ø6、118°钻尖穿透12板几何需到约-13.803，取教学目标-14.5时说明额外0.697及背面间隙。完整多刀程序包含明确进刀、去料覆盖、退刀、G80和结束。图：尺寸化板图、口袋覆盖路径和钻孔剖面。
5. Common Mistakes：口袋只切边未清心、刀半径与角R冲突、通孔钻尖碰垫块、换刀后H不变。
6. Practice：口袋深度教学公差4.00±0.05，测3.92不合格；孔位按本作业独立坐标±0.10验收，不冒充GD&T位置度。交程序、工具表、包络核对和首件记录。

#### 29 · Subprograms and Repeated Features — K
1. Concept：主程序、子程序、调用、返回、重复次数及继承状态。
2. Why：相同几何可复用，但坐标/模态副作用也会重复。
3. How：用所选控制器M98/M99示例；明确程序编号、存储、重复语法；输入/输出状态作为契约；局部偏置/旋转是另一层功能，不默认调用自动平移。
4. Example：三工位X10/40/70，主程序定位，子程序执行同一已验证局部动作后返回；先展示重复写法，再展示调用。第二例每次G91 X5重复4次累计20 mm，返回后显式恢复约定模式。图：调用栈、三工位和累计位移图。
5. Common Mistakes：M30写在子程序、M99导致意外循环、G91泄漏、重复次数套用别的控制器格式。
6. Practice：起点X10，增量X5重复3次终点25；画返回路径并列调用前/后的状态契约。

#### 30 · CNC Programming Quick Reference — B
1. Concept：速查表是已理解知识的索引，不是免除上下文的命令清单。
2. Why：同一代码必须连同机型、单位、模态和取消方法一起查。
3. How：分“Mill motion/setup/cycles”和“Lathe motion/feed/cycles”；每行代码、用途、模态/取消、参数单位、前提、示例链接、来源。收录本课程实际使用的代码，不追求所有厂家大全。
4. Example：从“铣孔返回高度”查G98/G99，再用initial Z20/R3检验；从“车床每转进给”查模式，n1000、fn0.2得200 mm/min。图：由任务查代码的决策图。
5. Common Mistakes：把速查页当机器专属手册、忽略P/Q单位、脱离补偿状态看G00。
6. Practice：三个带条件的查表任务并返回课程链接；给出铣/车G98不能互换的解释。

#### 31 · Learning Path and Progress Checkpoints — B
1. Concept：按技能依赖学习，不按旧URL编号从小到大硬读。
2. Why：安全/坐标/状态不牢时直接读完整程序会变成背代码。
3. How：复述七模块、双应用分支、先修链；每课链接、3项能力目标；checkpoints用纸面自评，不靠账号或JS。
4. Example：给零基础读者每周3次×45min=135min的时间预算，仅作为学习安排示例，不承诺几周获得实操能力；一位只学铣削的读者从共享模块转模块4/28。图：带先修箭头的七模块路线SVG。
5. Common Mistakes：完成阅读当通过考核、跳过练习、依靠固定学习天数替代能力证据。
6. Practice：读者用39的评分规则识别短板，并选择回读路径；答错圆弧则回08/07/15，偏置错则回03/13/12。

#### 32 · From Engineering Drawing to Process Plan — K
1. Concept：毛坯、成品、基准、尺寸、公差、表面要求、装夹和工序；首次解释每个术语。
2. Why：G-code无法补救错误的加工顺序或不可达表面。
3. How：读视图→列特征→选基准→定装夹→选工具→粗精次序→检验；区分尺寸公差与位置度，不教授没有标准依据的GD&T规则。
4. Example：100×80×12板，孔距80×60，边距10；Ø6±0.05上下限5.95/6.05；将28的口袋/孔转成工序表。第二例图纸深4与工件Z-4的符号关系。图：带基准的板图、装夹与工艺流程。
5. Common Mistakes：读成比例量图、基准不一致、加工后失去夹持面、把设计公差当工艺能力。
6. Practice：实际孔6.06比上限多0.01，不合格；为先钻后开袋/先开袋后钻说明选择依据与需核验的支撑条件。

#### 33 · Facing, Slots, Pockets, and Contours — K
1. Concept：面铣、槽、开口/封闭口袋、外轮廓；径向/轴向切深和刀心路径。
2. Why：轮廓正确不代表毛坯全部去除；进刀方式由刀具切削能力和空间决定。
3. How：顺/逆铣原理与进给方向；覆盖、步距、分层、余量；直插/预钻/斜坡/螺旋的适用条件；不把任何坡角、步距百分比当全材料推荐。
4. Example：40×30、R5、深4口袋配Ø10刀，刀心可达范围30×20；假设层深2、横向步距4，列各层完整覆盖表和连线方式。第二例长60槽、Ø10刀、F200，单条直线理想18s，不含进退刀。图：轮廓与刀心包络、栅格去料覆盖剖面。
5. Common Mistakes：封闭口袋无合法入口、满槽套侧铣进给、缺清角、只走边界。
6. Practice：Ø12刀无法形成R5内角；要求选合适刀具或修改图纸，不能用“提高精度”解决几何限制。

#### 34 · Tapping and Thread Milling — K
1. Concept：攻丝与螺纹铣削；pitch/lead、底孔、有效牙深、工具端部额外长度。
2. Why：同步与几何不同，刚性攻丝能力不能由出现G84就推定。
3. How：G84按指定机床/选项核验；底孔和公差由标准与丝锥厂商数据确定；螺纹铣削区分单牙与多牙工具、刀心半径和每圈Z变化，区分刀心进给与接触点进给。
4. Example：单头M10×1.5、S500，在本例G94下同步F=750 mm/min；采用每转模式则按手册给1.5 mm/rev，不能混用。另简化几何：名义Ø20内螺纹、有效切削径Ø10单牙刀，名义刀心圆R5、每圈Z增加2（pitch2）；实际路径需查刀具有效直径/补偿，不能由公称尺寸确定最终配合。图：盲孔底余量剖面、螺旋升程与刀心圆。
5. Common Mistakes：随意变攻丝倍率、有效牙深=钻深、用减螺距经验值冒充底孔标准、把接触点F直接用于小刀心圆。
6. Practice：pitch1.25、S400得F500 mm/min；盲孔深20不自动允许有效牙长20，解释工具尖端和切屑余量。

#### 35 · CAD, CAM, and Post-Processor Verification — K
1. Concept：CAD几何、CAM工艺/刀路、post输出机床代码；三者不是同一个文件。
2. Why：CAM内仿真通过，错误后处理仍可输出不适合设备的代码。
3. How：导入单位→毛坯/夹具→WCS→刀具/刀柄→策略→仿真→匹配机器/控制器的post→独立审NC→版本和首件记录；不依赖某商业软件截图才能学习。
4. Example：同一100×80板误按inch导入变2540×2032 mm，用包络先发现；第二例CAM T02、post H07，依据设置表判断而不是强制号相等。图：CAD/CAM/post/NC的数据流、CAM路径与后处理状态核对矩阵。
5. Common Mistakes：拿相近机型post直接上机、漏刀柄/夹具、CAM自带仿真当实际NC仿真、改NC后不记版本。
6. Practice：审六项差异（单位、WCS、T/H、平面、feed mode、退刀），写变更记录及验证证据要求。

#### 36 · Variables, Logic, and Macro Foundations — K
1. Concept：变量、赋值、算术、条件、循环、局部/公共作用域；与普通子程序区分。
2. Why：重复几何可参数化，但错误参数会批量生成错误轨迹。
3. How：先纯计算伪代码，再给经手册核验的Haas宏选项示例；输入范围、循环上限、除零防护、保留变量范围；不写修改系统参数或偏置的未经验证程序。
4. Example：Xstart=10、pitch=20、count=4，生成10/30/50/70；第二例PCD40、4孔计算坐标(20,0)/(0,20)/(-20,0)/(0,-20)，介绍角度单位和精度。图：循环流程、变量逐轮追踪表。
5. Common Mistakes：未初始化、≤与<差一孔、count=0除零、把系统变量当普通变量、忽略前瞻求值特性（具体行为查手册）。
6. Practice：count=3输出10/30/50；输入count=-1或0应拒绝/按明确设计停止，附无机床运动的逻辑答案。

#### 37 · Rotary Axes, Multi-Axis Motion, and Probing — B
1. Concept：第四轴分度、3+2定位、同时五轴、TCP/RTCP、探测的功能边界。
2. Why：旋转改变刀具/工件姿态和包络；测头只是测量系统，不能自动证明装夹正确。
3. How：以旋转坐标几何解释分度，再讲枢轴、刀长、运动学和post匹配；探测流程为校准→接近→测量→验证，OEM循环语法不在本篇编造。
4. Example：在纯数学绕+Z正90°主动旋转定义下，点(20,0)到(0,20)，不等同于任意机床A/B/C实际命令。探测同一点读10.012/10.016/10.014，均值10.014、极差0.004，不由此宣布系统精度。图：旋转前后坐标、球头接触偏置示意。
5. Common Mistakes：把3+2叫同时五轴、忽略旋转扫掠、未校准测头、把极差当准确度。
6. Practice：同定义180°点(-20,0)；列实机还需机床运动学、枢轴位置、夹具包络和校准哪些数据。进一步链接仅指向确实存在的板块，不链接规划中的空页面。

#### 38 · Cycle Time, Quality, and Process Improvement — K
1. Concept：切削时间、非切削时间、换刀、检查、质量与稳定性；优化目标不是单纯提高F。
2. Why：缩短一次走刀可能增加废品、刀具成本或热漂移。
3. How：用L/F估算稳定直线段，再加入加减速、换刀/驻留等实测项目；一次改一项、记录样本、检验回归；从参数变化回算fz。
4. Example：L120、F300理想24s；F360变20s，节省4s（16.7%），但fz同步升20%，必须重新核查刀具负荷。第二例每件减少一次6s换刀、50件理论省300s，注明不含其他变化。图：时间构成条形图、进给/时间关系与尺寸趋势图。
5. Common Mistakes：理想时间等于实际周期、仅提速不验质量、把磨损趋势归零掩盖、从少量数据推断稳定过程能力。
6. Practice：200 mm、F400为30s；对25/24/27s三次数据平均25.333s，解释变差和缺失验证，不宣称统计能力达标。

#### 39 · Practice Projects and Final Assessment — K
1. Concept：用可审查的成果衡量能力；阅读完成与实机操作资质区分。
2. Why：综合题检验跨章节状态、几何、工艺的一致性。
3. How：20道基础题共40分（单位/坐标/数学/模态各5题），两份代码审查各10分，板件和阶梯轴方案各20分；总100分。80分及以上且所有关键安全/几何错误已修正才通过纸面课程。
4. Example：提供一题完整示范：G17，S(0,0)/C(0,20)/E(20,20)短弧应G03；含步骤、图、评分点。两综合项目使用27/28的完整数据，给空白设置表、提交要求、标准答案和可接受替代策略。图：评分能力矩阵、项目尺寸图或同数据重绘。
5. Common Mistakes：只提交代码、没有夹持条件/单位/方言、答案通过但不能解释状态。关键失败项：单位/坐标错误导致撞击、未限定CSS导致超速风险、退刀穿夹具、把未验证程序宣称可直接运行。
6. Practice：所有题提供原生details答案；数字结果与本SPEC一致。评分细则区分几何、状态、工艺、验证；未达标按错误类型回链课程，不用“多练习”敷衍。

#### 40 · CNC Programming Glossary and Source Guide — B
1. Concept：建立40–60条入门术语的英文解释，含datum、offset、modal、interpolation、chip load、pitch/lead、post、backplot。
2. Why：同一缩写或字母在不同机型/循环意义可能不同，需要查看上下文。
3. How：每词给普通英语定义、单位/适用场景、数字微例、对应课程链接；来源区按数学/公式、控制器、刀具推荐、尺寸标准分类。
4. Example：pitch1.5、双头lead3.0；Ø10的R5；n2000、4齿、F240反算fz0.03。图：坐标/偏置/几何/工艺术语关系图。
5. Common Mistakes：论坛数值当厂家参数、未注明版本的截图当标准、混淆教学公差和标准公差。
6. Practice：给五条未经核实的陈述，要求找对应一手资料种类；答案演示如何记录标题、版本、章节、检索日期和适用条件。

## 设计要求

### 参考布局与严格约束

参考现有板块首页布局：[CNC Programming](https://lilu1626.github.io/cnc-manufacturing-engineering/cnc-programming/)。文章结构参考现有[入门页](https://lilu1626.github.io/cnc-manufacturing-engineering/cnc-programming/01-getting-started/what-is-cnc-programming/)，只继承信息层级和配色，不继承缺漏SEO、相对路径、技术错误与不完整章节。

- 变量原样使用：`--ink:#17242f`、`--muted:#5c6872`、`--surface:#ffffff`、`--accent:#0b766e`、`--accent-dark:#07574f`、`--accent-light:#e6f4f2`、`--border:#cfdbd8`、`--radius:18px`。图形同样使用此色板，用实虚线、编号和文字区分，不依赖新增红色表达风险。
- 字体 Inter, system-ui, sans-serif，正文/列表行高1.6。首页内容宽度 `min(100% - 32px, 1080px)`，文章 `.article` 宽度 `min(100% - 32px, 780px)`。局部覆盖现有article.css行高，不能改其他板块。
- 每页加载绝对路径 `/cnc-manufacturing-engineering/assets/css/site.css`；文章再加载 `article.css`；最后加载本板块 `cnc-programming.css`。全站样式原文件不改。
- 导航完整保留 PROJECT_CONTEXT 的六项及次序：Home、Engineering Tools、Knowledge Base、Machine Systems、CNC Programming、About；品牌文字 Li Lu · CNC Eng。全部站内href/src采用 `/cnc-manufacturing-engineering/...`（页内锚点可用#）；当前板块加 `aria-current="page"` 的语义需准确，文章页可用导航高亮class但不把首页冒充当前页。
- 所有40个课程/服务页左上角回 `/cnc-manufacturing-engineering/cnc-programming/`，文本精确为 `← Back to CNC Programming`。本方案不建立章首页，01虽深一层也回板块首页；不得套用知识库“返回01章”的例子。首页可回Home。
- 正文 `main.article`、唯一h1、`p.lead`；复用 `.hero-eyebrow`、`.callout`、`.example`、`.formula-box`、`.nav-links`。警示采用 `.callout`加局部 `.cp-safety-note`，不沿用现有额外红色；标题写明限制/条件。
- 首页复用 `.page/.hero/.tool-cat/.tool-list/.tool-item`；只在局部样式中添加 `.cp-meta/.cp-toc/.cp-table-scroll/.cp-code/.cp-figure/.cp-practice/.cp-safety-note`。不引入框架、外部JS、网络字体依赖或全新设计体系。
- 页脚精确：`Designed by Li Lu · CNC &amp; Manufacturing Engineering`。

### 示意图与可访问性

图中必须标单位、轴正方向、工件/刀具/夹具、关键尺寸、运动箭头；圆弧注明观察方向；SVG用viewBox自适应、title/desc及可访问名称。数学坐标Y向上与SVG屏幕Y向下转换必须复核，不能只凭箭头看起来顺眼。

每张图有英文caption说明其用途与简化边界。不要把不按比例绘制的图用于测尺寸；标 “Schematic, not to scale”。示意图采用内联SVG，可读ASCII仅用于简单状态/流程；关键零件与路径图必须SVG。

代码和宽表在局部容器横向滚动，不导致整个页面横向溢出；表格有caption和th scope，滚动容器有可访问名称及可键盘操作方式。移动端不缩小文字硬塞；上下课导航换行。答案用原生details并标明确summary；不靠悬停访问关键解释。链接有可见焦点，SVG颜色之外还用虚线/标号识别。

### SEO、链接与旧路径兼容

每页 `<html lang="en">`、charset、viewport、唯一title、唯一description、唯一canonical。title统一为 `{英文页面标题} — CNC & Manufacturing Engineering`；description用不超过150个英文字符的独立概述，禁止复制成同一句。

canonical为 `https://lilu1626.github.io/cnc-manufacturing-engineering/` 加页面目录路径并以 `/` 结尾，不含index.html，不带锚点；例如01 canonical保留两层目录。全部41个canonical进入sitemap且每个恰好一次。旧23个URL仍是内容页，不做无必要改名/跳转。

正文相关工具链接可选：
- `/cnc-manufacturing-engineering/engineering-tools/spindle-speed-calculator/`
- `/cnc-manufacturing-engineering/engineering-tools/feed-rate-calculator/`
- `/cnc-manufacturing-engineering/engineering-tools/hole-pattern-generator/`
- `/cnc-manufacturing-engineering/engineering-tools/arc-and-chord-calculator/`
- `/cnc-manufacturing-engineering/engineering-tools/printable-setup-worksheet/`
- `/cnc-manufacturing-engineering/engineering-tools/machining-time-estimator/`

上述目录在现仓库存在；实施时再次检查。不得链接尚未建立的专业板块或声称相关计算器输出已代替人工回算。

### 技术来源与查证规则

2026-09-24 已检索的一手起点：

1. [Haas Mill Operator’s Manual — G-Codes](https://www.haascnc.com/service/online-operator-s-manuals/mill-operator-s-manual/mill---g-codes.html)：铣床代码语义与各条目入口。用于核对圆弧、补偿、循环与返回高度；实施时逐个打开实际用到的代码条目，并记录对应设置/选项，不只引用总目录。
2. [Haas Lathe Operator’s Manual — G-Codes](https://www.haascnc.com/service/online-operator-s-manuals/lathe-operator-s-manual/lathe---g-codes.html)：车床代码与循环入口；G98/G99在车床是进给模式，不能复用铣床返回平面说明。G71/G76等须依据具体条目确认参数。
3. [Sandvik Coromant — Formulas and Definitions for Milling, Metric](https://cdn.sandvik.coromant.com/files/sitecollectiondocuments/services/metal-cutting-e-learning/formulas-and-definitions/formulas-and-deinitions-for-milling-metric-enu.pdf)：切削速度、转速和进给公式的一手公式表。它不是为本文教学工件提供的刀具推荐参数表。
4. [Haas Mill Programming Workbook](https://www.haascnc.com/content/dam/haascnc/en/service/reference/programming-workbooks/mill---programming-workbook.pdf) 与 [Lathe Programming Workbook](https://www.haascnc.com/content/dam/haascnc/en/service/reference/programming-workbooks/lathe---programming-workbook.pdf)：补充教材入口；与当前操作手册有冲突时需查当前机型版本，不能由旧教材推定新机行为。

下一阶段必须补查：所用Haas M-code、宏选项与机器操作/安全章节；所有实际推荐的刀具数据；螺纹牙型/公差适用标准（例如具体版本的ISO公制螺纹相关标准或相应英制标准）；FANUC/SINUMERIK若提供具体语法必须找到对应型号一手手册。未查证项可讲原理并清楚标记范围，不允许在最终文章中留下“待补来源”的关键数值。

每项工程主张区分：**数学计算**（列式可回算）、**教学设定**（尺寸/公差/参数假设）、**控制器行为**（引用机型手册）、**真实工艺推荐/标准限值**（引用对应手册/标准）。不引用搜索摘要作为代码参数证据。文章为原创讲解/原创例题，不复制长段厂商教材。

## 验收标准（实施完成后逐项核验）

### 交付和结构

- [ ] 清单41个HTML文件全部存在；23个旧页面保留原URL，新增恰好18页；无孤立文章、空卡片、占位图、“Coming soon”或未填程序。
- [ ] 每页英文标题对应清单；首页和31课程顺序一致，七模块与双分支明确；23有前置基础段与后置复习入口。
- [ ] 每篇都有先修、目标、lead、统一六段、至少三题及详细答案、来源与适用范围；B/K词数符合要求。
- [ ] 全部内部页面/目录锚点/上下课/返回/工具链接可解析；旧首页七个ch锚点继续有效，01深目录链接单独检查。
- [ ] 首页覆盖其余40页；Reference页不会错误进入机械的数字顺序；所有文章可从首页两次点击内到达。

### 工程准确性与新手可学性

- [ ] 首次出现术语都解释，所有物理量带单位；算术例题有已知量、过程、结果和回验；不是用代码表代替解释。
- [ ] 所有K页至少两个实际图和两个例题（或完整项目+变式），B页至少一个图和一个数字例题；图/文字/代码/答案一致。
- [ ] 圆弧关键回归：S(0,0)、C(0,20)、E(20,20)的G03为90°、31.416mm；G02为270°、94.248mm；SVG观察方向正确，起终半径均20mm。
- [ ] 速度回归：2000×4×0.03=240mm/min；pitch1.5×500=750mm/min；CSS的D50/D25分别约955/1910rpm，教学上限1800时限制生效。
- [ ] 坐标回归：(-300,-200)+(40,30)=(-260,-170)；刀长例的几何符号定义完整，不再出现无条件“机器位置+偏置=刀尖”的口号。
- [ ] 车床直径/半径量、G98/G99及G90的语境逐段检查；刀尖方向、G71/G76参数、G84选项、P/Q量纲均能追溯至适用手册。
- [ ] 各完整训练程序无省略号/关键占位；有工具表、寄存器、机型、单位、初始状态、夹持边界、退刀、结束和行状态表。程序与选定控制器语法一致；不把片段当可直接运行程序。
- [ ] 教学数据与真实推荐数据显式分开；没有无来源的材料速度表、经验公差、螺纹底径或通用安全高度。
- [ ] 27/28项目尺寸彼此不冲突；口袋内部有去料覆盖，Ø10与R5关系正确；钻尖突破/背面空间经计算；车削前端项目不谎称完成切断与总长。
- [ ] 练习答案独立回算；综合评分100分构成正确、80分门槛与关键错误修正要求清晰。
- [ ] 旧页面已识别问题（圆弧方向、G49绝对化、无定义偏置公式、G84泛化、仿真保证论）全部移除并替换为条件明确的解释。

### 设计、访问性和SEO

- [ ] 色板、Inter/system-ui字体、1.6行高、1080/780容器、18px主圆角符合PROJECT_CONTEXT；局部CSS不污染其他板块。
- [ ] 每页全局六项导航、文章返回按钮和固定页脚正确；站内资源/跨页链接使用带仓库前缀绝对路径。
- [ ] 41页title/description/canonical完整且唯一；description≤150英文字符；sitemap全量保留其他模块URL，并覆盖41页且无重复。
- [ ] 360px、390px、768px、1440px视口检查：首页、01深目录、15圆弧、28完整项目、30大表、39答案页；整页无横向滚动，代码/表格可局部滚动，SVG标签可读。
- [ ] 键盘能访问导航/目录/答案，焦点可见；无单靠颜色表达；表头/图标题/替代说明完整；200%文字缩放无内容丢失。
- [ ] 本地按 `/cnc-manufacturing-engineering/` 子路径预览，不能只在根路径预览；无缺CSS或资源404。

### 验证证据与实施顺序

- [ ] 实施交付记录包含文件增改清单、旧URL核对、页面词数/章节/SEO/图/练习检查表及移动端截图。
- [ ] 对数值和几何进行独立计算；用适用控制器仿真/背绘检查完整项目，并记录工具、版本、所覆盖和未覆盖的机床/夹具模型。若没有适用仿真环境，明确该项未验收，不以通用HTML检查代替程序验证。
- [ ] 不声称执行过实机试切。现场操作与首件验证由有资格人员依实际机床规程完成；网页方案的验收和机床放行是两个范围。

建议实施批次：先做公共页面骨架与01/03/15三篇样板；然后模块1–3；再铣削/车削应用及两项目；最后CAM/进阶/评估/速查；所有页完成后一次核对导航、SEO、sitemap和跨页数据。分批实施不削减41页最终范围。

## 注意事项 / 开放问题

1. 当前采用Haas可查证语法作为教学基准是本方案的明确实施选择，不把待选控制器变成阻塞。若后续指定实际FANUC/Siemens机床，需对相关实例另做方言审查，不做字符串替换。
2. “完整学习路线”指基础与应用闭环；高级五轴运动学、全套宏库和OEM探测循环属于后续专业模块，本期必须提供37/36的真实入门内容而非空链接。
3. 本阶段只编写SPEC。网页实现、git提交、推送、部署不属于这次用户授权的交付内容。
4. 范围内保留旧URL，目录编号不重排；无需用户决定大规模迁移。未来如要新增章首页，应另列路径、返回规则和迁移验收，不在实施中临时改变。
5. 如缺少某项专有手册/标准，不得臆造精确参数或把未验证内容包装为通用规则；用已核实主线完成课程，其余明确适用范围并在实施报告中记录。
