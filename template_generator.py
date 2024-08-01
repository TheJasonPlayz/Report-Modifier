from enum import Enum, auto
from docx2pdf import convert

from re import search
from os import listdir
from os.path import isfile
from subprocess import run
from shutil import move

# from constants import TEMPLATE_SPLIT, TEMPLATE_SPLIT_PAGES
from constants import PDF, DOCX, TEMPLATE, CWD_LINUX, OUTPUT, PageNums

def generate_template(pages: PageNums):
    if not isfile(PDF):
        convert(DOCX, PDF)
    if not isfile(TEMPLATE) and pages == PageNums.Single:
        run(["kali", "run", f'cd {CWD_LINUX}; pdf2htmlEX \"{PDF}\" {TEMPLATE}'], shell=True)
