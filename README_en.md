# tex-hyphen
## Introduction
tex-hyphen is a hyphenation pattern library for the TeX system. It can correctly hyphenate words in multiple languages to improve typesetting quality.

Source: tex-hyphen  
URL: https://github.com/hyphenation/tex-hyphen  
Version: CTAN-2021.03.21  
License: Various combinations 

## Background
In multilingual document processing and typesetting, correct hyphenation is crucial. tex-hyphen provides a comprehensive set of hyphenation patterns that support multiple languages, ensuring high-quality typesetting. Introducing tex-hyphen into OpenHarmony can significantly enhance the typesetting quality of multilingual documents.

## Language Classification
The tex directory contains multiple hyphenation patterns from TeX hyphenation patterns, each using different open-source licenses. The classification is as follows:
* MIT License
* GPL, GPL 2
* LGPL 1, LGPL 2.1
* LPPL 1, LPPL 1.2, LPPL 1.3
* MPL 1.1
* BSD 3

Languages used in OHOS:
* Arabic (ar)
* Assamese (as)
* Belarusian
* Bulgarian (bg)
* Bengali (bn)
* Czech (cs)
* Welsh (cy)
* Danish (da)
* German-1901 (de-1901)
* German-1996 (de-1996)
* Swiss German (de-ch-1901)
* Modern Greek (el-monoton)
* Modern Greek (el-polyton)
* British English (en-gb)
* American English (en-us)
* Spanish (es)
* Estonian (et)
* Basque (eu)
* Farsi (fa)
* French (fr)
* Irish (ga)
* Galician (gl)
* Gujarati (gu)
* Hindi (hi)
* Croatian (hr)
* Hungarian (hu)
* Armenian (hy)
* Indonesian (id)
* Icelandic (is)
* Italian (it)
* Georgian (ka)
* Kannada (kn)
* Latin (la)
* Lithuanian (lt)
* Latvian (lv)
* Macedonian
* Malayalam (ml)
* Mongolian (mn-cyrl)
* Marathi (mr)
* Ethiopic (mul-ethi)
* Norwegian (nb)
* Dutch (nl)
* Norwegian, nynorsk (nn)
* Oriya (or)
* Panjabi (pa)
* Polish (pl)
* Portuguese (pt)
* Romansh (rm)
* Russian (ru)
* Serbo-Croatian, Latin (sh-cyrl)
* Serbo-Croatian, Latin (sh-latn)
* Slovak (sk)
* Slovenian (sl)
* Serbian, Cyrillic (sr-cyrl)
* Swedish (sv)
* Tamil (ta)
* Telugu (te)
* Thai (th)
* Turkmen (tk)
* Turkish (tr)
* Ukrainian (uk)
* Chinese-pinyin (zh-latn-pinyin)

## Directory Structure
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
```
collaboration/       JavaScript dependencies and XML configuration files required by the tex-hyphen official website
ohos/                OpenHarmony compilation files and hpb binary files  
data/                Language library  
docs/                Documentation related to hyphenation  
encoding/            Encoding database  
hyph-utf8/           Hyphenation pattern package for TeX, providing hyphenation patterns encoded in UTF-8  
misc/                An example of a hyphenation file for the en-gb language.  
old/                 Historical data  
source/              Source file packages
TL/                  tlpsrc resource files, which are package source files in the TeX Live system, used to describe  
metadata of TeX Live packages  
tools/               Tool packages  
webpage/             tex-hyphen official homepage, providing detailed information and resources about the hyph-utf8 package  


## Value Brought to OpenHarmony
**1. Improved Typesetting Quality:** By introducing tex-hyphen, OpenHarmony can achieve more accurate hyphenation, improving the readability and aesthetics of documents.  
**2. Enhanced Small Screen Experience:** Using hyphenation patterns on small screen devices can display more content in the same area, enhancing the reading experience.

## How to Use tex-hyphen in OpenHarmony
### Compilation Steps
Open the terminal (or command prompt), navigate to the directory containing the ohos/src/hyphen-build/hyphen_pattern_processor.cpp file, and run the following command to compile the code:

```
cd ohos/src/hyphen-build/
g++ -g -Wall hyphen_pattern_processor.cpp -o transform
```

Explanation of the command:
- g++: Invoke the GCC compiler.
- -g: Add debugging information.
- -Wall: Enable all warnings.
- hyphen_pattern_processor.cpp: Source code file.
- -o transform: Specify the output executable file name as transform.

### Execution Steps
After compilation, you can run the generated executable file and process the specified .tex file using the following command:

```
./transform hyph-en-us.tex ./out/
```

Explanation of the command:
- ./transform: Run the generated transform executable file.
- hyph-en-us.tex: Input file (the .tex file to be processed).
- ./out/: Output directory (the processed files will be stored in this directory).

After successful execution, the processed files will be stored in the ./out/ directory.
