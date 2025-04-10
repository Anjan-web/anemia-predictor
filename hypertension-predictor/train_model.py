import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.impute import SimpleImputer
import joblib
df=pd.read_csv(r"C:\Users\boyin\Downloads\data (3).csv")
df.drop(columns=['Patient_Number'],axis=1,inplace=True)
imputer=SimpleImputer(strategy='mean')
df1=pd.DataFrame(imputer.fit_transform(df),columns=df.columns)
X=df1.drop('Blood_Pressure_Abnormality',axis=1)
Y=df['Blood_Pressure_Abnormality']
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
rft=RandomForestClassifier()
rft.fit(x_train,y_train)
r_y_pred=rft.predict(x_test)
accuracy=accuracy_score(y_test,r_y_pred)
print("✅ Accuracy:", accuracy)
print("\n📊 Classification Report:\n", classification_report(y_test, r_y_pred))
print("🧮 Confusion Matrix:\n", confusion_matrix(y_test, r_y_pred))
joblib.dump(rft, "model.pkl")
print("\n📦 Model saved as model.pkl")