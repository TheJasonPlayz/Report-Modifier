from typing import List, Tuple
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from bs4 import BeautifulSoup, Tag
from pypdf import PdfReader, PdfWriter
# from bs4.diagnose import diagnose

import re
from copy import copy
from socket import gethostname
from importlib import reload

from template_generator import generate_template
from id_finder import getXSLXData, convert_docx
import constants

def modifyReportName(report_n: str):
    area = re.sub("/", ".", constants.ID_TO_AREA.get(str(report_n)))
    return f"{constants.OUTPUT}/{report_n} {area}.pdf"

def cropLogo(pdf_fn):
    output = PdfWriter()
    input = PdfReader(pdf_fn)
    page = input.pages[0]
    page.mediabox.upper_left =  (
        page.mediabox.left - 50,
        page.mediabox.top - 50,
    )
    output.add_page(page)
    for i in range(len(input.pages)):  
        page = input.pages[i]
        output.add_page(page)
    with open(pdf_fn, "wb") as pdf:
        output.write(pdf)

def editTag(target: Tag, template_id: str) -> Tag:
    new_tag = copy(target)
    new_tag.attrs["id"] = "target"
    new_tag.string = "{{" + template_id + "}}"
    return new_tag

def modifyHighHTML(soup: BeautifulSoup) -> BeautifulSoup:
    container = soup.find("div", id="page-container")
    if container:
        parent = container.parent
        if parent:
            pages = soup.find_all("div", id=["pf1", "pf2"])
            if pages:
                parent.extend(copy(pages))
            else:
                raise ValueError("PAGES NOT FOUND")
        else:
            raise ValueError("PARENT NOT FOUND")
    else:
        raise ValueError("CONTAINER NOT FOUND")
        # container.decompose()
    return soup

def modifyLowHTML(soup: BeautifulSoup) -> BeautifulSoup:
    v_id_tags = soup.find_all("span", string=re.compile("# "))
    h_date_tags = soup.find_all("div", string=re.compile("DATE: "))
    f_date_tags = soup.find_all("", string=re.compile(
        "Date "))

    # Modify Vehicle IDs
    for tag in v_id_tags:
        target = tag.parent.parent.next_sibling
        target.replace_with(editTag(target, "v_id"))
    # Modify Header Dates
    for tag in h_date_tags:
        target = tag.next_sibling
        target.replace_with(editTag(target, "h_date"))
    # Modify Footer Date
    if f_date_tags:
        target = f_date_tags[len(f_date_tags) - 1].parent
        new_tag = editTag(target, "f_date")
        new_tag.string = "Date {{f_date}}"
        target.replace_with(new_tag)

    return soup

def modifyHTML(soup: BeautifulSoup):
    soup_mod = modifyHighHTML(soup)
    soup_mod2 = modifyLowHTML(soup_mod)

    with open(TEMPLATE, "w") as t:
        t.write(str(soup_mod2))

def generateReport(id: int, date: str):
    env = Environment(loader=FileSystemLoader(CWD),
                      comment_start_string='{=', comment_end_string="=}")
    template_vars = {
        'v_id': id,
        'h_date': date,
        'f_date': date,
    }
    page_css = CSS(string='@page { width: 135%; height: 135%; }')

    template = env.get_template(TEMPLATE)
    rendered_string = template.render(template_vars)
    report_name = modifyReportName(id)
    HTML(string=rendered_string).write_pdf(
        report_name, stylesheets=[page_css])
    return report_name

(ids, dates) = getXSLXData()

if gethostname() == "JASONS_COMPUTER":
    generate_template(PageNums.Single)

with open(TEMPLATE, "r") as t:
    soup = BeautifulSoup(t, PARSER)
    soup_mod = modifyHTML(soup)

for id, date in zip(ids, dates):
   r = generateReport(id, date)
   cropLogo(r)
