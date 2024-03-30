import pdfplumber
import json


def read_file(file_name):
    data = json.loads(open(file_name, encoding='utf-8').read())
    return data


def read_pdf_file(file_name):
    data = []
    pdf = pdfplumber.open(file_name)
    for page_index in range(len(pdf.pages)):
        data.append({
            'page': f'page_{page_index + 1}',
            'content': pdf.pages[page_index].extract_text(),
        })

    return data
