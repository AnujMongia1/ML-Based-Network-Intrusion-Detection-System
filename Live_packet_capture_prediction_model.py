import pandas as pd
import joblib
import numpy as np
import os
import time
import subprocess


tshark_path = r"C:\Program Files\Wireshark\tshark.exe"

interface_name = "Wi-Fi"

output_pcap = "test.pcap"

output_csv = "capture_data.csv"

model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')


def capture_packets():

    tshark_command = [
        tshark_path,
        "-i", interface_name,
        "-w", output_pcap,
        "-a", "duration:10",
    ]
    
    try:
        subprocess.run(tshark_command, check=True)
        print(f"Capture completed, exporting to CSV")
    except subprocess.CalledProcessError as e:
        print(f"Error{e}")


def convert_pcap_to_csv():

    tshark_to_csv_command = [
        tshark_path,
        "-r", output_pcap,
        "-T", "fields",
        "-E", "separator=,",
        "-E", "quote=d",
        "-E", "header=y",
        "-e", "frame.number",
        "-e", "frame.time",
        "-e", "ip.src",
        "-e", "ip.dst",
        "-e", "ip.proto",
        "-e", "frame.len",
        "-e", "tcp.srcport",
        "-e", "tcp.dstport"
    ]
    

    try:
        with open(output_csv, "w") as f:
            subprocess.run(tshark_to_csv_command, stdout=f, check=True)
        print(f"Exported to CSV")
    except subprocess.CalledProcessError as e:
        print(f"Error{e}")

def analyze_data():

    if os.path.exists(output_csv) and os.path.getsize(output_csv) > 0:

        df = pd.read_csv(output_csv)
        df.rename(columns={'tcp.srcport': 'src_port', 'tcp.dstport': 'dst_port'}, inplace=True)

        features_new = df[['src_port', 'dst_port']]
        
        features_new = features_new.fillna(0)

        scaled_features_new = scaler.transform(features_new)
        predictions = model.predict(scaled_features_new)

        df['prediction'] = predictions

        print(df[['frame.time', 'ip.src', 'ip.dst', 'ip.proto', 'src_port', 'dst_port', 'prediction']])
        
        attack_rows = df[(df['prediction'] == 1) & (df['dst_port'] == 22)]


        if len(attack_rows)>10:
            print("Attack Detected!")
            print(len(attack_rows))
        else:
            print("Normal Traffic")
            print(len(attack_rows))
    else:
        print("Error.")


while True:
    capture_packets()
    convert_pcap_to_csv()
    analyze_data()
    time.sleep(1) 
