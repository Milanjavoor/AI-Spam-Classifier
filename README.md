🛡️ Spam Shield
AI-Powered Email Spam Detection & Intelligent Classification System


✨ Features
🤖 Machine Learning
Binary classification of emails into:
🟢 Ham
🔴 Spam
TF-IDF based text representation
Word and n-gram features
Multiple ML algorithms evaluated
Precision, Recall and F1-score based evaluation
Confusion matrix analysis
Best-performing model selection
🧠 NLP

The preprocessing pipeline can perform operations such as:

Lowercasing
Removing unnecessary characters
URL normalization
Number normalization
Punctuation handling
Text tokenization
TF-IDF feature extraction
N-gram generation
🖥️ Desktop Application

The project includes a Tkinter-based GUI where users can:

Paste an email
Analyze the email
Receive a Spam/Ham prediction
View prediction information
Clear the input
Interact with the classifier without writing Python code
📊 Model Evaluation

The project evaluates models using:

Accuracy
Precision
Recall
F1-score
Confusion Matrix



🧪 Dataset

The project uses email examples from the:

Apache SpamAssassin Public Corpus

The dataset contains both legitimate and spam messages.

After processing the dataset, the current dataset contains:

Class	Number of Emails 


🟢 Ham	2,551

🔴 Spam	501
Total	3,052



The dataset is split into training and testing subsets while preserving the class distribution.


1. Data Collection

Spam and legitimate email examples are collected from the Apache SpamAssassin public datasets.

Each email is assigned a label:

0 → Ham
1 → Spam
2. Data Preprocessing

Raw emails contain much more than useful textual information.

For example:

From: john@example.com
Subject: Congratulations!!!

Hello John,

You have WON $10,000!!!
Click here:
https://example.com

The preprocessing stage transforms the raw message into cleaner textual data.




🤖 Models Evaluated

Several classification algorithms were investigated.

1. Multinomial Naive Bayes

A strong baseline for text classification.

TF-IDF / Word Features
        ↓
Naive Bayes
        ↓
Spam / Ham
2. Logistic Regression

A linear classification algorithm that works particularly well with high-dimensional text features.

3. Support Vector Machine

A Support Vector Machine was also evaluated because SVM-based models are often highly effective for sparse, high-dimensional NLP datasets.

🏆 Best Model

For this project, SVM-based classification achieved the strongest overall performance among the evaluated models.

The final model is therefore based on the SVM approach.

📊 Evaluation

The model is evaluated using more than accuracy.

Precision

Precision answers:

Of all emails predicted as spam, how many were actually spam?

Precision = TP / (TP + FP)

High precision means fewer legitimate emails are incorrectly marked as spam.

Recall

Recall answers:

Of all actual spam emails, how many did the model successfully detect?

Recall = TP / (TP + FN)

High recall means fewer spam emails escape detection.

F1 Score

F1-score balances precision and recall.

F1 = 2 × (Precision × Recall)
     --------------------------
       Precision + Recall

For this project, F1-score is especially useful because both false positives and false negatives matter.



The GUI separates the user interface from the underlying ML pipeline.

⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/AIspamclassifier.git

Move into the project:

cd AIspamclassifier
2. Create a virtual environment

Windows:

python -m venv venv

Activate it:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
📦 Requirements

The primary dependencies include:

numpy
pandas
scikit-learn
joblib
matplotlib
seaborn

Tkinter is included with most standard Python installations on Windows.

▶️ Running the Project
Train the model

Run:

python model.py

This performs:

Load Dataset
      ↓
Preprocess
      ↓
Split Data
      ↓
TF-IDF
      ↓
Train Models
      ↓
Evaluate
      ↓
Select Best Model
      ↓
Save Model
Launch the GUI

After the model has been trained:

python app.py

The Spam Shield desktop application will launch.

🧪 Example Predictions
Example 1 — Spam
Subject: Congratulations! You have won!!!

You have been selected to receive $10,000.

Click here immediately to claim your prize.
Limited time offer!!!

Expected:

🚨 SPAM
Example 2 — Ham
Subject: Project Meeting

Hi,

Just confirming that our project meeting is scheduled
for tomorrow at 10 AM.

Regards,
Alex

Expected:

✓ HAM
🛡️ Real-World Considerations

This project is designed for educational and portfolio purposes.

A production-grade spam filtering system would additionally need:

Continuous retraining
Larger and more diverse datasets
Adversarial spam detection
Phishing URL analysis
HTML email analysis
Attachment analysis
Sender reputation
Domain reputation
Header analysis
Real-time threat intelligence
Concept drift monitoring
False-positive management
Model monitoring

Spam evolves continuously, so a real-world classifier must evolve with it.

🚀 Future Improvements

The project can be extended in several directions.

🔹 Advanced NLP
Word embeddings
Word2Vec
GloVe
FastText
Transformer-based embeddings
BERT-based classification
🔹 Advanced Detection
Phishing URL detection
Malicious attachment detection
Email header analysis
Sender/domain reputation
HTML structure analysis
🔹 Machine Learning
Hyperparameter optimization
Cross-validation
Ensemble learning
Probability calibration
Model explainability
🔹 Application
Drag-and-drop .eml files
Email file upload
Batch classification
Prediction history
Statistics dashboard
Export predictions to CSV
Confidence visualization
🔹 Deployment

The application could eventually be converted into:

Tkinter Desktop App
        ↓
Flask / FastAPI
        ↓
REST API
        ↓
Web Application
📈 Learning Outcomes

This project demonstrates practical experience with
Python
File handling
Modules
Functions
Object-oriented concepts
Exception handling
Data Science
Pandas
NumPy
Data cleaning
Dataset exploration
Train/test splitting
NLP
Text preprocessing
Tokenization
Bag-of-Words
TF-IDF
N-grams
Sparse matrices
Machine Learning
Supervised learning
Binary classification
Naive Bayes
Logistic Regression
Support Vector Machines
Model comparison
Hyperparameter selection
Evaluation
Accuracy
Precision
Recall
F1-score
Confusion matrix
Software Development
Model serialization
Modular Python architecture
Tkinter GUI development
Error handling
Project organization
🧠 Key Concepts Demonstrated
NLP
 
 Text Cleaning
 Tokenization
  TF-IDF
 N-Grams
      
  
Machine Learning
 
  Naive Bayes
 Logistic Regression
  SVM
        
        
Evaluation
 
  Precision
 Recall
  F1
 Confusion Matrix
        │
        ▼
Application
 
  Tkinter GUI
 CV / Resume Description
Short Version

Spam Shield — AI Email Spam Classifier
Developed an end-to-end NLP-based spam detection system using TF-IDF and SVM classification on 3,000+ real email samples. Evaluated multiple machine learning algorithms using precision, recall, F1-score, and confusion matrices, and integrated the selected model into a Tkinter desktop application for real-time email classification.

Technical Version

Built an end-to-end email spam classification pipeline using Python, Scikit-learn, TF-IDF, n-gram feature engineering, and Support Vector Machines. Implemented preprocessing, stratified train/test evaluation, model benchmarking, and performance analysis using precision, recall, F1-score, and confusion matrices. Serialized the trained model and integrated it with a Tkinter GUI for interactive spam detection.


📜 Dataset & Attribution

This project uses the publicly available Apache SpamAssassin public email corpus for educational and machine-learning experimentation.

The dataset is not redistributed with this repository.

Please refer to the original dataset source and its applicable terms before using the dataset for other purposes.

⚠️ Disclaimer

Spam Shield is an educational machine-learning project and should not be considered a production-grade email security solution.

Predictions may occasionally be incorrect.

Do not use the classifier as the sole mechanism for deciding whether an email is safe, malicious, or fraudulent.

👨‍💻 Author

Milan Javoor

Computer Science / AI & ML Enthusiast

Interested in:

Artificial Intelligence
Machine Learning
Natural Language Processing
Cybersecurity
Quantum Computing
Deep Learning
⭐ If You Like This Project

If you found this project interesting:

⭐ Star the repository
🍴 Fork the project
🐛 Report issues
💡 Suggest improvements
