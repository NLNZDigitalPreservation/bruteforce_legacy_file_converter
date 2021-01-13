# bruteforce legacy file converter

A tool that leverages the legacyfileconverter tool and tries to convert a file using all of the 200+ included converters (see below for a list of the included converters).

http://www.columbia.edu/~em36/legacyfileconverter.html 

> LegacyFileConverter is a 32-bit Windows application that make it easy to run the old Word for Word file converters in modern Windows systems. It uses the 1995-era Word for Word for DOS program, briefly released by Adobe in its Adobe File Utilities package, now packaged in a compiled AutoIt script. This package only converts files in formats in use before 1995; do not try to use it with modern formats like DOCX, ODT, Word 2007, etc.

This tool requires the above application to be installed on your system. The path to exe file should be changed on line #250

`location_of_legacyfileconverter_application = r"E:\\tools\\LegacyFileConverter\\source\\LegacyFileConverter.exe"`

The python wrapper uses the tool to try all the converters included in the app. 

When the tool is run, and new folder is created in the same folder as the file being used called `conversions`

Inside this folder, another folder is created called the same as the file name. 

The python tool then takes all the 208 codes recognised by LegacyFileConverter.exe and one by one requests a conversion. If the conversion is successful, a new converted file is created, inside this folder with the original filename prepended by the conversion code. 

There is some "hand holding" needed - vdos can hang a few times per run, the user needs to close the popup window and the python script carries on. 

There was also a minor issue with the original package for LegacyFileConverter.exe as found on the website. even in `/silent` mode the tool was requesting human input for most of the conversions. Working with the oroginal developer, we were able to repackage the tool in such a way that  `/silent` mode is now as expected. This fixed version in included in this repo. To use it, replace the original `LegacyFileConverter.exe` from   http://www.columbia.edu/~em36/legacyfileconverter.html  with the one foind in this repo. 

## How to use it

In python, the path of the file being tested is given to the function `try_all_codes()`.   

If I want to test the file `c:\files\example_file.wri`

When the process has finished, I can visit the folder  `c:\files\conversions\example` and observe the products of any attempted conversions.  

These files are prepended with the trigger code as part of the file name e.g. `123__example.wri.doc`, `ASC__example.wri.doc`, `ASC850__example.wri.doc` etc.

These files can then be opened, and examined. Most will be incorrect conversions. If there is a conversion instance that is useful for further research, the file type / converer used can be looked up via the prepened code. 

AMI - Ami Pro 1.x - 3.1
SDW - Ami Pro Graphics SDW
SAS - ASCII (Smart), PC
SAS850 - ASCII (Smart), PC - CP 850
SASM - ASCII (Smart), MAC
SASX - ASCII (Smart), UNIX
SASW - ASCII (Smart), Windows
ASC - ASCII (Standard), PC
ASC850 - ASCII (Standard), PC - CP 850
ASCM - ASCII (Standard), MAC
ASCX - ASCII (Standard), UNIX
ASCW - ASCII (Standard), Windows
STA - ASCII (Stripped), PC
STA850 - ASCII (Stripped), PC - CP 850
STAM - ASCII (Stripped), MAC
STAX - ASCII (Stripped), UNIX
STAW - ASCII (Stripped), Windows
CSV - ASCII (Comma Delimited), PC
CSVA - ASCII (Comma Delimited), WIN
CSVM - ASCII (Comma Delimited), MAC
CSVX - ASCII (Comma Delimited), UNIX
QSV - ASCII (Comma/Quote Delim), PC
QSVA - ASCII (Comma/Quote Delim), WIN
QSVM - ASCII (Comma/Quote Delim), MAC
QSVX - ASCII (Comma/Quote Delim), UNIX
TSV - ASCII (Tab Delimited), PC
TSVA - ASCII (Tab Delimited), WIN
TSVM - ASCII (Tab Delimited), MAC
TSVX - ASCII (Tab Delimited), UNIX
DXF - AutoCAD (DXF,DXB)
DXF - AutoCAD (DXF)
CEO - CEOwrite 3.0
CLWKS - Claris Works 3.0
COM - Communications Format
GIF - CompuServe GIF
CGM - Computer Graphics Metafile (CGM)
COR - CorelDraw Preview
DEF - CTOS DEF
DEFW - CTOS DEF (Word Processor)
DB4 - DBase IV 1.0
DB3 - DBase III, III+
FFT - DCA/FFT - Final Form Text
RFT - DCA/RFT - Revisable Form Text
RFT2 - DCA/RFT - DisplayWrite 5
DX - Digital DX
WPL - Digital WPS-PLUS
DW5 - DisplayWrite 5
DW - DisplayWrite 2,3,4
EBC - EBCDIC
EN - Enable 1.1, 2.0, 2.15
EPS - Encapsulated PostScript Preview
EPS - Encapsulated PostScript Bitmap
MIF4 - FrameMaker (MIF) 4.0 - 5.0
MIF4W - FrameMaker (MIF) 4.0 - 5.0 Win
MIF4M - FrameMaker (MIF) 4.0 - 5.0 Mac
MIF4X - FrameMaker (MIF) 4.0 - 5.0 Unix
MIF - FrameMaker (MIF) 3.0
MIFW - FrameMaker (MIF) 3.0 Win
MIFM - FrameMaker (MIF) 3.0 Mac
MIFX - FrameMaker (MIF) 3.0 Unix
FW4 - Framework IV
FW3 - Framework III 1.0, 1.1
AWP - HP AdvanceWrite Plus
HPPCL - HP PCL
HPGL - HP Graphics Language (HPGL)
HTML3 - HTML Level 3
HTML2 - HTML Level 2
HTML1 - HTML Level 1
HTML3N - HTML Level 3 – Netscape
HTML2N - HTML Level 2 – Netscape
HTML1N - HTML Level 1 – Netscape
WA - IBM Writing Assistant 1.0
IGES - IGES
ILF6 - Interleaf 6.0
ILF6 - Interleaf 5.2
ILF5 - Interleaf 5.2 - 6.0
INTL - Interleaf Publisher 1.1
JPEG - JPEG
LEG - Legacy 1.x, 2.0
123v4 - Lotus 123 4.0 - 5.0
123v3 - Lotus 123 3.0
123 - Lotus 123 1A, 2.0, 2.1
PRE - Lotus Freelance
MS2 - Lotus Manuscript 2.0, 2.1
LPIC - Lotus PIC
PICT - Macintosh QuickDraw (PICT)
MPAINT - Macintosh Paint
MCWPRO - MacWrite Pro 1.0
MCW2 - MacWrite II, 1.0 - 1.1
MCW - MacWrite 4.5 - 5.0
MASS - Mass 11, Version 8.5 - 9.0
MASS - Mass 11, Version 8.0 - 8.33
MGX - Micrografx Designer (DRW)
ACC2 - MS Access 2.0
XL5 - MS Excel 5.0 - 7.0
XL4 - MS Excel 4.0
XL3 - MS Excel 3.0
XL - MS Excel 2.1
XLM4 - MS Excel Mac 4.0
XLM3 - MS Excel Mac 3.0
FOXW - MS FoxPro for Windows 2.5
RTF - MS RTF
RTFW6 - MS RTF (WinWord 6)
RTFM6 - MS RTF (MacWord 6)
RTF - MS RTF (ANSI Char Set)
RTFINT - MS RTF (Codepage 850)
RTFM - MS RTF (MAC Char Set)
RTFPC - MS RTF (PC Char Set)
MSWW6 - MS Word for Windows 6.0 - 7.0
MSWW2 - MS Word for Windows 2.0
MSWW - MS Word for Windows 1.x
MS6 - MS Word for DOS 6.0
MS5 - MS Word for DOS 5.0, 5.5
MS4 - MS Word for DOS 4.0
MSW - MS Word for DOS 3.0, 3.1
MSWM - MS Word for DOS 5.x (Mail Merge)
MWM6 - MS Word for Mac 6.0
MWM5 - MS Word for Mac 5.0, 5.1
MWM4 - MS Word for Mac 4.0
MWM3 - MS Word for Mac 3.0
MSWK - MS Works for Windows 3.0
MWW - MS Write for Windows 3.x
MM4 - MultiMate 4
MA2 - MultiMate Advantage II
MMA - MultiMate Advantage I
MM - MultiMate 3.3
GSA - Navy DIF (GSA)
DIF - Navy DIF (WordPerfect)
OP7 - OfficePower 7
OP6 - OfficePower 6
OW6 - OfficeWriter 6.0 - 6.2
OW5 - OfficeWriter 5.0
OW4 - OfficeWriter 4.0
OS2B - OS/2 Bitmap
OS2M - OS/2 Metafile
PDX - Paradox 3.5, 4.0
DCX - PC Paintbrush (DCX)
PCX - PC Paintbrush (PCX)
PT - PeachText 5000 2.12
FC3 - PFS:First Choice 3.0
FC2 - PFS:First Choice 2.0
FC - PFS:First Choice 1.0
FC3DB - First Choice 3.0 Data Base
PFS - PFS:WRITE Ver C
PW2 - Professional Write 2.0 - 2.2
PPW - Professional Write 1.0
PWP - Professional Write Plus
PNG - Portable Network Graphics (PNG)
PS - PostScript
QA4 - Q&A 4.0
QA3 - Q&A Write 1.x, Q&A 3.0
QPD - Quattro Pro DOS
QPW - Quattro Pro Windows
RF1 - Rapid File 1.2
RF - Rapid File 1.0
RGIP - RGIP
SW4 - Samna Word IV & IV+ 1.0, 2.0
SIG - Signature 1.0
RAS - Sun Raster Graphics
TIFF - Tagged Image File Format (TIFF)
TW - Total Word 1.2, 1.3
VW3 - Volkswriter 3,4
VW - Volkswriter Deluxe 2.2
V7 - Uniplex V7 - V8
ONGO - Uniplex OnGO
WANG - Wang PC, Version 3
BMP - Windows Bitmap (BMP)
WINCLP - Windows Clipboard (CLP)
WMF - Windows Metafile (WMF)
ICON - Windows ICON
WPAINT2 - Windows Paint 2.x
WRLE - Windows RLE
WIZI - WiziWord
WIZID - WiziDraw
WPW61 - WordPerfect for Windows 6.1
WPW6 - WordPerfect for Windows 6.0
WPW51 - WordPerfect for Windows 5.x
WP6 - WordPerfect 6.0
WP51 - WordPerfect 5.1
WP5 - WordPerfect 5.0
W42 - WordPerfect 4.2
WP4 - WordPerfect 4.1
WPG2 - WordPerfect Graphics 2 (WPG)
WPG - WordPerfect Graphics 1 (WPG)
WPM31 - WordPerfect Mac 3.1 - 3.5
WPM3 - WordPerfect Mac 3.0
WPM21 - WordPerfect Mac 2.1
WPM2 - WordPerfect Mac 2.0
WPM1 - WordPerfect Mac 1.0
WPMM - WordPerfect 5.1 (Mail Merge)
WS7 - WordStar 7.0
WS6 - WordStar 6.0
WS55 - WordStar 5.5
WS5 - WordStar 5.0
WS4 - WordStar 4.0
WS3 - WordStar 3.45
WS - WordStar 3.3, 3.31
WSW - WordStar for Windows
WS2R35 - WordStar 2000, Rel 3.5
WS2R3 - WordStar 2000, Rel 3.0
WNOW3 - WriteNow 3.0
XIF - XEROX - XIF 5.0, 6.0
XIFG - XIF Graphics (Interpress)
XPM - Xwindows PixMap XPM
XYW - XyWrite for Windows
XY4 - XyWrite IV
XYP - XyWrite III Plus
XY3 - XyWrite III
