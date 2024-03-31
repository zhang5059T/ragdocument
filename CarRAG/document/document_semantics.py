from sentence_transformers import SentenceTransformer


def document_semantics(questions, pdf_contents):
    model = SentenceTransformer("./huggingface/moka-ai/m3e-small/")
    question_words = [x['question'] for x in questions]
    pdf_content_words = [x['content'] for x in pdf_contents]
    question_emb = model.encode(question_words, normalize_embeddings=True)
    pdf_content_emb = model.encode(pdf_content_words, normalize_embeddings=True)

    # 检索进行排序
    for query_idx, feat in enumerate(question_emb):
        score = feat @ pdf_content_emb.T
        max_score_page_idx = score.argsort()[-1] + 1
        questions[query_idx]['reference'] = f'page_{max_score_page_idx}'

    print(questions)


def document_baai(questions, pdf_contents):
    model = SentenceTransformer("./huggingface/BAAI/bge-small-zh-v1.5//")
    question_words = [x['question'] for x in questions]
    pdf_content_words = [x['content'] for x in pdf_contents]
    question_emb = model.encode(question_words, normalize_embeddings=True, show_progress_bar=True)
    pdf_content_emb = model.encode(pdf_content_words, normalize_embeddings=True, show_progress_bar=True)

    # 检索进行排序
    for query_idx, feat in enumerate(question_emb):
        score = feat @ pdf_content_emb.T
        max_score_page_idx = score.argsort()[-1]
        questions[query_idx]['reference'] = pdf_contents[max_score_page_idx]["page"]
        questions[query_idx]['segment'] = pdf_contents[max_score_page_idx]["segment"]

    print(questions)
