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
parser.add_argument('--clean', help="Makes the translation output the only thing to appear.", action='store_true')
parser.add_argument('--boomerang', '-b', help="Translates it back to source language after translation. If --clean is on it will only display the boomeranged translation.", action='store_true')
parser.add_argument('--version', action='version', version='%(prog)s 0.1.0')
args, unknown = parser.parse_known_args()

# Checks if you are using the check_languages argument; if so it will display languages and close
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
    if args.clean == False:
        print("\n")
        print("Phrase was detected as", detection + ".")
        print("\n")

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
    words = args.phrase.split(" ") # For other languages it just splits the phrase into words

if args.source_language == "detect":
    translations = translator.translate(words, src=detection, dest=args.destination_language) # If the argument source_language uses detect it will use this
else:
    translations = translator.translate(words, src=args.source_language, dest=args.destination_language)

# Prints out the result
if args.clean == False: # If false it will display the original and the arrows
    print(args.phrase)
    print("\n")
    print("↓↓↓↓↓ (" + args.destination_language + ")")
    print("\n")
if args.clean == False:
    for translation in translations:
        print(translation.text, end=" ")
    print("\n")
elif args.boomerang == False:
    for translation in translations:
        print(translation.text, end=" ")
    print("\n")

# Next part is for the boomerang argument
if args.boomerang == True:
    # Checks if the detection it's a logographic language and splits the phrase into parts if so
    if args.destination_language == "ar":
        boomerwords = [i for i in args.phrase]
    elif args.destination_language == "zh-TW":
        boomerwords = [i for i in args.phrase]
    elif args.destination_language == "zh-CN":
        boomerwords = [i for i in args.phrase]
    elif args.destination_language == "jw":
        boomerwords = [i for i in args.phrase]
    elif args.destination_language == "ja":
        boomerwords = [i for i in args.phrase]
    elif args.destination_language == "ko":
        boomerwords = [i for i in args.phrase]
    else:
        boomerwords = args.phrase.split(" ") # For other languages it just splits the phrase into words
    
    if args.source_language == "detect":
        boomertranslations = translator.translate(boomerwords, src=args.destination_language, dest=detection) # If the argument source_language uses detect it will use this
    else:
        boomertranslations = translator.translate(boomerwords, src=args.destination_language, dest=args.source_language)
        
    if args.clean == False: # If false it will display the original and the arrows
        print("\n")
        if args.source_language == "detect":
            print("↓↓↓↓↓ (" + detection + ")")
        else:
            print("↓↓↓↓↓ (" + args.source_language + ")")
        print("\n")
    for translation in boomertranslations:
        print(translation.text, end=" ")
        
    print("\n")