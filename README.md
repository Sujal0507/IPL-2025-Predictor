** IPL Match Outcome Predictor (2008–2024)**

A Machine Learning project that predicts the winning team of an IPL match using historical match data and match conditions. Built with a Logistic Regression model and deployed using Streamlit.


📌 Objective
To build a machine learning model that predicts the likely winner of an IPL match based on input features such as city and total runs. The goal is to provide real-time insights useful for fans, analysts, and fantasy league players.

🧠 Approach
Collected and preprocessed IPL match data (2008–2024) from Kaggle

Selected key features: match_id, city, winner, total_runs

Performed extensive data cleaning and feature engineering

Trained a Logistic Regression classifier

Achieved ~80% accuracy on the test data

Deployed the model with an interactive UI using Streamlit

💻 Tech Stack
Language: Python

Libraries: Pandas, Scikit-learn, Matplotlib

IDE/Notebook: Jupyter Notebook

Frontend: Streamlit

🚀 How to Run the App
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/IPL-Win-Predictor.git
cd IPL-Win-Predictor
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py




📈 Model Performance
Algorithm used: Logistic Regression

Accuracy: ~80%

Evaluation Metrics: Accuracy Score, Confusion Matrix, Classification Report
