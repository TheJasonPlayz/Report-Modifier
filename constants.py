from os import getcwd, listdir
from enum import Enum, auto
from re import search

CWD = getcwd()
CWD_LINUX = CWD.replace("C:", "/mnt/c").replace("\\", "/")
OUTPUT = "output"
DOCX = "317301 KRUPA.docx"
PDF = f"{OUTPUT}/317301 KRUPA.pdf"
XLSX = f"data.xlsx"
TEMPLATE = f"{OUTPUT}/template.html"
REPORT = f"{OUTPUT}/report.pdf"
METRICS = f"{OUTPUT}/metrics.txt"
TEMPLATE = f"{OUTPUT}/template.html"
# TEMPLATE_SPLIT = f"{OUTPUT}/template_split.html"
# PDF_SPLIT = PDF.split(".")[0]
# TEMPLATE_SPLIT_PAGES = [f"{OUTPUT}/{f}" for f in listdir(OUTPUT) if search(fr"317301 KRUPA[0-9]+.page", f)]
PARSER = "html5lib"

class PageNums(Enum):
    Single = auto()
    Multiple = auto()
