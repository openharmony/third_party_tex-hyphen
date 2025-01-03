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
* as - 阿萨姆语（Assamese）
* be - 白俄罗斯语（Belarusian）
* bg - 保加利亚语（Bulgarian）
* bn - 孟加拉语（Bengali）
* cs - 捷克语（Czech）
* cy - 威尔士语（Welsh）
* da - 丹麦语（Danish）
* de-1901 - 德语（German,1901orthography）
* de-1996 - 德语（German,1996orthography）
* de-ch-1901 - 瑞士德语（SwissGerman,1901orthography）
* el-monoton - 现代希腊语（ModernGreek,monotonic）
* el-polyton - 现代希腊语（ModernGreek,polytonic）
* en-gb - 英式英语（BritishEnglish）
* en-us - 美式英语（AmericanEnglish）
* es - 西班牙语（Spanish）
* et - 爱沙尼亚语（Estonian）
* fr - 法语（French）
* ga - 爱尔兰语（Irish）
* gl - 加利西亚语（Galician）
* gu - 古吉拉特语（Gujarati）
* hi - 印地语（Hindi）
* hr - 克罗地亚语（Croatian）
* hu - 匈牙利语（Hungarian）
* hy - 亚美尼亚语（Armenian）
* id - 印度尼西亚语（Indonesian）
* is - 冰岛语（Icelandic）
* it - 意大利语（Italian）
* ka - 格鲁吉亚语（Georgian）
* kn - 卡纳达语（Kannada）
* la - 拉丁语（Latin）
* lt - 立陶宛语（Lithuanian）
* lv - 拉脱维亚语（Latvian）
* mk - 马其顿语（Macedonian）
* ml - 马拉雅拉姆语（Malayalam）
* mn-cyrl - 蒙古语（Mongolian,Cyrillicscript）
* mr - 马拉地语（Marathi）
* mul-ethi - 埃塞俄比亚语（Ethiopic）
* nl - 荷兰语（Dutch）
* or - 奥里亚语（Odia）
* pa - 旁遮普语（Punjabi）
* pl - 波兰语（Polish）
* pt - 葡萄牙语（Portuguese）
* rm - 罗曼什语（Romansh）
* ru - 俄语（Russian）
* sh-cyrl - 塞尔维亚-克罗地亚语（Serbo-Croatian,Cyrillicscript）
* sh-latn - 塞尔维亚-克罗地亚语（Serbo-Croatian,Latinscript）
* sk - 斯洛伐克语（Slovak）
* sl - 斯洛文尼亚语（Slovenian）
* sr-cyrl - 塞尔维亚语（Serbian,Cyrillicscript）
* sv - 瑞典语（Swedish）
* ta - 泰米尔语（Tamil）
* te - 泰卢固语（Telugu）
* th - 泰语（Thai）
* tk - 土库曼语（Turkmen）
* tr - 土耳其语（Turkish）
* uk - 乌克兰语（Ukrainian）
* zh-latn-pinyin - 汉语拼音（Chinese,Pinyin）

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


