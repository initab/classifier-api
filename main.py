import json
import os

import torch
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer

config_path = os.getenv("CLASSIFY_API_CONF", "config.json")
with open(config_path, "r") as f:
    config = json.load(f)

app = FastAPI(root_path=config["root"])


class Item(BaseModel):
    text: str
    labels: list[str]


tokenizer = AutoTokenizer.from_pretrained(
    pretrained_model_name_or_path=config["model"],
    model_max_length=512,
    use_fast=True,
)

classifier = pipeline(
    "zero-shot-classification",
    model=config["model"],
    device=0 if torch.cuda.is_available() else -1,
    batch_size=8,
    torch_dtype=torch.float16,
    tokenizer=tokenizer,
)


@app.post(config["endpoint"])
async def classify(item: Item):
    hypothesis_template = config["template"]
    results = classifier(
        sequences=item.text,
        candidate_labels=item.labels,
        hypothesis_template=hypothesis_template,
        multi_label=True,
        max_length=512,
    )

    return results
