# spanglish
[![the logo](https://raw.githubusercontent.com/exurd/spanglish/master/docs/logo.png)](https://github.com/exurd/spanglish/ "at least it has more of a reason to live than smilk.")
###### for python 3+ only
[![GitHub version](https://badge.fury.io/gh/exurd%2Fspanglish.svg)](https://badge.fury.io/gh/exurd%2Fspanglish) ![hyper](https://img.shields.io/badge/runs%20better%20with-hyper-red "i mean, someone said so.") ![build status](https://img.shields.io/badge/build%20status-%C2%A1Muy%20bien!-green "that's good!")

Have you ever seen a translation so bad it's good? spanglish tries to replicate this by translating a sentence on Google Translate word by word.

## Usage

spanglish requires the packages 'googletrans' and 'hyper'.

You can install the packages via 'pip install -r requirements.txt'.

To get help you can use the -h parameter:

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
                        it won't work.
  --destination_language DESTINATION_LANGUAGE, -d DESTINATION_LANGUAGE
                        The source text language. Same as source language; use
                        two letter codes!
  --check_languages     Checks for languages possible on googletrans.
  --version             show program's version number and exit
```

To type translate using spanglsh:

```
>spanglish -s en -d es
```
The default text is "The quick brown fox jumps over the lazy dog." The phrase must be encased in quotation marks for it to work. Afterwards, the translater will translate it as:

```
The quick brown fox jumps over the lazy dog.
↓↓↓↓↓
los rápido marrón zorro saltos encima el perezoso perro.
```

Here is another example.

```
>spanglish --phrase "Este script de Python apesta y debería ser exiliado de GitHub por hacer esto" -s es -d en
Este script de Python apesta y debería ser exiliado de GitHub por hacer esto
↓↓↓↓↓
This script of Python stinks and should be exiled of GitHub by do this
```

To check what languages you can use and get their codes, you can use the --check_languages argument.
```
>spanglish --check_languages
The languages possible are:
{'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', ... 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
```

## Notes

Release executable is made using PyInstaller.

This program has been licensed with "Do What The F-ck You Want To Public License". In short, DO WHAT THE F-CK YOU WANT TO DO WITH THIS!
