# bruteforce legacy file converter

A tool that leverages the legacyfileconverter tool and tries to convert a file using all of the 200+ included converters  

http://www.columbia.edu/~em36/legacyfileconverter.html 

This tool requires the above application to be installed on your system. The path to exe file should be changed on line #250

`location_of_legacyfileconverter_application = r"E:\\tools\\LegacyFileConverter\\source\\LegacyFileConverter.exe"`

The python wrapper uses the tool to try all the converters included in the app. 

When the tool is run, and new folder is created in the same folder as the file being used called `conversions`

Inside this folder, another folder is created called the same as the file name. 

The python tool then takes all the 208 codes recognised by LegacyFileConverter.exe and one by one requests a conversion. If the conversion is successful, a new converted file is created, inside this folder with the original filename prepended by the conversion code. 

There is some "hand holding" needed - vdos can hang a few times per run, the user needs to close the popup window and the python script carries on. 

There was also a minor issue with the original package for LegacyFileConverter.exe as found on the website. even in `/silent` mode the tool was requesting human input for most of the conversions. Working with the oroginal developer, we were able to repackage the tool in such a way that  `/silent` mode is now as expected. This version in included in this repo.   
