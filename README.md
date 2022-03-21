# Localization

These are the official localization files for LocationSimulator. Feel free to fork the project and contribute to an existing language or create a new one. The easiest why to edit these files is by using [LocalizationEditor](https://github.com/igorkulman/iOSLocalizationEditor). Just click on the release link on the right sidebar and download the latest release. To contribute a new language follow these steps: 

1. Download or clone this repository. 
2. Create a new folder with your language code and the file ending `lproj`. 
3. Place a new empty file called `Localizable.strings` inside the newly created folder.
4. Start `LocalizationEditor` and click on the folder icon.
5. Choose the downloaded `Localization` folder.
6. You'll get a list will all strings to localize. Missing strings are highlighted with a red border.
7. Open a pull request or open a new issue and upload your strings.

If you want to edit an existing language just skip step 2 and 3. If you need some help with creating a new language, let me know! If you are a developer or know how to install python3 and use a terminal you can easily create a new language which already has some pre-translated entries. 

Run the following command and replace `LANGUAGE_CODE` with your language code. E.g. this would be `de` for german.

```
python3 MainMenuTranslate.py Base.lproj/Localizable.strings -l LANGUAGE_CODE
```