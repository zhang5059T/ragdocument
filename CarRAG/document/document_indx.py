"""
文本检索
"""
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize


def document_index(questions, pdf_contents):
    question_words = [' '.join(jieba.lcut(x['question'])) for x in questions]
    pdf_content_words = [' '.join(jieba.lcut(x['content'])) for x in pdf_contents]
    tfidf = TfidfVectorizer()
    tfidf.fit(question_words+pdf_content_words)

    # 提取TFIDF
    question_feat = tfidf.transform(question_words)
    pdf_content_feat = tfidf.transform(pdf_content_words)
    question_feat = normalize(question_feat)
    pdf_content_feat = normalize(pdf_content_feat)

    # 检索进行排序
    for query_idx, feat in enumerate(question_feat):
        score = feat @ pdf_content_feat.T
        score = score.toarray()[0]
        max_score_page_idx = score.argsort()[-1]+1
        questions[query_idx]['reference'] = f'page_{max_score_page_idx}'

    print(questions)
