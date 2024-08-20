from os import getcwd, listdir
from os.path import isfile
from re import search

CWD = getcwd()
CWD_LINUX = CWD.replace("C:", "/mnt/c").replace("\\", "/")
OUTPUT = "output"
DOCX_FILES = [f for f in listdir(CWD) if f.endswith(".docx")]
NEEDED_PDFS = [f"{OUTPUT}/{f.split(".")[0] + ".pdf"}" for f in DOCX_FILES]
PDF_TEMPLATE = f"{OUTPUT}/template.pdf"
XLSX = f"data.xlsx"
TEMPLATE = f"{OUTPUT}/template.html"
METRICS = f"{OUTPUT}/metrics.txt"
PARSER = "html5lib"
ID_TO_AREA = dict([search(r"([0-9|a-zA-Z]+)?\s?([0-9|a-zA-Z]+)?", f).groups(2) for f in listdir(CWD) if f.endswith(".docx")])
XLSX_SERIAL = "Serial #"
XLSX_DATE = "Date"
XLSX_REPORT = "Report #"
CSS_STR = '@page { width: 135%; height: 135%; margin-top: 0.5in; margin-bottom: 0.6in; margin-right: 0.6in; margin-left: 0.6in; font-family: Arial }'