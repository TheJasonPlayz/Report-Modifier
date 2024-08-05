from os import getcwd, listdir
from enum import Enum, auto
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

class PageNums(Enum):
    Single = auto()
    Multiple = auto()
