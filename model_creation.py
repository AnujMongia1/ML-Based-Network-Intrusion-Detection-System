import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import re
import joblib
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('hydra_csv.csv')

# Extract source and destination port
def extract_ports(info):
    match = re.findall(r'(\d+)\s*>\s*(\d+)', info)
    if match:
        src_port, dst_port = match[0]
        return int(src_port), int(dst_port)
    return 0, 0

df['src_port'], df['dst_port'] = zip(*df['Info'].apply(extract_ports))


df['attack'] = df['dst_port'].apply(lambda x: 1 if x == 22 else 0)


features = df[['src_port', 'dst_port']]
labels = df['attack']


scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(scaled_features, labels)
print(df['attack'].sum())
print(len(df))

joblib.dump(model, 'random_forest_model.pkl') 
joblib.dump(scaler, 'scaler.pkl')
