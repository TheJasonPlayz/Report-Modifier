from bs4 import BeautifulSoup, Tag
from docx2pdf import convert

from os.path import isfile
from subprocess import run
from copy import copy
import re

from constants import PDF_TEMPLATE, TEMPLATE, CWD_LINUX, PARSER, DOCX_FILES

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

def removeLogo(soup: BeautifulSoup) -> BeautifulSoup:
    logo_div = soup.find("div", class_="loading-indicator")
    if logo_div:
        new_div = soup.new_tag("div", class_="loading-indicator")
        logo_div.replace_with(new_div)
    else:
        raise ValueError("LOGO NOT FOUND")
    return soup

def modify_template(soup: BeautifulSoup):
    soup_mod = modifyHighHTML(soup)
    soup_mod2 = modifyLowHTML(soup_mod)
    soup_mod3 = removeLogo(soup_mod2)

    with open(TEMPLATE, "w") as t:
        t.write(str(soup_mod3))
    
        
def generate_template():
    if not isfile(PDF_TEMPLATE):
        convert(DOCX_FILES[0], PDF_TEMPLATE)
    if not isfile(TEMPLATE):
        run(["kali", "run", f'cd {CWD_LINUX}; pdf2htmlEX \"{PDF_TEMPLATE}\" {TEMPLATE}'], shell=True)
        
        with open(TEMPLATE, "r") as t:
            soup = BeautifulSoup(t, PARSER)
            modify_template(soup)
            
generate_template()