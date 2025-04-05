# Centralized MQ Demo (ActiveMQ with Python)

This project demonstrates a **centralized message queue (MQ)** using **ActiveMQ** and **STOMP protocol** in Python.  
It consists of two separate services:
- **Producer** (`producer.py`) - Sends messages to the queue.
- **Consumer** (`consumer.py`) - Listens for messages and processes them.

## 📌 How It Works
1. The **Producer** sends messages to ActiveMQ.
2. The **Consumer** listens for messages and processes them.
3. If the **Consumer is offline**, messages remain in the queue.
4. When the **Consumer restarts**, it processes all queued messages.

## 🚀 Setup and Run Instructions

### **1️⃣ Install ActiveMQ**
Download and install **ActiveMQ** from [ActiveMQ Website](https://activemq.apache.org/components/classic/download/).  
After installation, navigate to the `bin` directory and start the server:

```sh
./activemq start
```

### **2️⃣ Install Python**
Download Python from python.org.
During installation, check the box "Add Python to PATH".
Restart your PC, then run:

```sh
python --version
python -m pip install stomp.py
```

### **3️⃣ Run the Services**
Start the Consumer (Receiver)

```sh
python consumer.py
```
Send Messages Using the Producer (Sender)

```sh
python producer.py
```
