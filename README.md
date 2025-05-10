# Multimedia Deepfake Detection using Deep Learning

A Python-based desktop application to detect fake (AI-generated) images and videos using Convolutional Neural Networks (CNN). This project was built for the **Smart India Hackathon** and aims to combat the increasing threat of multimedia deepfakes.

## 🚀 Features

- 📷 Fake Image & Video Detection
- 🧠 CNN-Based Deep Learning Model
- 🗃️ SQLite3 Database for Logging
- 🖼️ User Interface using Tkinter
- 📊 Result Visualization using Matplotlib

## 🛠️ Technologies Used

- Python
- TensorFlow & Keras
- OpenCV
- NumPy
- Matplotlib
- Tkinter
- SQLite3

## 🖥️ How to Run

**1. Clone the repository:**
   bash
   git clone https://github.com/your-username/multimedia-deepfake-detector.git
   cd multimedia-deepfake-detector
   
**2.Create a virtual environment and install dependencies:**
bash
Copy code
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate for Windows
pip install -r requirements.txt

**3.Run the application:**
bash
Copy code
python main.py

📁 **Project Structure**

├── model/                  # Trained CNN model
├── media_samples/         # Sample images/videos
├── database/              # SQLite database file
├── utils/                 # Helper scripts
├── main.py                # Entry point (Tkinter UI)
├── requirements.txt       # Python dependencies
└── README.md
