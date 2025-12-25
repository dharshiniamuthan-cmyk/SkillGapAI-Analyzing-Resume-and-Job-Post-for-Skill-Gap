install python-docx ipywidgets
import io
import re
from docx import Document
import ipywidgets as widgets
from IPython.display import display
upload = widgets.FileUpload(
    accept='.docx',
    multiple=False
)

display(upload)
def extract_text_from_upload(upload_widget):
    # upload_widget.value is a tuple in latest ipywidgets
    uploaded_file = upload_widget.value[0]
    
    file_content = uploaded_file['content']
    
    # Read DOCX from memory
    doc = Document(io.BytesIO(file_content))
    
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
        
    return text
extracted_text = extract_text_from_upload(upload)

print("----- Extracted Text from Uploaded DOCX Resume -----\n")
print(extracted_text)
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)   # remove extra spaces & line breaks
    text = text.strip()
    return text

cleaned_text = clean_text(extracted_text)

print("----- Cleaned & Normalised Text -----\n")
print(cleaned_text)
print("========== DOCX RESUME PREVIEW ==========\n")
print(cleaned_text)
with open("cleaned_resume.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Cleaned resume saved as cleaned_resume.txt")
