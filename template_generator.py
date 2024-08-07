from docx2pdf import convert

from os.path import isfile
from subprocess import run

# from constants import TEMPLATE_SPLIT, TEMPLATE_SPLIT_PAGES
from constants import PDF_TEMPLATE, DOCX_FILES, TEMPLATE, CWD_LINUX, OUTPUT

def generate_template():
    if not isfile(TEMPLATE):
        run(["kali", "run", f'cd {CWD_LINUX}; pdf2htmlEX \"{PDF_TEMPLATE}\" {TEMPLATE}'], shell=True)