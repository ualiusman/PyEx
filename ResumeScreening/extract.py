import fitz
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# load stopwords
stop_words = set(stopwords.words('english'))

doc = fitz.open("cv1.pdf")
jd = fitz.open("jd.pdf")

full_text = ""
jd_text = ""

for page_num_jd in range(jd.page_count):
    page = jd[page_num_jd]
    text = page.get_text()
    jd_text += text


for page_num in range(doc.page_count):
    page = doc[page_num]
    text = page.get_text()
    full_text += text

clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', full_text)
words = clean_text.split()
filtered_words = [word for word in words if word not in stop_words]
clean_text = " ".join(filtered_words)
tokens = word_tokenize(clean_text)


cv_embedding = model.encode(full_text, convert_to_tensor=True)
job_embedding = model.encode(jd_text, convert_to_tensor=True)

similarity = util.cos_sim(cv_embedding, job_embedding)

print(tokens)
print("Similarity Score:", similarity.item())