from pathlib import Path
import tarfile
import pandas as pd 
import matplotlib.pyplot as plt 
from preproccesing import clean_text
project_dir=Path(__file__).resolve().parent.parent
raw_data=project_dir/ "AIspamclassifier" /"datasets" 
print("Project directory:",project_dir)
print("Datasets directory:",raw_data)
for file in raw_data.iterdir():
    print(file.name)
print("THe files are found...")

def extract_file(extract_loc,output_dir):
    with tarfile.open(extract_loc,"r:bz2") as archieve:
        archieve.extractall(output_dir)
spam_archieve=raw_data/"spam.tar.bz2"
ham_archieve=raw_data/"easy_ham.tar.bz2"

ham_dir=raw_data/"easy_ham"
spam_dir=raw_data/"spam"

if not ham_dir.exists:
    extract_file(ham_archieve,ham_dir)
if not spam_dir.exists:
    extract_file(spam_archieve,spam_dir)

ham_files=list(ham_dir.iterdir())
spam_files=list(spam_dir.iterdir())

sample_email=ham_files[0]
with open(sample_email,"r",encoding="latin1") as file:
    info=file.read()
print(info)

print("the number of ham emails ",len(ham_files))
print("The number of spam emails :",len(spam_files))

def load_emails(folderpath,label):
    emails=[]
    for file_path in folderpath.iterdir():
        with open(file_path,"r",encoding="latin1") as file:
            email_text=file.read()
        emails.append({
            "email":email_text,
            "label":label
        })
    return emails
ham_data=load_emails(ham_dir,0)
spam_data=load_emails(spam_dir,1)

all_data=ham_data+spam_data
df=pd.DataFrame(all_data)
print(df.shape)
print(df["label"].value_counts())

print(df.isnull().sum())
print(df.info())

df["label"].value_counts().plot(kind="bar")
plt.title("Spam vs Ham emails ")
plt.ylabel("Number of emails ")
plt.xlabel("label")
plt.xticks([0,1],["Ham","Spam"],rotation=0)
plt.show()

df["Email_length"]=df["email"].apply(len)
print(df.groupby("label")["Email_length"].mean())

print("An example for a spam email")
print(df[df["label"]==1]["email"].iloc[0])

print("An example for a Ham email")
print(df[df["label"]==0]["email"].iloc[0])

df["has_html"]=df["email"].str.contains(
    r"<html|<body|<div|<table",
    case=False,
    regex=True,
    na=False
)
print(df["has_html"].value_counts())

print(
    pd.crosstab(
        df["has_html"],df["label"],
        normalize="index"
    )
)

df["url_count"]=df["email"].str.count(
    r"https?://|www\."
)
print(df["url_count"].describe())

df["clean_email"]=df["email"].apply(clean_text)

sample=df.iloc[0]
#---------------------------- Before cleaning ---------------------------------------------------------------------------------------------------------

print(sample["email"])

#----------------------------------------------------- After cleaning ----------------------------------------------------------------------------------

print(sample["clean_email"])

