import pandas as pd
from docx2pdf import convert

from os import listdir
from os.path import isfile
from re import search

from constants import XLSX, DOCX_FILES, OUTPUT

def getXSLXData() -> list[list[int], list[int], list[str]]:
    xslx = pd.read_excel(XLSX)
    rows = []
    for row in xslx.iloc:
        rows.append([row["Report #"], row["Serial #"], row["Date"]])
    return rows