# spanglish
[![the logo](https://raw.githubusercontent.com/exurd/spanglish/master/docs/logo.png)](https://github.com/exurd/spanglish/ "at least it has more of a reason to live than smilk.")
###### for python 3+ only
[![GitHub version](https://badge.fury.io/gh/exurd%2Fspanglish.svg)](https://badge.fury.io/gh/exurd%2Fspanglish) ![hyper](https://img.shields.io/badge/runs%20better%20with-hyper-red "i mean, someone said so.") ![build status](https://img.shields.io/badge/build%20status-%C2%A1Muy%20bien!-green "that's good!")

Have you ever seen a translation so bad it's good? spanglish tries to replicate this by translating a sentence on Google Translate word by word, instead of the whole sentence. This leads to the program generating readable nonsense.

### Examples:

```
No solo me gusta la trama de esta película, sino que también me encanta la banda sonora y el elenco es muy talentoso.

↓↓↓↓↓ (en)

Not alone I like the plot of is movie, if not than too I love it the band sonorous and he cast it is very talented.
```

```
我在浪费时间。

↓↓↓↓↓ (en)

I in wave fee Time between.
```

```
こんにちは

↓↓↓↓↓ (en)

This Hmm To Chi Is
```

```
Because I had to catch the train, and as we were short on time, I forgot to pack my laptop in my suitcase for our one in a lifetime honeymoon.

↓↓↓↓↓ (ko)

때문에 나는 했다 에 잡기 그만큼 기차, 과 같이 우리 했다 짧은 의 위에 시각, 나는 잊었다 에 팩 나의 노트북 에 나의 여행 가방 ...에 대한 우리의 하나 에 ㅏ 일생 신흔 여행.
```

```
Можно, пожалуйста, твой номер телефона?

↓↓↓↓↓ (en)

Can, you are welcome, is yours number phone?
```

## Usage

### Requirements

spanglish requires the packages 'googletrans' and 'hyper'.

You can install the packages via 'pip install -r requirements.txt'.

### Help

To get help in the program you can use the -h parameter:

```
usage: spanglish.py [-h] [--phrase PHRASE] [--source_language SOURCE_LANGUAGE]
                    [--destination_language DESTINATION_LANGUAGE]
                    [--check_languages] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --phrase PHRASE, -p PHRASE
                        The phrase you want to translate. Make sure it's spelt
                        correctly!
  --source_language SOURCE_LANGUAGE, -s SOURCE_LANGUAGE
                        The source text language. Use two letter codes or else
                        it won't work. If you don't know what the language is,
                        you can type 'detect'.
  --destination_language DESTINATION_LANGUAGE, -d DESTINATION_LANGUAGE
                        The source text language. Same as source language; use
                        two letter codes!
  --check_languages     Checks for languages possible on googletrans.
  --clean               Makes the translation output the only thing to appear.
  --version             show program's version number and exit
```

### Translate

To type translate using spanglsh:

```
>spanglish -s en -d es
```
The default text is "The quick brown fox jumps over the lazy dog." The phrase must be encased in quotation marks for script to work. Afterwards, the translater will translate it as:

```
The quick brown fox jumps over the lazy dog.

↓↓↓↓↓ (en)

los rápido marrón zorro saltos encima el perezoso perro.
```

You can also translate into different languages other than English:

```
>spanglish --phrase "Este script de Python apesta y debería ser exiliado de GitHub por hacer esto" -s es -d ja
Este script de Python apesta y debería ser exiliado de GitHub por hacer esto

↓↓↓↓↓ (ja)

この 脚本 の パイソン 悪臭 そして すべき なる 追放された の GitHub 沿って 行う この
```

### Detect Languages

To detect languages you don't know, you can use detect instead of a code. It will tell you which language it is in and use it automatically.
```
>spanglish --phrase "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eu libero mauris." --source_language detect -d en
Phrase was detected as la.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eu libero mauris.

↓↓↓↓↓ (en)

lorem very pain let it be carrots; Minneapolis undergraduate developer. to football free start.
```

### Check Languages that you can use

To check what languages you can use and get their codes, you can use the --check_languages argument.
```
>spanglish --check_languages
The languages possible are:
{'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', ... 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
```

## Notes

Release executable is made using PyInstaller.

This program has been licensed with "Do What The F-ck You Want To Public License". In short, DO WHAT THE F-CK YOU WANT TO DO WITH THIS!
