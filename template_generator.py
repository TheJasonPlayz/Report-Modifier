from enum import Enum, auto
from docx2pdf import convert

from re import search
from os import listdir
from os.path import isfile
from subprocess import run
from shutil import move

# from constants import TEMPLATE_SPLIT, TEMPLATE_SPLIT_PAGES
from constants import PDF_TEMPLATE, DOCX_FILES, TEMPLATE, CWD_LINUX, OUTPUT

def generate_template():
    if not isfile(TEMPLATE):
        run(["kali", "run", f'cd {CWD_LINUX}; pdf2htmlEX \"{PDF_TEMPLATE}\" {TEMPLATE}'], shell=True)
        
def convert_docx():
    needed_files = [f for f in DOCX_FILES if isfile(f)]
    for file in needed_files:
        convert(file, f"{OUTPUT}/{file.split(".")[0]}.pdf")