# 🩺 Diabetic Retinopathy Prediction using Machine Learning

A machine learning project to predict the likelihood of **Diabetic Retinopathy** in patients based on clinical features such as age, blood pressure, and cholesterol levels.

---

## 📌 Project Overview

Diabetic Retinopathy is a diabetes complication that affects eyes. Early detection can prevent vision loss. This project uses supervised machine learning models to classify whether a patient has retinopathy or not.

**Target Variable:**
- `1` → Retinopathy
- `0` → No Retinopathy

---

## 📁 Project Structure

```
retinopathy-prediction/
│
├── Predict_Retinopathy_Project.ipynb   # Main Jupyter Notebook
├── P600_pronostico_dataset.csv         # Dataset used for training/testing
├── best_retinopathy_model.pkl          # Saved best ML model (joblib)
├── model_accuracies_bar.png            # Bar chart of model accuracies
├── requirements.txt                    # Python dependencies
├── predict.py                          # Standalone prediction script
└── README.md                           # Project documentation
```

---

## 📊 Dataset Features

| Feature       | Description                        |
|---------------|------------------------------------|
| `age`         | Age of the patient                 |
| `sbp`         | Systolic Blood Pressure            |
| `dbp`         | Diastolic Blood Pressure           |
| `cholesterol` | Cholesterol level                  |
| `prognosis`   | Target: retinopathy / no_retinopathy |

---

## 🤖 Models Used

| Model                  | Description                              |
|------------------------|------------------------------------------|
| Random Forest          | Ensemble of decision trees               |
| Logistic Regression    | Linear classification model              |
| SVM (Linear Kernel)    | Support Vector Machine                   |
| Decision Tree          | Single tree-based classifier             |

The **best model** is automatically selected by accuracy and saved as `best_retinopathy_model.pkl`.

---

## 📈 Results

- Model accuracies are compared using a bar chart (`model_accuracies_bar.png`)
- Cross-validation (5-fold) is performed on the best model
- Hyperparameter tuning is done via `GridSearchCV` on Random Forest

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/retinopathy-prediction.git
cd retinopathy-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Jupyter Notebook
```bash
jupyter notebook Predict_Retinopathy_Project.ipynb
```

### 4. Or use the prediction script
```bash
python predict.py
```

---

## 🔮 Make a Prediction

```python
from predict import predict_retinopathy

result = predict_retinopathy(age=55, sbp=140, dbp=90, cholesterol=220)
print("Retinopathy" if result == 1 else "No Retinopathy")
```

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Joblib
- Jupyter Notebook

---

## 👤 Author

**Your Name**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
