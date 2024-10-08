import pandas as pd

from constants import XLSX, XLSX_DATE, XLSX_REPORT, XLSX_SERIAL

def getXSLXData() -> list[list[int], list[int], list[str]]:
    xslx = pd.read_excel(XLSX)
    rows = []
    for row in xslx.iloc:
        rows.append([row[XLSX_REPORT], row[XLSX_SERIAL], row[XLSX_DATE]])
    return rows