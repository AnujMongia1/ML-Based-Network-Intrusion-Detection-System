# Machine Learning-Based Network Intrusion Detection System (IDS)

## Overview

This project is a **Machine Learning-based Intrusion Detection System (IDS)** designed to detect **brute force** and **dictionary-based authentication attacks** over **SSH (Secure Shell)**. It uses the **Random Forest classifier** to classify network traffic as either malicious or benign, alerting the system whenever potential intrusion is detected in real-time.

The system was tested in a live environment using **penetration testing** tools like **Hydra** and **Wireshark** to simulate attacks and evaluate the performance of the IDS.

## Features

- **Real-time Traffic Monitoring:** Captures and analyzes network traffic in real time.
- **Brute Force and Dictionary Attack Detection:** Specifically focuses on detecting dictionary and brute force authentication attacks on SSH.
- **Machine Learning:** Trained using the Random Forest Classifier to detect malicious activity based on network traffic data.
- **Penetration Testing:** Uses Hydra on Kali Linux to simulate dictionary-based attacks, creating real-world scenarios to test the IDS.

## Tools and Technologies

- **Programming Language:** Python
- **Libraries/Frameworks:**
    - Scikit-learn (for machine learning)
    - Pandas (for data processing)
    - Wireshark (for network traffic analysis)
    - TShark (for capturing traffic on Windows)
- **Penetration Testing Tools:** Hydra (for simulating dictionary and brute-force SSH attacks)
- **Operating Systems:** Kali Linux, Windows 10 (VMs)
- **Network Traffic Dataset:** [913 Malicious Network Traffic PCAPs Dataset](https://ieee-dataport.org/open-access/913-malicious-network-traffic-pcaps-and-binary-visualisation-images-dataset)

- ## Dataset

This project uses the **“913 Malicious Network Traffic PCAPs and Binary Visualisation Images Dataset”** from IEEE Dataport. The primary dataset used for training the model is:

- **hydra_ssh.pcap**: A packet capture file that simulates an SSH dictionary attack using Hydra.

These files contain information such as source and destination IP addresses, ports, protocols, and other important details that are extracted and preprocessed for machine learning training.

### The IDS consists of:

- **Traffic capture**: TShark captures network packets in real time.
- **Data processing**: Relevant features such as source/destination ports are extracted from PCAP files and processed.
- **Random Forest Classifier**: The model classifies the network traffic as benign or malicious based on the trained data.
- **Alert system**: The system raises an alert when it detects a potential intrusion.
