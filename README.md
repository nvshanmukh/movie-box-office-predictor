# 🎬 Movie Box Office Gross Predictor

A machine learning-powered web application that predicts the box office revenue of movies using key features like budget, genre, popularity, runtime, director, and release details.

> ⚙️ Built using Flask, Python, HTML/CSS, and Scikit-learn.

---

## 🚀 Live Preview

This app runs locally via Flask. For a publicly hosted version, consider deploying it using platforms like **Streamlit Cloud**, **Render**, or **Heroku**.

---

## 📊 Features

- Predicts movie revenue using linear regression.
- Inputs include budget, genre, popularity, rating, votes, director, and release date.
- Clean, modern user interface.
- Feature scaling using `StandardScaler`.
- Encodes categorical data like `genres` and `director`.
- Full visualization support (EDA + Feature Importance).

---

## 🧠 Tech Stack

- **Backend:** Flask, Python
- **ML:** Scikit-learn, Linear Regression
- **Frontend:** HTML5, CSS3, Bootstrap
- **Data:** TMDB 5000 Movie Dataset
- **Visualization:** Seaborn, Matplotlib, WordCloud

---

## 📁 Project Structure

📦 movie-box-office-predictor
├── app.py
├── model_movies.pkl
├── scaler_movies.pkl
├── label_encoders.pkl
├── templates/
│ ├── Demo2.html
│ └── resultnew.html
├── static/
│ └── styles.css
├── README.md
└── requirements.txt



---

##  How to Run Locally

### 1. Clone the Repository
git clone https://github.com/yourusername/movie-box-office-predictor.git
cd movie-box-office-predictor

### 2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 3. Run the codes
run the ipynb file
cd app
python app.py

Visit http://127.0.0.1:5000 in your browser to use the app. 


📷 Screenshots

🏠 Homepage
![Homepage](homepage.png)

📊 Prediction Result Page
![Result](prediction.png)


## 📚 Data Source

[TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)



🙋‍♂️ Author
Shanmukh Venkata Nutulapati
📧 Email: nvshanmukh28@gmail.com
🔗 GitHub: https://github.com/nvshanmukh

Sekharamahanthi Sai Yeshwin
📧 Email: saiyeshwin@gmail.com
🔗 GitHub: https://github.com/saiyeshwin

Ritesh Kandra Reddy
📧 Email: riteshkandra.reddy2022@vitstudent.ac.in
🔗 GitHub: https://github.com/Ritesh1147
