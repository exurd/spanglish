#                This code has been licensed by the
#            DO WHAT THE F*CK YOU WANT TO PUBLIC LICENSE
#                             Version 2
import sys
import argparse
import googletrans
from googletrans import Translator

parser = argparse.ArgumentParser(description="Translates a piece of text in the worst way possible.", epilog="This program has the WTFPL license. DO WHAT THE F*CK YOU WANT TO.")
parser.add_argument('--phrase', '-p', type=str,  help="The phrase you want to translate. Make sure it's spelt correctly!", default="The quick brown fox jumps over the lazy dog.")
parser.add_argument('--source_language', '-s', type=str,  help="The source text language. Use two letter codes or else it won't work.", default="en")
parser.add_argument('--destination_language', '-d', type=str,  help="The source text language. Same as source language; use two letter codes!", default="es")
parser.add_argument('--check_languages', help="Checks for languages possible on googletrans.", action='store_true')
parser.add_argument('--version', action='version', version='%(prog)s 0.1')
args, unknown = parser.parse_known_args()

# Checks if you are using the check_languages argument
if args.check_languages == True:
    print("The languages possible are:")
    print(googletrans.LANGUAGES)
    print("The program will now close.")
    sys.exit()

# Splits the phrase into words
words = args.phrase.split(" ")

# Puts it through the translator
translator = Translator()

# Uses this code if the argument source_language uses detect
if args.source_language == "detect":
    detection = translator.detect(args.phrase).lang
    print("Phrase was detected as", detection + ".")
    translations = translator.translate(words, src=detection, dest=args.destination_language)
else:
    translations = translator.translate(words, src=args.source_language, dest=args.destination_language)

# Prints out the result
print(args.phrase)
print("↓↓↓↓↓")
for translation in translations:
    print(translation.text, end=" ")