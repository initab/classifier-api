import torch
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer

app = FastAPI(root_path="/api")


class Item(BaseModel):
    text: str
    labels: list[str]


tokenizer = AutoTokenizer.from_pretrained(
    pretrained_model_name_or_path='KBlab/megatron-bert-large-swedish-cased-165-zero-shot',
    model_max_length=512,
    use_fast=True,
)

classifier = pipeline(
    "zero-shot-classification",
    model="KBlab/megatron-bert-large-swedish-cased-165-zero-shot",
    device=0 if torch.cuda.is_available() else -1,
    batch_size=8,
    torch_dtype=torch.float16,
    tokenizer=tokenizer,
)


@app.post("/classify")
async def classify(item: Item):
    hypothesis_template = "Detta exempel handlar om {}."
    results = classifier(
        sequences=item.text,
        candidate_labels=item.labels,
        hypothesis_template=hypothesis_template,
        multi_label=True,
        max_length=512,
    )

    return results
