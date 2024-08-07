from os import getcwd, listdir
from re import search

CWD = getcwd()
CWD_LINUX = CWD.replace("C:", "/mnt/c").replace("\\", "/")
OUTPUT = "output"
DOCX_TEMPLATE = "317301 KRUPA.docx"
PDF_TEMPLATE = f"{OUTPUT}/317301 KRUPA.pdf"
XLSX = f"data.xlsx"
TEMPLATE = f"{OUTPUT}/template.html"
METRICS = f"{OUTPUT}/metrics.txt"
PARSER = "html5lib"
DOCX_FILES = [f for f in listdir() if f.endswith(".docx")]
ID_TO_AREA = dict([search(r"([0-9|a-zA-Z]+)?\s?([0-9|a-zA-Z]+)?", f).groups(2) for f in listdir(f"{OUTPUT}/") if f.endswith(".docx") or f.endswith(".pdf")])
XLSX_SERIAL = "Serial #"
XLSX_DATE = "Date"
XLSX_REPORT = "Report #"