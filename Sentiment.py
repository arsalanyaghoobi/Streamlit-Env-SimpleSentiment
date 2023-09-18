import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification

dir = 'Sentiment'
tokenizer = RobertaTokenizer.from_pretrained(dir)
model = RobertaForSequenceClassification.from_pretrained(dir, num_labels=6)
label_map = {0:'Joyful', 1:'Scared', 2:'Sad', 3:'Neutral', 4:'Excited', 5:'Mad'}

def sentiment(data):
    encodes = tokenizer.encode(data, return_tensors='pt')
    out = model(encodes)
    preds = torch.argmax(out.logits, dim=1)
    label = label_map[preds.item()]
    return label
