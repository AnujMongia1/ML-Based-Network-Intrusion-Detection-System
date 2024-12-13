import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import re
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


df = pd.read_csv('hydra_csv.csv')
df_pred = pd.read_csv('hydra_ssh_2_csv.csv')

# Extract source and destination port
def extract_ports(info):
    match = re.findall(r'(\d+)\s*>\s*(\d+)', info)
    if match:
        src_port, dst_port = match[0]
        return int(src_port), int(dst_port)
    return 0, 0

df['src_port'], df['dst_port'] = zip(*df['Info'].apply(extract_ports))
df_pred['src_port'], df_pred['dst_port'] = zip(*df_pred['Info'].apply(extract_ports))


df['attack'] = df['dst_port'].apply(lambda x: 1 if x == 22 else 0)
df_pred['attack'] = df_pred['dst_port'].apply(lambda x: 1 if x == 22 else 0)


features = df[['src_port', 'dst_port']]
features_pred = df_pred[['src_port', 'dst_port']]
labels = df['attack']
labels_pred = df_pred['attack']


scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
scaled_features_pred = scaler.fit_transform(features_pred)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(scaled_features, labels)

y_pred_test = model.predict(scaled_features_pred)
print("Accuracy Score:")
print(accuracy_score(labels_pred, y_pred_test))
print("Confusion Matrix:")
print(confusion_matrix(labels_pred, y_pred_test))

