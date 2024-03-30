from CarRAG.document_index.document_indx import document_index
from CarRAG.utils.read_doc_data import read_file, read_pdf_file

if __name__ == '__main__':
    questions = read_file('./doc/questions.json')
    pdf_datas = read_pdf_file('./doc/初赛训练数据集.pdf')
    document_index(questions, pdf_datas)