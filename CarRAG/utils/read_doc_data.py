import pdfplumber
import json


def read_file(file_name):
    data = json.loads(open(file_name, encoding='utf-8').read())
    return data


def split_text_fixed_size(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def read_pdf_file_split(file_name):
    data = []
    pdf = pdfplumber.open(file_name)
    for page_index in range(len(pdf.pages)):
        text = pdf.pages[page_index].extract_text()
        for index, chunk_txt in enumerate(split_text_fixed_size(text, 40)):
            data.append({
                'page': f'page_{page_index + 1}',
                'content': chunk_txt,
                'segment': index
            })

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
