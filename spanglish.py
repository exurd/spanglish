#                This code has been licensed by the
#            DO WHAT THE F*CK YOU WANT TO PUBLIC LICENSE
#                             Version 2
import sys
import argparse
import googletrans
from googletrans import Translator

parser = argparse.ArgumentParser(description="Translates a piece of text in the worst way possible.", epilog="This program has the WTFPL license. DO WHAT THE F*CK YOU WANT TO.")
parser.add_argument('--phrase', '-p', type=str,  help="The phrase you want to translate. Make sure it's spelt correctly!", default="The quick brown fox jumps over the lazy dog.")
parser.add_argument('--source_language', '-s', type=str,  help="The source text language. Use two letter codes or else it won't work. If you don't know what the language is, you can type 'detect'.", default="en")
parser.add_argument('--destination_language', '-d', type=str,  help="The source text language. Same as source language; use two letter codes!", default="es")
parser.add_argument('--check_languages', help="Checks for languages possible on googletrans.", action='store_true')
parser.add_argument('--version', action='version', version='%(prog)s 0.1.0')
args, unknown = parser.parse_known_args()

# Checks if you are using the check_languages argument
if args.check_languages == True:
    print("The languages possible are:")
    print(googletrans.LANGUAGES)
    print("The program will now close.")
    sys.exit()

# Activates the translator
translator = Translator()
detection = "detection" # so the program won't error out when checking for a logographic language

if args.source_language == "detect":
    detection = translator.detect(args.phrase).lang
    print("Phrase was detected as", detection + ".")

# Checks if the detection it's a logographic language and splits the phrase into parts if so
if detection == "ar" or args.source_language == "ar":
    words = [i for i in args.phrase]
elif detection == "zh-TW" or args.source_language == "zh-TW":
    words = [i for i in args.phrase]
elif detection == "zh-CN" or args.source_language == "zh-CN":
    words = [i for i in args.phrase]
elif detection == "jw" or args.source_language == "jw":
    words = [i for i in args.phrase]
elif detection == "ja" or args.source_language == "ja":
    words = [i for i in args.phrase]
elif detection == "ko" or args.source_language == "ko":
    words = [i for i in args.phrase]
else:
    words = args.phrase.split(" ") # Splits the phrase into words

# Uses this code if the argument source_language uses detect
if args.source_language == "detect":
    translations = translator.translate(words, src=detection, dest=args.destination_language)
else:
    translations = translator.translate(words, src=args.source_language, dest=args.destination_language)

# Prints out the result
print(args.phrase)
print("↓↓↓↓↓ (" + args.destination_language + ")")
for translation in translations:
    print(translation.text, end=" ")