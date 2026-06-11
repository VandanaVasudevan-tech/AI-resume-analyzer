import torch
import joblib

from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

MODEL_PATH = "resume_classifier"

tokenizer = DistilBertTokenizerFast.from_pretrained(
    MODEL_PATH
)

model = DistilBertForSequenceClassification.from_pretrained(
    MODEL_PATH
)

encoder = joblib.load(
    "label_encoder.pkl"
)


def predict_resume(text):
    inputs = tokenizer(
        text,
        truncation=True,
        padding=True,
        max_length=512,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=1)

    top_probs, top_indices = torch.topk(probs, 5)

    print("\nTop Predictions:")
    for prob, idx in zip(top_probs[0], top_indices[0]):
        label = encoder.inverse_transform([idx.item()])[0]
        print(f"{label}: {prob.item()*100:.2f}%")

    confidence, prediction = torch.max(probs, dim=1)

    category = encoder.inverse_transform(
        [prediction.item()]
    )[0]

    return category, round(confidence.item() * 100, 2)