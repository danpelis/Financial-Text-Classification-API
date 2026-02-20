from transformers import AutoConfig

MODEL_NAME = "facebook/bart-large-mnli"
config = AutoConfig.from_pretrained(MODEL_NAME)
MAX_LENGTH = config.max_position_embeddings