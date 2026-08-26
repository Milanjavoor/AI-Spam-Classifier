import tkinter as tk 
import joblib
from tkinter import messagebox
from preproccesing import clean_text

import joblib
#----------------------------Model and Tokenizer loading -------------------------------------------------------------------------------------------
model=joblib.load("Spam_model.pkl")
vectorizer=joblib.load("Vectorizer.pkl")


#-------------------------------------------------------------------Colours ------------------------------------------------------------------------

bg_color="#0f0f1a"
card_color="#181827"
text_color="#ffffff"
accent_color="#8b5cf6"
success="#22c55e"
failure="#ef4444"

#----------------------------------------------- Main window ---------------------------------------------------------------------------------------

root=tk.Tk()
root.title("Spam Sheil - AI Email Classifier")
root.geometry("800x600")
root.resizable(False,False)
root.config(bg=bg_color)

title_label=tk.Label(root,
                     text="SPAM SHIELD",font=("Segoe UI",28,"bold"),bg=bg_color,fg=accent_color)
title_label.pack(pady=(30,5))

email_text=tk.Text(root,height=12,
                   width=80,font=("Consolas",12),bg=card_color,fg=text_color,
                   insertbackground=text_color,relief="flat",padx=15,pady=15)
email_text.pack(padx=40,pady=10)


#------------------------------------------------------ Result desplay --------------------------------------------------------------

result_label=tk.Label(root,text="Prediction will appear here",font=("Segoe UI",18,"bold"),bg=bg_color,fg=text_color)
result_label.pack(pady=15)


#------------------------------------------------ Prediction function  and Clear function----------------------------------------------------------------

def predict_email():
    email=email_text.get("1.0",tk.END)
    if not email.strip():
        messagebox.showwarning("Empty email","You have not given any email text for classification please recheck")
        return
    cleaned_email=clean_text(email)
    features=vectorizer.transform([cleaned_email])
    prediction=model.predict(features)[0]
    if prediction==1:
        result_label.config(text="SPAM DETECTED",fg=failure)
    else:
        result_label.config(text="NOT SPAM",fg=success)

def clear_email():
    email_text.delete("1.0",tk.END)
    result_label.config(text="Prediction will appear here ",fg=text_color)

#------------------------------------ Analyse and clear text buttons --------------------------------------------------------------

analyse_email=tk.Button(root,text="Analyse email",command=predict_email,font=("Seguo UI",12,"bold"),
                        bg=accent_color,fg="white",activeforeground="white",activebackground="#7c3aed",
                        relief="flat",pady=10,padx=30,
                        cursor="hand2")
analyse_email.pack(pady=5)

clear_button=tk.Button(root,text="Clear text",command=clear_email,font=("Seguo UI",10),fg=text_color,bg=card_color,
                       activebackground="#25253a",
                       activeforeground="white",relief="flat"
                       ,pady=5,padx=25,cursor="hand2")
clear_button.pack(pady=5)

#----------------------------------------- Run application ---------------------------------------------------------------------------

root.mainloop()