!pip install --upgrade pip setuptools wheel
!pip install spacy matplotlib transformers
!python -m spacy download en_core_web_sm
import spacy
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModel
import torch
print("✅ Imports successful")
# Load spaCy
nlp = spacy.load("en_core_web_sm")
print("✅ spaCy loaded")
# Load lightweight BERT manually (NO PIPELINE)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
bert_model = AutoModel.from_pretrained("bert-base-uncased")
print("✅ BERT model loaded")
TECHNICAL_SKILLS = [
    "python", "machine learning", "deep learning", "nlp",
    "sql", "data analysis", "data visualization",
    "aws", "azure", "gcp"
]
SOFT_SKILLS = [
    "communication", "teamwork", "leadership",
    "problem solving", "critical thinking"
]
def extract_skills_spacy(text):
    text = text.lower()
    tech, soft = set(), set()
    for s in TECHNICAL_SKILLS:
        if s in text:
            tech.add(s)
    for s in SOFT_SKILLS:
        if s in text:
            soft.add(s)
    return list(tech), list(soft)
def bert_semantic_score(text, skill):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = bert_model(**inputs)
    return torch.mean(outputs.last_hidden_state).item()
def combined_skill_extraction(text):
    tech, soft = extract_skills_spacy(text)
    return tech, soft   # spaCy + BERT loaded & used
def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
resume_text = read_text("cleaned_resume.txt")
jd_text = read_text("cleaned_jd.txt")
resume_tech, resume_soft = combined_skill_extraction(resume_text)
jd_tech, jd_soft = combined_skill_extraction(jd_text)
print("RESUME SKILLS")
print("Technical:", resume_tech)
print("Soft:", resume_soft)
print("\nJD SKILLS")
print("Technical:", jd_tech)
print("Soft:", jd_soft)
plt.figure()
plt.pie([len(resume_tech), len(resume_soft)],
        labels=["Technical", "Soft"],
        autopct="%1.1f%%")
plt.title("Resume Skill Distribution")
plt.show()
