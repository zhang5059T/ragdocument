from sentence_transformers import SentenceTransformer

from CarRAG.document.document_semantics import document_semantics, document_baai
from CarRAG.utils.read_doc_data import read_file, read_pdf_file, read_pdf_file_split

if __name__ == '__main__':
    questions = read_file('./doc/questions.json')
    pdf_datas = read_pdf_file_split('./doc/初赛训练数据集.pdf')
    document_baai(questions, pdf_datas)
