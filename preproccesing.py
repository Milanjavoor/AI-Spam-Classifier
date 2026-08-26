import re
import string
from bs4 import BeautifulSoup
def clean_text(text):
    text=text.lower()
    soup=BeautifulSoup(text,"html.parser")
    text=soup.get_text(" ")
    text=re.sub(r"https?://\S+|www\.\S+"," URL ",text)
    text=re.sub(r"\b\d+(?:[.,]\d+)?\b",
                " NUMBER ",text)
    text=re.sub(r"\s+"," ",text)
    text=text.translate(str.maketrans("","",string.punctuation))
    return text

    