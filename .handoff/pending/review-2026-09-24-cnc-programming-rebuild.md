# Review — CNC Programming Rebuild

日期：2026-09-24  
结论：**不通过，需返修；不能按“DONE”验收完整课程。**  
对照：`.handoff/pending/2026-09-24-cnc-programming-fundamentals-applications-spec.md`。  
审阅版本：HEAD `80051d9`；功能提交 `a5c592e`，清理提交 `0a1a54a`；diff基线 `f221f5d`。完成报告写的0a1a54a是清理提交，应连同功能提交说明。开始/结束检查时工作区干净。本次仅写审阅报告，未改网页、运行生成器或推送。

## 审阅范围与已通过项

全量检查41页的路径、站内href/src、canonical与sitemap、英文词数近似统计、SVG/答案数量；重点人工审查坐标/刀补/圆弧/进给/循环/安全/验证/两项目/子程序/宏/探测/考核/路线。官方资料用于核验控制器行为；代码几何采用独立推导。线上浏览器抽查15页，默认1280px宽与390×844窄屏；不是完整移动端矩阵测试，也不是控制器仿真或实机验证。

已通过：
- 41个目标HTML均存在，旧23条路径保留，新增18页。
- 扫描当前41页实际引用的站内href/src和锚点，未发现目标不存在的链接。此检查不证明旧外部书签兼容，见R13。
- 41个canonical均在sitemap中；相对基线未删除旧sitemap URL；无重复URL。
- 六项全局导航、文章返回板块首页及基本页脚已存在。
- 15文字例题的G03、31.416/94.248计算已纠正，但图形仍错。
- 390px线上15页未发现整页横向溢出；其余规定页面/视口尚未验证。

## 必须修复的发现

优先级：P1为会误导操作/代码结果或构成核心交付缺失的阻断项；P2为课程一致性、设计和可核验性缺陷。下列位置均为审阅版本的仓库相对路径与行号。

### R01 [P1] 重启教学要求直接跳到断刀行，缺失状态恢复

位置：`docs/cnc-programming/23-program-safety/index.html:31`、`:37`（正文及练习答案）。

当前教读者换刀后手动定位到N80附近直接重启，并绝对化“never from the top”。中途程序行依赖此前建立的工具、长度/半径补偿、工件零点、循环、进给模式和接近路径，手动移到附近不能恢复这些状态。页面还把一组铣床启动码宣称适用于“every program”，同时标Mill & Lathe；这既不清除所有状态，也不适用于所有车床。

Haas的Program Restart设置涉及对前文状态的扫描，不能省略其适用设置及重启路径检查：[Haas Setting 36](https://www.haascnc.com/service/codes-settings.type=setting.machine=mill.value=S36.html)。

修复：删除当前断言与答案，按照SPEC 23重写为“确认安全状态→核对更换工具/偏置→选择经过验证的重启入口→按具体控制器重建/核对状态→检查退刀/接近包络”。分开铣车启动；不把任意N行、从头运行或某组代码称为普适安全方案。

回验：给出遗留G91、错误H号、活动循环三种重启案例，读者能说明缺失状态和恢复验证；正文和答案不能仍然建议只定位后跳行。

### R02 [P1] 铣削“完整项目”不能产生所述零件

位置：`docs/cnc-programming/28-milling-project/index.html:26`、`:31–47`，尤其`:46`。

`Y20. X60. Y-20. X0.`写在同一block，不是四条依次执行的轮廓边，而是同块重复X/Y地址，不能表达声称的矩形路径。即使拆成四行，轮廓在Y负侧、没有口袋内部清料轨迹，也不是100×80板中心的60×40口袋。面铣仅在Y0走一次Ø63刀，无法覆盖Y0–80整面。列出T04倒角却没有该工序代码。该页还擅自把SPEC的40×30×4、R5口袋和Ø6孔变成60×40×5、Ø8孔。

修复：回到SPEC28统一的尺寸/原点/夹持定义，重建刀心轨迹、合法进刀、分层覆盖、钻尖深度和退刀；每个运动block单独一行。按SPEC已加工顶面方案处理Z0，不额外声称完成未实现的面铣/倒角。补工具表、D/H含义、机型、初始状态和检查记录。

回验：语法检查通过；背绘端点、圆角、口袋覆盖和孔中心与尺寸图一致；对刀柄/背面垫块包络做独立检查，不能只检查出现了G41/G80。

### R03 [P1] 螺纹与进给混用方言，G95在Haas车床并非每转进给

位置：`docs/cnc-programming/10-spindle-feed/index.html:31`；`docs/cnc-programming/22-threading/index.html:31–39`。

首页宣称Haas-verified，但10/22把车床G95解释为mm/rev；Haas车床G95是动力刀具端面刚性攻丝，普通每转进给应按其G99语境解释。22又把FANUC风格双行G76、未经声明的P/Q小数单位与Haas来源混排。示例X28/P1.08与正文X28.16、径向深约0.92互相不一致；“约5–6刀”没有充分参数依据。

依据：[Haas G95](https://www.haascnc.com/service/codes-settings.type=gcode.machine=lathe.value=G95.html)、[Haas G76](https://www.haascnc.com/service/codes-settings.type=gcode.machine=lathe.value=G76.html)。官方G76用K/D等定义牙高/首刀量，不能把这里的两行格式标成已核验Haas示例。

修复：按SPEC教学基准重写10和22，逐一声明机型/控制器/版本和参数单位；螺距与多头导程区分；实际牙深与最终尺寸由牙型、公差和刀片资料确定。不要只把G95替换成G99而保留不匹配的整套G76参数。

回验：逐地址对照适用手册，代码、图纸和数字例题三者一致；给定500rpm、单头1.5mm导程的同步轴向速度为750mm/min，并明确该计算不等于任意模式下的F字输入值。

### R04 [P1] 刀长误差方向反了，首件修正建议可能进一步加深

位置：`docs/cnc-programming/12-tool-offsets/index.html:29`、`:35`；`docs/cnc-programming/24-verification/index.html:39`（Example段，以文本定位复核）。

12写H=100而实际刀长102会切浅2mm；在该文暗示的正刀长、Z向上模型下，实际刀尖更低，应该切深2mm。`machine_home + H01 + (-5)`又漏了工件零点和符号定义。24将实测口袋深10.02、目标10.00直接给出wear=-0.02，也未说明控制器约定；在正刀长补偿模型中减小有效刀长会进一步切深。

独立几何回算：设工件零点机器Z=-400，编程刀尖Z=-5、存储H=100，基准面=-305；实际L=102时刀尖=-407，即工件Z=-7，深2mm。

修复：按SPEC12画基准面—刀尖—工件零点尺寸链，明确假设。用有符号推导解释改偏置后刀尖如何移动，禁止把一个wear正负号当通用修正。删去“spindle nose必然撞零件”等无条件结论。

回验：刀具比记录长/短各2mm的两题能正确推导；对过深口袋的补偿解释不会再使刀尖更低。

### R05 [P1] 验证页把抬高试运行当成碰撞证明

位置：`docs/cnc-programming/24-verification/index.html:27–43`。

当前固定“Z=+50 dry run”“25% feed override”并宣称抬高空跑能发现深口袋的刀柄碰虎钳，且笼统说仿真不建模夹具/刀柄。抬高路径并不能复现真实切深的刀柄干涉；仿真能力取决于模型与功能。攻丝/螺纹的倍率也不能按一般进给统一处理。

修复：按SPEC24分清语法、状态、背绘、材料去除、机床/夹具碰撞和现场验证；声明每层覆盖/未覆盖范围，安全高度来自实际包络。现场试运行和倍率按具体机床/工序规程，不给统一数值口诀。

回验：把“有夹具模型的机床仿真”和“只画刀尖线的背绘”分开；不得以抬高后的空跑宣称排除实际切深碰撞。保留独立首件尺寸检验。

### R06 [P1] 车削项目违反轮廓限制，并未完成所称切断

位置：`docs/cnc-programming/27-turning-project/index.html:38–58`。

粗精轮廓P10–Q20包含先往负Z加工、再在`N20 G00 Z2.`逆向返回的段；该段不应当作为G71最终零件轮廓。Haas G71要求轮廓Z不改变方向，Type II也不放宽此项：[Haas G71](https://www.haascnc.com/service/codes-settings.type=gcode.machine=lathe.value=g71.html)。结束只切到X1，直径模式仍有Ø1芯，不能无条件称为已切断。验证文字“center outward”与代码X42→X-1相反；零点G54只在文字出现未明确选定；缺夹持/刀宽参考信息，不能由Z-36直接得“36mm加刀宽”的最终长度。

修复：恢复SPEC27只加工前端台阶、不切断的清晰范围及尺寸；轮廓和退刀分离。若要另做切断项目，应单列经核验的刀宽参考、夹持、接料/支撑和余量方案，不在现项目中临时增加。

回验：P/Q段只含允许的目标轮廓；粗精加工图与程序逐点一致；文字不再声称程序未完成的工序。

### R07 [P1] “4×3孔阵列”子程序实际不换行

位置：`docs/cnc-programming/29-subprograms/index.html:32–43`。

主程序只用`M98 P0201 L4`，子程序只有增量X20/Y0重复3次，没有Y行距或X复位。忽略其他语法/状态缺陷仅追踪XY，四次调用得到X20至240、Y始终0，不是4行3列。初始Z50下使用G91 R5/Z-15也不能按绝对R5/孔底-15解读；主/子程序号仅在注释里，不能直接作为完整两程序文件。

修复：明确主程序负责换行/定位、子程序的入口出口状态契约；先列12个目标点，再生成调用代码。给出真正程序标识或清楚标Fragment，并单独追踪循环的增量Z/R语义。

回验：展开全部调用后恰有指定12个XY点和一致孔底；调用后模式/位置已知，不能用一句“explicit and safe”代替验证。

### R08 [P1] 宏示例跳转目标不存在

位置：`docs/cnc-programming/36-macro-foundations/index.html:35–40`。

使用`O1000`作循环标记，却`GOTO1000`；O为程序标识，GOTO需指向N块标记，示例没有N1000。孔数直接作除数且缺count范围检查；宏语法也未明确机型/选项。

依据：[Haas Macro Programming Information](https://www.haascnc.com/content/dam/haascnc/service/guides/how-to/lathe-work-probe-%28lpro-r%29---chc---installation---ad0027/macro_programming_information.pdf)。

修复：先交无运动的数学/循环练习，再给按声明控制器核验过的宏；区分程序头与分支标签，加入输入校验/循环上限，核对表达式括号与变量范围。

回验：count=4坐标表正确，count=0/负数可控拒绝；合法分支目标均存在，不把除零/死循环留给机床报警。

### R09 [P2] 圆弧SVG不属于标出的圆心

位置：`docs/cnc-programming/15-circular-interpolation/index.html:31–37`。

背景圆C在屏幕(40,100)、R80，S=(40,180)、E=(120,100)。当前`A 80 80 0 0 1`选择的是中心(120,180)那条短弧，因此绿色弧在灰色圆内而非其上。线上截图已复核，文字更正并未修正图形。

修复：此坐标下短弧应使用`A 80 80 0 0 0 120 100`，并扩展viewBox容纳左侧被裁掉的灰圆，加入行进箭头与明确观察方向。另按SPEC补长弧/螺旋图。

回验：取弧中点约屏幕(96.569,156.569)，距标记中心80；绿色轨迹必须与所标圆同圆，不能仅核对端点。

### R10 [P2] 综合考核给出了错误的固定循环答案

位置：`docs/cnc-programming/39-exercises-assessment/index.html:35–40`。

题目含`G00 X0 Y0`却判其仍会钻孔。在课程声明的Haas铣床语境下，G00/G01也会取消固定循环；建议显式G80有利于可读性，但不等于当前题目的行为解释正确。依据：[Haas G80](https://www.haascnc.com/service/codes-settings.type=gcode.machine=mill.value=G80.html)。

修复：如要考继续钻孔，提供仍处于循环中且仅写XY的新位置行，并声明前置状态；保留显式取消的编码规范，但解释真实行为。其他代码阅读题也须说明初始Z、单位、工具等前提，第一行只有XY不能推定“above part”。

回验：分别比较循环后`X0 Y0`、`G00 X0 Y0`、`G80`三种结果，答案与指定手册一致。

### R11 [P2] 探测示例把另一方言和工件偏置更新混为一谈

位置：`docs/cnc-programming/37-multiaxis-probing-overview/index.html:32`。

`M06 probe, G38.2 ... records ... into work offset`不是已声明Haas机型的可核验语法。触碰坐标记录与更新工作偏置也不是同一步；Haas G31记录跳跃位置至宏变量，OEM探测循环可能另行计算/写偏置。[Haas G31](https://www.haascnc.com/service/codes-settings.type=gcode.machine=mill.value=G31.html)。LinuxCNC的G38.2同样将结果存为探测参数，并非自动把G54改成触点：[LinuxCNC G-codes](https://www.linuxcnc.org/docs/scratch/html/gcode/g-code.html)。

修复：遵从SPEC37，只讲校准→接近→记录→计算→独立核验，不编造OEM调用；如保留具体语法必须分别标出控制器和副作用。

回验：读者能区分测到一个位置、计算偏置、批准写入偏置；去除“M06 probe”伪代码冒充实机命令。

### R12 [P1] 全量内容深度、图示和练习未达到交付要求

位置：全40篇；代表 `docs/cnc-programming/08-programming-math/index.html:26`、`docs/cnc-programming/39-exercises-assessment/index.html:26`、`docs/cnc-programming/40-glossary-sources/index.html:25`。

静态抽取main可读英文单词，去掉pre/svg内容，但仍计入目标/答案/来源/底部导航，因此对教学正文偏宽松：40篇约111–520词，全部低于B篇最低800，更低于K篇2000。35篇无SVG；其中大量也无实际ASCII示意图。34篇少于3个details答案；所有文章都没有外部来源链接。39只有3组简短练习，无要求的20道基础题、两份审码、两项目、100分评分与80分门槛；首页却宣称“20 questions, two projects”。40只有16条术语而非40–60条。

这不是“少数篇幅略短/图可更丰富”，而是尚未完成详细课程。代表缺项：08未完整讲三角函数/数值步骤；15缺螺旋；34没有真实螺纹铣削例题；37无旋转/测量数字例；绝大多数无具体先修链接和逐行状态表。

修复：逐篇按SPEC D节补齐实质内容，不用模板、代码或导航凑词数。按B/K实现例题、实际图、三题及解析；39/40按单独数量和结构要求完成。来源提供可点击具体章节/版本/适用条件，不能用“Haas Manual”“Shop best practices”代替证据。恢复教学假设标签，不能只写“adjust feeds”就把任意数值当推荐。

回验：提交40行验收矩阵（词数口径、六段、先修、图数、题数、数字例题、来源、未完成项）；每个K篇至少2图/2例或完整项目+变式；完整评分表合计100，答案独立回算。

### R13 [P2] 三种学习顺序不一致，旧锚点兼容丢失

位置：`docs/cnc-programming/31-learning-path/index.html:25`起；各页`.cp-nav-bottom`，例如`02-machine-fundamentals/index.html`底部；首页。

首页按SPEC七模块排布，31却是另一套六阶段、漏多篇；底部导航仍按01→02→03编号串联，绕过首页安排的安全/数学/图纸先修。31自身还把服务页串入课程连续顺序。旧首页`ch01/ch05/ch10/ch14/ch17/ch23/ch30`七锚点全部不存在，外部旧书签不会落到预期模块。

修复：首页、31、上下课链接共用同一明确顺序表；保持23早期入口/复习入口的区别，服务页回Start the course；恢复七旧锚点映射并加先修链接。

回验：从01只点Next即可走完SPEC规定的首访顺序；31逐项一致。手动打开七个旧URL#chXX都能落到对应内容。当前站内链接检查无坏链并不能替代这项兼容验收。

### R14 [P2] 文章模板绕开既有样式，设计和访问性要求未落实

位置：全部文章`<main class="cp-article">`（通常行20）；`docs/assets/css/cnc-programming.css:1–7`；`docs/cnc-programming/index.html:6`。

使用cp-article替代要求的article，导致article.css里的h1/h2/表格等规则不命中；线上15页h2实际是#17242f而非规定accent-dark。body也没有cnc-programming class，声明的作用域选择器不命中。CSS/图示引入额外色值；SVG无title/desc；首页title仍旧而非规定后缀；所有文章把指向板块首页的链接标aria-current=page。未完成规定视口矩阵及键盘/200%文字检查。

修复：恢复`body.cnc-programming`和`main.article`/lead及既有类复用，新增样式以模块作用域覆盖；图表加可访问名称和表头语义；修正aria-current与首页SEO。重新做规定移动端/键盘检查。

回验：计算样式符合PROJECT_CONTEXT；未污染别的板块；360/390/768/1440各指定页有证据，SVG标签可读、代码/宽表局部滚动。

## 完成报告与证据需同步修正

- “All 6-section teaching structure per page”不成立：27/28用Process Plan/Verification替代Why/Example，Practice为H3；39及30/31/40也非所需统一结构；部分页连Example都缺。
- 报告称CSS例D50=955/D25=1910，但10页实际用Vc200，算1273/2546。这组实际数值本身可算对，但不是报告声称核验的那组。攻丝900也只有在600rpm时成立，报告应列清输入而非裸结果。
- “Google verification meta tag present”在这些新课程页面里未见，但本SPEC也未要求每篇复制验证meta；不要将其当作本次通过/失败项。
- gen_cp.py如继续保留，必须同步修复来源内容，避免下一次生成覆盖已修好的HTML；本次未运行它。是否保留生成脚本不是当前主要阻断项。
- 不需要为本次审阅改发布历史；下一份完成报告应准确写已完成/未验证项，不能把缺仿真和缺全量可视验证勾为通过。

## 返修顺序与复审入口

1. 先修R01–R08的操作指导/代码/符号问题，并复核相关练习答案；优先保证不是把错误知识扩写成更长文章。
2. 修R09–R11图形与控制器语义，统一方言和引用。
3. 按R12落实40篇详细教学、真实图、解析和综合考核；同步R13路线与R14模板。
4. 提交新完成报告及明确commit范围、逐页验收矩阵、控制器语法/回绘证据、移动端检查。未取得控制器仿真条件时显式保留未验收，不用HTML无报错代替。

复审通过需：上述发现逐项有对应修改/证据；SPEC所有硬性验收项满足。当前页面骨架和链接已完成，可以作为返修基础，但不能据此宣布完整学习课程已交付。

## 附录：本次静态统计

统计英文词的方式：HTMLParser读取main文本，排除pre/svg/nav；按英文单词切分，数字不计。仍包含目标、练习答案、来源及底部文字，因此不是最终正文词数认证。下表用于定位明显缺项；即使改变分词器，也无法弥合与800/2000词门槛的差距。

| 页面目录 | 可读英文词近似数 | SVG | details答案 |
|---|---:|---:|---:|
| `01-getting-started/what-is-cnc-programming` | 356 | 1 | 3 |
| `02-machine-fundamentals` | 341 | 1 | 2 |
| `03-coordinate-systems` | 520 | 1 | 3 |
| `04-program-structure` | 311 | 0 | 3 |
| `05-gcode-fundamentals` | 379 | 0 | 3 |
| `06-modal-codes` | 193 | 0 | 2 |
| `07-plane-units` | 133 | 0 | 2 |
| `08-programming-math` | 126 | 0 | 2 |
| `09-mcode-fundamentals` | 111 | 0 | 1 |
| `10-spindle-feed` | 182 | 0 | 3 |
| `11-controller-dialects` | 146 | 0 | 1 |
| `12-tool-offsets` | 346 | 0 | 2 |
| `13-work-offsets` | 352 | 0 | 2 |
| `14-linear-interpolation` | 293 | 0 | 2 |
| `15-circular-interpolation` | 366 | 1 | 3 |
| `16-cutter-compensation` | 332 | 1 | 2 |
| `17-drilling-cycles` | 303 | 0 | 2 |
| `18-canned-cycles` | 308 | 0 | 2 |
| `19-turning-fundamentals` | 296 | 0 | 2 |
| `20-turning-cycles` | 266 | 0 | 2 |
| `21-grooving-parting-boring` | 305 | 0 | 2 |
| `22-threading` | 257 | 0 | 2 |
| `23-program-safety` | 337 | 0 | 2 |
| `24-verification` | 337 | 0 | 2 |
| `25-troubleshooting` | 304 | 0 | 2 |
| `26-common-mistakes` | 308 | 0 | 2 |
| `27-turning-project` | 202 | 0 | 2 |
| `28-milling-project` | 185 | 0 | 2 |
| `29-subprograms` | 244 | 0 | 2 |
| `30-reference` | 265 | 0 | 0 |
| `31-learning-path` | 145 | 0 | 2 |
| `32-drawings-process-planning` | 309 | 0 | 2 |
| `33-milling-strategies` | 291 | 0 | 2 |
| `34-tapping-thread-milling` | 237 | 0 | 2 |
| `35-cad-cam-postprocessing` | 292 | 0 | 2 |
| `36-macro-foundations` | 193 | 0 | 1 |
| `37-multiaxis-probing-overview` | 210 | 0 | 1 |
| `38-process-optimization` | 238 | 0 | 2 |
| `39-exercises-assessment` | 231 | 0 | 1 |
| `40-glossary-sources` | 237 | 0 | 0 |
