# Review — CNC Programming v2

日期：2026-09-24  
审阅提交：`c59e665`；对比基线：`80051d9`。  
依据：原始SPEC及上一轮R01–R14反馈。  
**结论：不通过。部分原问题修正，但仍有工程错误，且新增URL/课程覆盖退化；不能只安排扩写和补图。**

本轮读取v2完成报告和实际diff，全量检查本地42个HTML的路径、链接、canonical/sitemap及内容统计，重点复核上轮涉及的程序与解释。查阅Haas官方代码资料并独立回算几何。未执行生成器、修改网页、提交/推送；未运行控制器仿真或实机，也未完成浏览器多视口验收。以下是源文件审阅结论，不是机床运行认证。

## 先纠正完成报告的交付口径

- 实际为 **42个HTML = 首页 + 41个内容页**；首页只有 **38个课程/服务页入口**，不是完整的40篇路线。
- 原SPEC的41个路径中 **14个被删除**；新增了 **15个非SPEC路径**。旧路径保留是硬性要求，不应自行重命名。
- sitemap未随v2改动：仍指向14个已不存在的页面，同时漏掉15个新canonical。
- 三个旧页面仍留在目录但不在新首页中：`38-process-optimization/`、`39-exercises-assessment/`、`40-glossary-sources/`。旧39页仍保留上一轮已指出的错误G80答案。
- 首页可达38篇，英文词近似数175–831，37篇不足800；唯一超过800的23页是K类，仍不足2000。它们远不只是“部分500–800词”。统计不计代码/SVG/nav，但包括目标、答案与来源，对正文仍偏宽松；数字不计作英文词，最终词数验收应另用统一口径。
- 现存SVG在01、02、15三个页面，不是“只有15页”；但仍远低于逐页配图要求。
- 实际HTML中没有可点击的外部来源链接；“haascnc.com, retrieved ...”是普通文本，不是指向适用章节的证据。多个工具链接仍是写进HTML的Markdown文字。

## 上轮R01–R14回归状态

| 上轮项 | 本轮状态 | 依据/后续 |
|---|---|---|
| R01 重启 | 部分修正，不能关闭 | 23已反对跳行，但lead又宣称从头运行即安全；见V08 |
| R02 铣削项目 | 未解决 | 坐标名义尺寸修正，实际刀路仍错误；见V02 |
| R03 方言/螺纹 | 部分修正，不能关闭 | Haas G99已引入，但G76 K/D含义与参数仍错；见V04 |
| R04 刀长 | 未解决且文本退化 | 同页同时讲深/浅、保留“Wait/let me redo”与错误算式；见V01 |
| R05 验证 | 部分修正，不能关闭 | 已否定抬高空跑证明碰撞，但仍给普适倍率/证明论；见V08 |
| R06 车削项目 | 两个指定缺陷已修 | P/Q内Z不再反向，删去切断；缺面加工、设置完整性仍需修；见V09 |
| R07 子程序 | 未解决 | 有换行动作，但调用语法错且首孔重复；见V03 |
| R08 宏跳转 | 代码中的N标签已修，整页未通过 | 输入校验改进；讲解仍错误、未检查整数；见V10 |
| R09 圆弧图 | 圆心几何修正，教学仍未通过 | SVG Y向下未转换，新增练习方向错；见V05 |
| R10 循环取消 | 新考核局部修正，旧错误仍发布 | 老39残留错误，新33相互矛盾；见V06 |
| R11 探测 | G31与写偏置分开了，仍未通过 | 中心零点公式符号错，坐标基准缺失；见V07 |
| R12 深度/图/练习 | 未完成 | 字数、图数、来源及课程主题缺失；见V12 |
| R13 路线/兼容 | 退化 | 改路径、七模块缩水、sitemap失配；见V11 |
| R14 模板/访问性 | 部分修正 | 新页body/main修正；行高/返回类/源码文字等仍未落实；见V13 |

## 必须修复的发现

### V01 [P1] 刀长页公开了互相矛盾的推导，并把G49误写成机器坐标切换

位置：`docs/cnc-programming/12-tool-offsets/index.html:32–36`、`:39–41`。

How先说实际刀长120而存100会高20、切浅；下一段又说切深。Example写`10 - (-400) - 100 = -290`，左侧实际为310。页面还保留“Wait — recheck”“No — let's be precise”“Let me redo”等未完成草稿。标题/最后一句正确不能抵消中间错误推导。另将G49解释为后续Z转为机器坐标；G49仅取消刀长补偿，不取消活动工件坐标系，不等于G53。

统一用一套定义即可：W=工件原点机器Z，P=编程刀尖工件Z，H=存储正刀长，L=实际正刀长，M=主轴基准面机器Z。简化未旋转模型：`M=W+P+H`；实际刀尖工件Z=`M-L-W=P+H-L`。W=-400、P=10、H=100，则M=-290；L=102时实际刀尖为8，比目标低2mm。P=-10时实际为-12，切深2mm。

修复：整段重写，只保留经回算的几何链和尺寸图；明确显示值/测量约定，不泛化为所有机型内部实现。按[Haas G49](https://www.haascnc.com/service/codes-settings.type=gcode.machine=mill.value=G49.html)更正作用域。练习解答同源校验。

复验：H/L分别大/小2mm都能回算；G54活动时执行G49，说明G54仍活动；页面无自我纠错草稿和等式计算错误。

### V02 [P1] 铣削项目仍不能加工所述口袋，且混淆D寄存器与半径

位置：`docs/cnc-programming/28-milling-project/index.html:41–59`、`:74`；关联`20-milling-programming/`。

- Ø63面铣刀沿Y40只走一条线，覆盖约Y8.5–71.5，未覆盖板宽Y0–80；起点X-20时刀具也已部分搭在板上，不能当作刀具整体在外。
- Ø10刀直接在X30/Y25角点下到Z-4，刀刃会越过指定口袋边界；这不是合法的内部清料入口。
- X35–65/Y30–50本来已是Ø10刀对应的刀心边界，却又启用G41 D05，重复补偿。D05是寄存器编号，不能仅凭“05”认定补偿半径=5。
- 即使去掉补偿只走这个矩形一圈，中间仍留料；没有完整扫除口袋的刀路，更没有约定分层。
- “complete, runnable-style”与缺少D寄存器值、刀具进刀能力、工况、夹具/背面间隙证据不符。

修复：按SPEC28的已加工顶面前提去掉未定义的面铣，或者单独完整设计基准更新；采用明确的刀心编程或轮廓补偿方案之一，给完整入口/分层/覆盖/清角/退出和刀具表。禁止用“coordinates match drawing”替代材料去除验证。

复验：回绘刀心及刀具扫掠面，口袋边界X30–70/Y25–55、角R5、深4正确，内部无残料，进刀不越界；D寄存器含义和值可审查。钻尖角、突破余量和背面空间也须明确，不能把四舍五入后的-13.8视为充分工艺保证。

### V03 [P1] 子程序调用格式错误，修正后仍会每行重复钻首孔

位置：`docs/cnc-programming/34-subprograms/index.html:40`、`:47–54`。

`M98 O2000 L3`应按Haas格式使用P指定子程序号，O是程序标识。[Haas M98](https://www.haascnc.com/service/codes-settings.type=mcode.machine=mill.value=M98.html)规定`M98 Pnnnn`。

即使修正调用，在已定位X10/Y10后，`G90 G81 Z-10 R2 F100`就会在当前XY执行第一孔；下一行X10又调用一次循环，再X30/X50/X70。因此每行5次循环、三行15次，只有12个唯一位置。Haas官方G81示例明确首条无XY的G81在当前位置钻孔：[Haas G81](https://www.haascnc.com/service/codes-settings.type=gcode.machine=mill.value=G81.html)。换行前还需核对返回高度，而非默认R2能横移。

修复：修P调用；把首孔明确写在循环启用块，并移除重复的X10；指定G17、进给模式、返回平面和换行间隙。给出入口/出口状态及逐次展开表。

复验：恰好12次孔循环，分别对应X10/30/50/70与Y10/30/50；不是仅有12个唯一点就算通过。三次调用结束的XY/Z和模态已知。

### V04 [P1] G76把K和D当作可互换参数，且示例漏D

位置：`docs/cnc-programming/22-lathe-threading/index.html:23–38`。

lead/目标/正文写“K(or D)=thread depth”，两个例子只有K没有D。Haas官方定义K为牙高（径向总深），D为首刀切深，它们不是同义词；官方参数表把D列为非可选地址。[Haas G76](https://www.haascnc.com/service/codes-settings.type=gcode.machine=lathe.value=G76.html)。M10例X8.2和K0.92又不是对Ø10简单径向尺寸链一致的组合：10−2×0.92=8.16。

修复：逐项讲K、D、F、X、Z及影响终刀/退尾的设置，补完整受支持格式或明确是片段。最终螺纹尺寸按适用标准/刀片、公差核定，近似牙深只能用于原理计算。不能以“把双行变单行”声称方言已验证。

复验：K/D职责和单位分开，关键参数齐全；程序、几何推导与目标尺寸一致，有具体官方条目引用。

### V05 [P2] 圆弧新增练习把90°顺时针判成逆时针

位置：`docs/cnc-programming/15-circular-interpolation/index.html:52`；图形`:35–45`。

练习S(0,0)、C(30,0)、E(30,30)，相对圆心向量为(-30,0)→(0,30)。从+Z看，短弧是顺时针90°，应G02；当前答案G03会走逆时针270°，与47.1mm弧长不符。正确短弧片段是`G02 X30 Y30 I30 J0`（前提G17及已知起点/圆心模式）。

主例SVG的几何圆心这次确实选对了，不应再沿用上一轮“圆心错”的结论；但屏幕Y向下未转换为工程图Y向上，视觉呈顺时针，且无轴方向/观察方向，C标签x=-14超出viewBox左界-10。

修复：改练习及解析，按工程坐标变换绘图并标方向、尺寸与箭头；另画长短弧对照。扩viewBox防止标签裁切。

复验：主例与练习均独立用向量角度验算；不能只机械替换所有G02为G03。

### V06 [P2] 固定循环纠错未全站统一，旧错误仍可访问

位置：新`33-drilling-cycles/index.html:41–44`；旧`39-exercises-assessment/index.html:40`；新`39-assessment/index.html:48–49`。

新33仍称“next rapid move drills”，同时练习只写`X0 Y0`却用“G00 cancels”作答案。仅XY和显式G00是不同情况。旧39没有删/改，仍断言显式G00会继续钻孔，并留在sitemap。新39的G00解释已局部修正，但审码题忽略刀尖仍在Z-2时快速横移的实际问题；另一题答案假定G90，题目却未声明初始距离模式。

修复：按[Haas G80](https://www.haascnc.com/service/codes-settings.type=gcode.machine=mill.value=G80.html)统一“仅XY延续循环，显式G00/G01取消”的指定机型行为。恢复原39路径作为唯一已更新考核入口，清除重复陈旧版本。审码要列模式和位置前提，识别低Z快速穿料风险。

复验：同一初始循环状态下分别推演XY、G00 XY、G80三例；所有可访问页面和答案一致。

### V07 [P1] 探测页中心零点公式符号反了，坐标基准也未声明

位置：`docs/cnc-programming/37-probing/index.html:32`。

从左侧接近，触球中心X=-100、球径4，左边缘=-98的算术在同一坐标基准下正确；但“center G54 X = -98 - half-width”把中心放到左边缘更左。宽40时，几何中心应为-98+20=-78，而不是-118。还没有区分#5061的记录坐标与机器坐标，不能直接把数值塞进G54寄存器。

修复：先定义触点记录所用坐标系、探针标定和测量方向；左边缘到零件中心为加半宽。再按机型偏置定义解释转换，不直接把测量数当偏置。练习中“tip radius 2 to the left”也需改成球中心在边缘左侧、接触点在中心右侧，避免文字反向。

复验：给已知机器/工件变换的宽40算例，中心位置与左右边缘平均一致；继续保留“G31记录≠自动更新G54”的正确区分。

### V08 [P1] 安全与验证仍保留绝对保证和统一倍率

位置：`23-program-safety/index.html:23`、`:56–58`；`24-program-verification/index.html:27–40`。

23首句仍说“从头运行的程序是安全的”，和后文“不总是安全”自相矛盾。24虽已说明抬高空跑不能证明碰撞，却称只有控制器仿真或手算“proves clearance”，同时指定50%快速、100%单段、25–50%首切，没有区分攻丝/螺纹等同步操作，也未说明模型/状态不确定性。不能从一次空跑泛化“XY一定正确”。

修复：删除无条件保证；已知状态、几何模型、夹具、刀具和控制器规程共同决定验证范围。倍率和试运行方式由机型/工序规定，不给通用百分比处方；正文按SPEC要求说明已验证和未覆盖项。

复验：从程序头/中途两种入口都列前提；不再出现“从头就安全”“单一层证明全部”“所有工序统一倍率”的结论。

### V09 [P2] 车削原先两项错误虽已修，完整项目仍缺前提

位置：`27-turning-project/index.html:27–55`及`19-turning-programming/`对应程序。

认可：P/Q内Z单调、明确不切断，上一轮这两项已修。剩余问题：正文说“Face it”，代码却没有单独覆盖Ø40端面的面加工；起始只写G21/G97/G99，没有建立G18等所依赖状态或说明片段前提；两刀与夹具、卡爪边界、几何/鼻圆偏置仍无设置图/表。不能称已完成从原始棒料到所述基准端面的全过程。

修复：明确端面已预加工的前提，或补经核验的面加工；声明控制器初始状态及所有设置值、夹持区域、退出包络。代码与文字所称工序一致。

复验：依据尺寸图逐步解释每个工序何时完成；没有未声明继承的关键状态，不把普通片段标完整项目。

### V10 [P2] 宏代码N标签已修，但讲解仍错且输入校验不完整

位置：`36-macro-programming/index.html:27–29`、`:38–46`。

`GOTO 100`与N100这次匹配，值得保留。可正文又说“GOTO N100 is correct”，并把旧`GOTO1000`解释成会跳O1000；正确解释是GOTO数值指向N标签，旧例是缺N1000，不是它真的调用了O程序。count只限制3–12，没有整数校验：N=3.5会执行4次、角度步长102.857°，不是等分3.5孔的合法阵列。片段含实际G81运动，却没明确所有前置机床状态。

修复：统一标签语法与原理，校验正整数及上限；按SPEC先提供无运动的数学追踪，再提供适用机型片段及状态合同，核查表达式语法/变量范围。

复验：4孔结果正确；0、负数、3.5均按规定拒绝；合法循环执行次数与输入整数一致。叙述与代码不再彼此冲突。

### V11 [P1] 擅自更换路径与课程主题，破坏SPEC和sitemap

位置：`docs/cnc-programming/index.html`、`31-learning-path/index.html`、`docs/sitemap.xml`、被删除的14页。

旧URL保留原样是明确要求。现在旧10/17/24等被删，sitemap仍引用它们；新增页面未收录。首页从七模块改五级，31又只有四级且没有逐课链接，遗漏32等步骤；主题也不是简单改名：原CAD/CAM/post页变成“Practical Examples”，槽/切断/镗孔页被螺纹基础替代，完整铣削策略/攻丝与螺纹铣削、多轴概览等失去规定内容。旧38优化成孤立页，其上一页链接到已删除37；旧39/40重复内容仍存。

修复：恢复原SPEC的41个目标路径和七模块/服务页结构，在这些稳定路径里更新内容；将有用的新文字合并回正确课程，避免另建同号不同主题。sitemap与最终目录一致，所有旧23入口继续可达。修复首页/31/Next同序与七个旧ch锚点。不将错误的内容迁移用重定向掩盖为课程完成。

复验：SPEC路径集与交付集一致；sitemap无指向缺文件URL、无缺canonical；首页覆盖全部40篇；Next链和31一致；旧23入口及七锚点均有效；没有陈旧考核页旁路。

### V12 [P1] 已知深度/图片不足之外，考核与来源仍未交付

位置：全量；重点`39-assessment/index.html:26–54`、`40-glossary/index.html`、`38-controller-specific/index.html`。

报告已承认字数/图数不足，但真实范围更大：现存41篇中40篇不足800；重点篇最高831，均远低于2000。首页38篇中的35篇无SVG。练习大多只有2题，先修、状态表、独立数值变式不齐。考核新增20题与分数组成，但两份项目只是模糊提案，缺SPEC两项目完整数据与评分细则、标准答案、关键安全错误否决条件；唯一details答案为空。

控制器页不只是简略：它仍把FANUC进给模式按品牌一概而论，练习称Haas车床G98/G99同时控制“retract and feed mode”，混回铣床返回平面语义。来源只有泛称手册，无法核查型号版本。

修复：逐篇按原SPEC的内容合同补实质讲解、例题/数字回算、图与三题解析，不按新编号自行缩减主题。考核沿用27/28的项目和可评分答案；控制器差异按机型/系统版本查证，不再给品牌级万能表。所有真实参数与代码行为旁提供具体来源链接，教学假设明确标示。

复验：交40行验收矩阵，包含词数、图、题、先修、来源、完整项目状态及证据。最低词数只是必要条件，不能保留错误推导或“Wait/recheck”来凑字数。

### V13 [P2] 模板改动只完成一部分，页面仍暴露交接历史和原始标记

位置：新页面通用模板、`docs/assets/css/cnc-programming.css`；`24-program-verification/index.html:44`、`27-turning-project/index.html:58`。

body.cnc-programming、main.article与active导航已改正确。但article.css的p/li行高1.75仍生效，现cp样式只对cp-article设1.6，body行高被更具体规则覆盖；返回链接改为未定义的cp-back而不是规定back-link；首页使用780px article而非1080px首页容器；title缺品牌后缀，首页课程链接为相对路径，旧锚点缺失。两个页面有裸`li>`文字；多数“[工具名](路径)”直接输出在HTML中，不会生成a链接。

学生正文还出现“R04 critical”“R06 previous version”“SPEC says”等交接语言，并把返修过程当Concept/Why，违背面向零基础教学。删去这些背景，写最终知识，不把review历史展示给学习者。

修复：恢复设计规范的类/作用域覆盖，补实际HTML链接、语义图表、正确列表；清理内部修订痕迹。实施后做360/390/768/1440与键盘/200%缩放检查，不能因为DOM类名改对就勾选可视验收。

复验：计算样式符合1.6行高和容器要求；页面不存在裸Markdown、li>或R编号；图有标题/说明，来源可点击；提供规定视口测试证据。

## 建议下一轮顺序

1. 先修V01–V08的错误知识和程序，不把这些草稿扩充到2000词。
2. 按V11恢复稳定目录/课程范围，清理陈旧旁路页面并同步sitemap。
3. 完成V09/V10程序前提与逐行验证，再补V12全部教学深度和考核。
4. 修V13模板和显示，提供逐页验收矩阵、控制器语法/刀路验证及多视口证据。

下一份完成报告应按本轮V01–V13逐项给出修改位置和证据，并准确区分“某一错误已修”与“该篇整体验收通过”。本轮认可的局部修正不等于R01–R14全部完成。未进行的仿真/实机验证应明确保留，不写成已通过。

## 附录A：缺失的原SPEC路径

- `docs/cnc-programming/10-spindle-feed/index.html`
- `docs/cnc-programming/11-controller-dialects/index.html`
- `docs/cnc-programming/17-drilling-cycles/index.html`
- `docs/cnc-programming/19-turning-fundamentals/index.html`
- `docs/cnc-programming/20-turning-cycles/index.html`
- `docs/cnc-programming/21-grooving-parting-boring/index.html`
- `docs/cnc-programming/22-threading/index.html`
- `docs/cnc-programming/24-verification/index.html`
- `docs/cnc-programming/29-subprograms/index.html`
- `docs/cnc-programming/33-milling-strategies/index.html`
- `docs/cnc-programming/34-tapping-thread-milling/index.html`
- `docs/cnc-programming/35-cad-cam-postprocessing/index.html`
- `docs/cnc-programming/36-macro-foundations/index.html`
- `docs/cnc-programming/37-multiaxis-probing-overview/index.html`

## 附录B：现存页面静态统计

词数按main中英文单词近似提取，排除pre/svg/nav，但包含目标、答案和来源；仅作为缺口定位。details数量不保证答案非空。

| 页面目录 | 英文词近似数 | SVG数 | details数 |
|---|---:|---:|---:|
| `01-getting-started/what-is-cnc-programming` | 786 | 1 | 3 |
| `02-machine-fundamentals` | 623 | 1 | 2 |
| `03-coordinate-systems` | 417 | 0 | 3 |
| `04-program-structure` | 304 | 0 | 2 |
| `05-gcode-fundamentals` | 327 | 0 | 2 |
| `06-modal-codes` | 299 | 0 | 2 |
| `07-plane-units` | 313 | 0 | 2 |
| `08-programming-math` | 401 | 0 | 3 |
| `09-mcode-fundamentals` | 292 | 0 | 2 |
| `10-spindle-programming` | 315 | 0 | 2 |
| `11-feed-programming` | 322 | 0 | 2 |
| `12-tool-offsets` | 664 | 0 | 2 |
| `13-work-offsets` | 363 | 0 | 2 |
| `14-linear-interpolation` | 239 | 0 | 2 |
| `15-circular-interpolation` | 287 | 1 | 2 |
| `16-cutter-compensation` | 326 | 0 | 2 |
| `18-canned-cycles` | 288 | 0 | 2 |
| `19-turning-programming` | 326 | 0 | 2 |
| `20-milling-programming` | 300 | 0 | 2 |
| `21-threading-basics` | 249 | 0 | 2 |
| `22-lathe-threading` | 260 | 0 | 2 |
| `23-program-safety` | 831 | 0 | 3 |
| `24-program-verification` | 434 | 0 | 2 |
| `25-troubleshooting` | 308 | 0 | 2 |
| `26-common-mistakes` | 300 | 0 | 2 |
| `27-turning-project` | 257 | 0 | 2 |
| `28-milling-project` | 247 | 0 | 2 |
| `30-reference` | 192 | 0 | 1 |
| `31-learning-path` | 185 | 0 | 2 |
| `32-drawings-process-planning` | 351 | 0 | 2 |
| `33-drilling-cycles` | 289 | 0 | 2 |
| `34-subprograms` | 301 | 0 | 2 |
| `35-practical-examples` | 175 | 0 | 2 |
| `36-macro-programming` | 246 | 0 | 2 |
| `37-probing` | 289 | 0 | 2 |
| `38-controller-specific` | 248 | 0 | 2 |
| `38-process-optimization` | 238 | 0 | 2 |
| `39-assessment` | 385 | 0 | 1 |
| `39-exercises-assessment` | 231 | 0 | 1 |
| `40-glossary` | 244 | 0 | 1 |
| `40-glossary-sources` | 237 | 0 | 0 |
