from transformers import AutoModel, AutoTokenizer

model_name = "BAAI/bge-small-zh-v1.5"  # 模型的名称或标识符
output_dir = "../huggingface/BAAI/bge-small-zh-v1.5/"  # 模型保存的本地路径

# 下载模型
model = AutoModel.from_pretrained(model_name)

# 下载标记器
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 将模型和标记器保存到本地
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)