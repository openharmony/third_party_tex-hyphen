# 三方开源软件tex-hyphen

## tex-hyphen简介
tex-hyphen是一个用于TeX系统的断字模式库，它能够在多种语言中正确地将单词断行，以改善排版效果。

来源：tex-hyphen  
URL：https://github.com/hyphenation/tex-hyphen  
版本：CTAN-2021.03.21  
License：多种组合  

## 引入背景陈述
在多语言文档处理和排版中，正确的断字处理是至关重要的。tex-hyphen 提供了一套通用的断字模式，支持多种语言，为高质量的排版提供了基础保障。在OpenHarmony中，引入tex-hyphen可以显著提升多语言文档的排版质量。

## 语种归类
tex目录下包含了多个来自TeX hyphenations patterns的连字符规则，不同语种使用的开源许可证各不相同，整理归类：
* MIT License
* GPL,GPL 2
* LGPL 1,LGPL 2.1
* LPPL 1,LPPL 1.2,LPPL 1.3
* MPL 1.1
* BSD 3

OHOS中使用以下语种资源：
* 阿拉伯语 Arabic (ar)
* 阿萨姆语 Assamese (as)
* 白俄罗斯语 Belarusian
* 保加利亚语 Bulgarian (bg)
* 孟加拉语 Bengali (bn)
* 捷克语 Czech (cs)
* 威尔士语 Welsh (cy)
* 丹麦语 Danish (da)
* 德语-1901 German (de-1901)
* 德语-1996 German (de-1996)
* 瑞士德语 SwissGerman (de-ch-1901)
* 现代希腊语 Greek (el-monoton)
* 现代希腊语 Modern Greek (el-polyton)
* 英式英语 English （en-gb）
* 美式英语 English （en-us）
* 西班牙语 Spanish （es）
* 爱沙尼亚语 Estonian (et)
* 巴斯克语 Basque (eu)
* 波斯语 Farsi (fa)
* 法语 French (fr)
* 爱尔兰语 Irish (ga)
* 加利西亚语 Galician (gl)
* 古吉拉特语 Gujarati (gu)
* 印地语 Hindi (hi)
* 克罗地亚语 Croatian (hr)
* 匈牙利语 Hungarian (hu)
* 亚美尼亚语 Armenian (hy)
* 印度尼西亚语 Indonesian (id)
* 冰岛语 Icelandic (is)
* 意大利语 Italian (it)
* 格鲁吉亚语 Georgian (ka)
* 卡纳拉语(印度西南部卡纳塔克邦语言) Kannada (kn)
* 现代和中世纪拉丁语 Latin (la)
* 立陶宛语 Lithuanian (lt)
* 拉脱维亚语 Latvian (lv)
* 马其顿语 Macedonian
* 马拉亚兰语(印度西南部喀拉拉邦的语言) Malayalam (ml)
* 蒙古语 Mongolian (mn-cyrl)
* 马拉塔语 Marathi (mr)
* 埃塞俄比亚语 Ethiopic (mul-ethi)
* 挪威语 Norwegian (nb)
* 荷兰语 Dutch (nl)
* 尼诺斯克语 Norwegian, nynorsk (nn)
* 奥里雅语(印度东部奥里萨邦的语言) Oriya (or)
* 旁遮普语 Panjabi (pa)
* 波兰语 Polish (pl)
* 葡萄牙语 Portuguese (pt)
* 罗曼什语 Romansh (rm)
* 俄语 Russian (ru)
* 塞尔维亚-克罗地亚语 Serbo-Croatian,Latin (sh-cyrl)
* 塞尔维亚-克罗地亚语、拉丁语 Serbo-Croatian,Latin (sh-latn)
* 斯洛伐克语 Slovak (sk)
* 斯洛文尼亚语 Slovenian (sl)
* 塞尔维亚语，西里尔文 Serbian Serbian (sr-cyrl)
* 瑞典语 Swedish (sv)
* 泰米尔语 Tamil (ta)
* 泰卢固语 Telugu (te)
* 泰语 Thai (th)
* 土库曼语 Turkmen (tk)
* 土耳其语 Turkish (tr)
* 乌克兰语 Ukrainian (uk)
* 中文拼音 Chinese-pinyin (zh-latn-pinyin)

## 目录结构

```
third_party_tex-hyphen
├── collaboration
│   ├── original
│   ├── repository
│   └── source
├── data/language-codes
├── docs
│   └── languages
├── encoding
│   └── data
├── hyph-utf8
│   ├── doc
│   ├── source
│   └── tex
├── misc
├── ohos
│   ├── src
│   └── hpb-binary
├── old
├── source
├── tests
├── TL
├── tools
└── webpage

collaboration/       tex-hyphen官网依赖的js脚本、xml配置文件
ohos/                OpenHarmony编译文件和hpb二进制文件
data/                语种库
docs/                hyphenation相关文档资料
encoding/            编码数据库
hyph-utf8/           TeX 的断字模式包，提供了以 UTF-8 编码的断字模式
misc/                en-gb语种断词文件案例
old/                 历史数据
source/              源文件包
TL/                  tlpsrc资源文件，tlpsrc文件是TeX Live系统中的一个包源文件，用于描述TeX Live包的元数据
tools/               工具包
webpage/             tex-hyphen官网主页，提供了关于 hyph-utf8 包的详细信息和资源
```

## 为 OpenHarmony 带来的价值

**1.提高排版质量：** 通过引入 tex-hyphen，OpenHarmony 可以实现更为精准的断字处理，提高文档的可读性和美观度。  
**2.提升小屏设备体验：** 在小屏设备中使用断词模式，能够在相同区域内显示更多内容，提升阅读体验。

## OpenHarmony中如何使用tex-hyphen


### 编译步骤
打开终端（或命令提示符），导航到包含 ohos/src/hyphen-build/hyphen_pattern_processor.cpp 文件的目录，并运行以下命令来编译代码：

```
cd ohos/src/hyphen-build/
g++ -g -Wall hyphen_pattern_processor.cpp -o transform
```
上述命令说明：
- g++: 调用 GCC 编译器。  
- -g: 添加调试信息。  
- -Wall: 启用所有警告。  
- hyphen_pattern_processor.cpp: 源代码文件。  
- -o transform: 指定输出的可执行文件名为 transform。

### 运行步骤
编译完成后，可以使用以下命令来运行生成的可执行文件，并处理指定的 .tex 文件：
```
./transform hyph-en-us.tex ./out/
```
上述命令说明：
- ./transform: 运行生成的 transform 可执行文件。  
- hyph-en-us.tex: 输入文件（待处理的 .tex 文件）。  
- ./out/: 输出目录（处理后的文件将存储在此目录中）。  

运行成功后，处理后的文件将存储在 ./out/ 目录中。


