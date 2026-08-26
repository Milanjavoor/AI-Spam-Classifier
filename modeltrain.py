from sklearn.feature_extraction.text import TfidfVectorizer
from dataloader import df
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,ConfusionMatrixDisplay,confusion_matrix
import matplotlib.pyplot as plt
import joblib
# TEST CASE 1 :
# vectorizer=CountVectorizer()
vectorizer=TfidfVectorizer(ngram_range=(1,2),
                           max_features=50000,min_df=2)
#------------------------------------------ creating two features target and input--------------------------------------------------
x=df["clean_email"]
y=df["label"]

#----------------------------------------spliting data into test and train -------------------------------------------------------
x_train,x_text,y_train,y_test=train_test_split(x,y,test_size=0.2,
                                               random_state=42,stratify=y)

x_train_vectorized=vectorizer.fit_transform(x_train)
x_test_vectorized=vectorizer.transform(x_text)

print(x_train_vectorized.shape)

#------------------------------------------------------model fitting----------------------------------------------------------------------------------

model1=MultinomialNB()

model1.fit(x_train_vectorized,y_train)

y_pred=model1.predict(x_test_vectorized)

accuracy=accuracy_score(y_pred,y_test)

print("The accuracy of the naive bayes model is :",accuracy)

print(
    classification_report(y_pred,y_test,target_names=["Ham","Spam"])
)
cm=confusion_matrix(y_pred,y_test)
print(cm)
CM=ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["Ham","Spam"])
CM.plot()
plt.title("Spam vs Ham classification")
plt.show()
#---------------------------------------------- Second model Logistic regression ---------------------------------------------------

model2=LogisticRegression(max_iter=1000)
model2.fit(x_train_vectorized,y_train)
y_pred2=model2.predict(x_test_vectorized)
print(
    classification_report(y_test,y_pred2,target_names=["Ham","Spam"])
)
accuracy2=accuracy_score(y_test,y_pred2)
print("The accuracy score of the Logistic regression model is ",accuracy2)
#---------------------------------------- Third model - Linear SVC - -------------------------------------------------------------------

model3=LinearSVC()
model3.fit(x_train_vectorized,y_train)

y_pred3=model3.predict(x_test_vectorized)
print(classification_report(y_test,y_pred3,target_names=["Ham","Spam"]))
accuracy3=accuracy_score(y_test,y_pred3)
print("The accuracy score of the Linear SVC model is",accuracy3)

# Saving the best performing model and the vectorizer ----------------------------------------------------------------------------
joblib.dump(model3,"Spam_model.pkl")
joblib.dump(vectorizer,"Vectorizer.pkl")



