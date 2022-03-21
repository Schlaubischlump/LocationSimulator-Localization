#/usr/bin/env python3
# To get a list with all untranslated keys print pipe the stderr

import os
import sys
import plistlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(dest="loc_file", help="The base localization file to translate.")
parser.add_argument("-l", "--language", type=str, default="de")
parser.add_argument("-a", "--appname", type=str, default="LocationSimulator")
args = parser.parse_args()

# Read in all available translations
key = f"{args.language}.lproj"
mainMenuFile = open("MainMenuTranslations.plist", "rb")
main_menu_strings = plistlib.load(mainMenuFile)
translations = main_menu_strings[key]
mainMenuFile.close()

# Translate the file
fileToTranslate = open(args.loc_file, "r")

os.mkdir(key)
targetFile = open(f"{key}/Localizable.strings", "w+")

totalEntries = 0
translatedEntries = 0

for line in fileToTranslate:
    comp = line.split('"')
    if len(comp) >= 5:
        # Increase the total entries count
        totalEntries += 1
        # Read the key and value
        key, value = comp[1], comp[3]
        # Replace the application name
        new_value = value.replace(args.appname, "APPLICATIONNAME")
        # Lookup the translation
        translation = translations.get(new_value, "")
        # Insert the real application name in the translation
        translation = translation.replace("APPLICATIONNAME", args.appname)
        comp[3] = translation
        # Write the new string
        targetFile.write('"'.join(comp))
        # If a new translation was written
        if translation and translation != value:
            translatedEntries += 1
            print(f"{key}\t{value}\t{translation}", file=sys.stdout)
        else:
            print(f"\033[01;31m{key}\t{value}\033[0m", file=sys.stderr)
    else:
        targetFile.write(line)

print()
print(f"Finished. Translated {translatedEntries} of {totalEntries} entries.")

fileToTranslate.close()
targetFile.close()
