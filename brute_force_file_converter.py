import subprocess
import os
import shutil

codes = {"Ami Pro 1.x - 3.1":"AMI",
            "Ami Pro Graphics SDW":"SDW",
            "ASCII (Smart), PC":"SAS",
            "ASCII (Smart), PC - CP 850":"SAS850",
            "ASCII (Smart), MAC":"SASM",
            "ASCII (Smart), UNIX":"SASX",
            "ASCII (Smart), Windows":"SASW",
            "ASCII (Standard), PC":"ASC",
            "ASCII (Standard), PC - CP 850":"ASC850",
            "ASCII (Standard), MAC":"ASCM",
            "ASCII (Standard), UNIX":"ASCX",
            "ASCII (Standard), Windows":"ASCW",
            "ASCII (Stripped), PC":"STA",
            "ASCII (Stripped), PC - CP 850":"STA850",
            "ASCII (Stripped), MAC":"STAM",
            "ASCII (Stripped), UNIX":"STAX",
            "ASCII (Stripped), Windows":"STAW",
            "ASCII (Comma Delimited), PC":"CSV",
            "ASCII (Comma Delimited), WIN":"CSVA",
            "ASCII (Comma Delimited), MAC":"CSVM",
            "ASCII (Comma Delimited), UNIX":"CSVX",
            "ASCII (Comma/Quote Delim), PC":"QSV",
            "ASCII (Comma/Quote Delim), WIN":"QSVA",
            "ASCII (Comma/Quote Delim), MAC":"QSVM",
            "ASCII (Comma/Quote Delim), UNIX":"QSVX",
            "ASCII (Tab Delimited), PC":"TSV",
            "ASCII (Tab Delimited), WIN":"TSVA",
            "ASCII (Tab Delimited), MAC":"TSVM",
            "ASCII (Tab Delimited), UNIX":"TSVX",
            "AutoCAD (DXF,DXB)":"DXF",
            "AutoCAD (DXF)":"DXF",
            "CEOwrite 3.0":"CEO",
            "Claris Works 3.0":"CLWKS",
            "Communications Format":"COM",
            "CompuServe GIF":"GIF",
            "Computer Graphics Metafile (CGM)":"CGM",
            "CorelDraw Preview":"COR",
            "CTOS DEF":"DEF",
            "CTOS DEF (Word Processor)":"DEFW",
            "DBase IV 1.0":"DB4",
            "DBase III, III+":"DB3",
            "DCA/FFT - Final Form Text":"FFT",
            "DCA/RFT - Revisable Form Text":"RFT",
            "DCA/RFT - DisplayWrite 5":"RFT2",
            "Digital DX":"DX",
            "Digital WPS-PLUS":"WPL",
            "DisplayWrite 5":"DW5",
            "DisplayWrite 2,3,4":"DW",
            "EBCDIC":"EBC",
            "Enable 1.1, 2.0, 2.15":"EN",
            "Encapsulated PostScript Preview":"EPS",
            "Encapsulated PostScript Bitmap":"EPS",
            "FrameMaker (MIF) 4.0 - 5.0":"MIF4",
            "FrameMaker (MIF) 4.0 - 5.0 Win":"MIF4W",
            "FrameMaker (MIF) 4.0 - 5.0 Mac":"MIF4M",
            "FrameMaker (MIF) 4.0 - 5.0 Unix":"MIF4X",
            "FrameMaker (MIF) 3.0":"MIF",
            "FrameMaker (MIF) 3.0 Win":"MIFW",
            "FrameMaker (MIF) 3.0 Mac":"MIFM",
            "FrameMaker (MIF) 3.0 Unix":"MIFX",
            "Framework IV":"FW4",
            "Framework III 1.0, 1.1":"FW3",
            "HP AdvanceWrite Plus":"AWP",
            "HP PCL":"HPPCL",
            "HP Graphics Language (HPGL)":"HPGL",
            "HTML Level 3":"HTML3",
            "HTML Level 2":"HTML2",
            "HTML Level 1":"HTML1",
            "HTML Level 3 – Netscape":"HTML3N",
            "HTML Level 2 – Netscape":"HTML2N",
            "HTML Level 1 – Netscape":"HTML1N",
            "IBM Writing Assistant 1.0":"WA",
            "IGES":"IGES",
            "Interleaf 6.0":"ILF6",
            "Interleaf 5.2":"ILF6",
            "Interleaf 5.2 - 6.0":"ILF5",
            "Interleaf Publisher 1.1":"INTL",
            "JPEG":"JPEG",
            "Legacy 1.x, 2.0":"LEG",
            "Lotus 123 4.0 - 5.0":"123v4",
            "Lotus 123 3.0":"123v3",
            "Lotus 123 1A, 2.0, 2.1":"123",
            "Lotus Freelance":"PRE",
            "Lotus Manuscript 2.0, 2.1":"MS2",
            "Lotus PIC":"LPIC",
            "Macintosh QuickDraw (PICT)":"PICT",
            "Macintosh Paint":"MPAINT",
            "MacWrite Pro 1.0":"MCWPRO",
            "MacWrite II, 1.0 - 1.1":"MCW2",
            "MacWrite 4.5 - 5.0":"MCW",
            "Mass 11, Version 8.5 - 9.0":"MASS",
            "Mass 11, Version 8.0 - 8.33":"MASS",
            "Micrografx Designer (DRW)":"MGX",
            "MS Access 2.0":"ACC2",
            "MS Excel 5.0 - 7.0":"XL5",
            "MS Excel 4.0":"XL4",
            "MS Excel 3.0":"XL3",
            "MS Excel 2.1":"XL",
            "MS Excel Mac 4.0":"XLM4",
            "MS Excel Mac 3.0":"XLM3",
            "MS FoxPro for Windows 2.5":"FOXW",
            "MS RTF":"RTF",
            "MS RTF (WinWord 6)":"RTFW6",
            "MS RTF (MacWord 6)":"RTFM6",
            "MS RTF (ANSI Char Set)":"RTF",
            "MS RTF (Codepage 850)":"RTFINT",
            "MS RTF (MAC Char Set)":"RTFM",
            "MS RTF (PC Char Set)":"RTFPC",
            "MS Word for Windows 6.0 - 7.0":"MSWW6",
            "MS Word for Windows 2.0":"MSWW2",
            "MS Word for Windows 1.x":"MSWW",
            "MS Word for DOS 6.0":"MS6",
            "MS Word for DOS 5.0, 5.5":"MS5",
            "MS Word for DOS 4.0":"MS4",
            "MS Word for DOS 3.0, 3.1":"MSW",
            "MS Word for DOS 5.x (Mail Merge)":"MSWM",
            "MS Word for Mac 6.0":"MWM6",
            "MS Word for Mac 5.0, 5.1":"MWM5",
            "MS Word for Mac 4.0":"MWM4",
            "MS Word for Mac 3.0":"MWM3",
            "MS Works for Windows 3.0":"MSWK",
            "MS Write for Windows 3.x":"MWW",
            "MultiMate 4":"MM4",
            "MultiMate Advantage II":"MA2",
            "MultiMate Advantage I":"MMA",
            "MultiMate 3.3":"MM",
            "Navy DIF (GSA)":"GSA",
            "Navy DIF (WordPerfect)":"DIF",
            "OfficePower 7":"OP7",
            "OfficePower 6":"OP6",
            "OfficeWriter 6.0 - 6.2":"OW6",
            "OfficeWriter 5.0":"OW5",
            "OfficeWriter 4.0":"OW4",
            "OS/2 Bitmap":"OS2B",
            "OS/2 Metafile":"OS2M",
            "Paradox 3.5, 4.0":"PDX",
            "PC Paintbrush (DCX)":"DCX",
            "PC Paintbrush (PCX)":"PCX",
            "PeachText 5000 2.12":"PT",
            "PFS:First Choice 3.0":"FC3",
            "PFS:First Choice 2.0":"FC2",
            "PFS:First Choice 1.0":"FC",
            "First Choice 3.0 Data Base":"FC3DB",
            "PFS:WRITE Ver C":"PFS",
            "Professional Write 2.0 - 2.2":"PW2",
            "Professional Write 1.0":"PPW",
            "Professional Write Plus":"PWP",
            "Portable Network Graphics (PNG)":"PNG",
            "PostScript":"PS",
            "Q&A 4.0":"QA4",
            "Q&A Write 1.x, Q&A 3.0":"QA3",
            "Quattro Pro DOS":"QPD",
            "Quattro Pro Windows":"QPW",
            "Rapid File 1.2":"RF1",
            "Rapid File 1.0":"RF",
            "RGIP":"RGIP",
            "Samna Word IV & IV+ 1.0, 2.0":"SW4",
            "Signature 1.0":"SIG",
            "Sun Raster Graphics":"RAS",
            "Tagged Image File Format (TIFF)":"TIFF",
            "Total Word 1.2, 1.3":"TW",
            "Volkswriter 3,4":"VW3",
            "Volkswriter Deluxe 2.2":"VW",
            "Uniplex V7 - V8":"V7",
            "Uniplex OnGO":"ONGO",
            "Wang PC, Version 3":"WANG",
            "Windows Bitmap (BMP)":"BMP",
            "Windows Clipboard (CLP)":"WINCLP",
            "Windows Metafile (WMF)":"WMF",
            "Windows ICON":"ICON",
            "Windows Paint 2.x":"WPAINT2",
            "Windows RLE":"WRLE",
            "WiziWord":"WIZI",
            "WiziDraw":"WIZID",
            "WordPerfect for Windows 6.1":"WPW61",
            "WordPerfect for Windows 6.0":"WPW6",
            "WordPerfect for Windows 5.x":"WPW51",
            "WordPerfect 6.0":"WP6",
            "WordPerfect 5.1":"WP51",
            "WordPerfect 5.0":"WP5",
            "WordPerfect 4.2":"W42",
            "WordPerfect 4.1":"WP4",
            "WordPerfect Graphics 2 (WPG)":"WPG2",
            "WordPerfect Graphics 1 (WPG)":"WPG",
            "WordPerfect Mac 3.1 - 3.5":"WPM31",
            "WordPerfect Mac 3.0":"WPM3",
            "WordPerfect Mac 2.1":"WPM21",
            "WordPerfect Mac 2.0":"WPM2",
            "WordPerfect Mac 1.0":"WPM1",
            "WordPerfect 5.1 (Mail Merge)":"WPMM",
            "WordStar 7.0":"WS7",
            "WordStar 6.0":"WS6",
            "WordStar 5.5":"WS55",
            "WordStar 5.0":"WS5",
            "WordStar 4.0":"WS4",
            "WordStar 3.45":"WS3",
            "WordStar 3.3, 3.31":"WS",
            "WordStar for Windows":"WSW",
            "WordStar 2000, Rel 3.5":"WS2R35",
            "WordStar 2000, Rel 3.0":"WS2R3",
            "WriteNow 3.0":"WNOW3",
            "XEROX - XIF 5.0, 6.0":"XIF",
            "XIF Graphics (Interpress)":"XIFG",
            "Xwindows PixMap XPM":"XPM",
            "XyWrite for Windows":"XYW",
            "XyWrite IV":"XY4",
            "XyWrite III Plus":"XYP",
            "XyWrite III":"XY3"}

def call_subprocess(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    if err:
        print (err)

def try_all_codes(my_f):
    root, f_name = my_f.rsplit(os.sep, 1)
    try:
        f_name_only, ext = f_name.rsplit(".", 1)
    except:
        f_name_only = f_name

    outfolder  = os.path.join(root, "conversions", f_name_only)
    temp_infile = os.path.join(outfolder, f_name)
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)
    if not os.path.exists(temp_infile):
        shutil.copy(my_f, outfolder)

    for i, (name, code) in enumerate(codes.items(), 1):
        temp_infile_with_code = os.path.join(outfolder, f"{code}__"+f_name)
        print (f"{i}/{len(codes)} - {name} - {code}")
        if not os.path.exists(temp_infile_with_code):
            os.rename(temp_infile, temp_infile_with_code)
        cmd = f"{location_of_legacyfileconverter_application} {temp_infile_with_code} /input={code} /silent"  
        call_subprocess(cmd)
        if not os.path.exists(temp_infile):
            os.rename(temp_infile_with_code, temp_infile)
    
    if os.path.exists(temp_infile):
        os.remove(temp_infile)

    if os.path.exists(temp_infile_with_code):
        os.remove(temp_infile_with_code)

location_of_legacyfileconverter_application = r"E:\\tools\\LegacyFileConverter\\source\\LegacyFileConverter.exe" 

### single file
my_f = r"E:\testSet\x-fmt_261\V1-FL965240"
my_f = r"c:\files\example.wri"
try_all_codes(my_f)


# ### all files in a folder
# folder = r"E:\testSet\x-fmt_114"
# for f in [os.path.join(folder, x) for x in os.listdir(folder) if os.path.isfile(os.path.join(folder, x)) ]:
#     print (f)
#     print ()
#     try_all_codes(f)

