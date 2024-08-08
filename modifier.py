from jinja2 import Environment, FileSystemLoader
from pypdf import PdfWriter, PdfReader
from weasyprint import HTML, CSS
from docx2pdf import convert

from os.path import isfile
from re import sub
from socket import gethostname
from importlib import reload

from template_generator import generate_template
from id_finder import getXSLXData
import constants
            
def modifyReportName(report_n: int):
    area = sub("/", ".", constants.ID_TO_AREA.get(str(report_n)))
    return f"{constants.OUTPUT}/{report_n} {area}.pdf"

def modifyReport(pdf_fn):
    output = PdfWriter()
    input = PdfReader(pdf_fn)
    
    first = input.pages[0]
    first.mediabox.upper_left = (
        first.mediabox.left + 25,
        first.mediabox.top - 75,
    )
    output.add_page(first)
    
    for i in range(1, len(input.pages)):  
        page = input.pages[i]
        output.add_page(page)
        
    with open(pdf_fn, "wb") as pdf:
        output.write(pdf)

def generateReport(report_n: int, id: int, date: str):
    env = Environment(loader=FileSystemLoader(constants.CWD),
                      comment_start_string='{=', comment_end_string="=}")
    template_vars = {
        'v_id': id,
        'h_date': date,
        'f_date': date,
    }
    page_css = CSS(string='@page { width: 135%; height: 135%; margin-top: 0.5in; margin-bottom: 0.6in; margin-right: 0.6in; margin-left: 0.6in; }')

    template = env.get_template(constants.TEMPLATE)
    rendered_string = template.render(template_vars)
    report_name = modifyReportName(report_n)
    HTML(string=rendered_string).write_pdf(
        report_name, stylesheets=[page_css])
    return report_name


def main():
    if gethostname() == "JASONS_COMPUTER":
        generate_template()
        
    with open(constants.TEMPLATE, "r") as t:
        soup = BeautifulSoup(t, constants.PARSER)
        modifyHTML(soup)


    reload(constants)
    for nested in getXSLXData():
        report_n = nested[0]
        id = nested[1]
        date = nested[2]
        r = generateReport(report_n, id, date)
        cropReport(r)
        
main()