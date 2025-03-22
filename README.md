## 📊 **Case Study: Calories Prediction Using Machine Learning**

### 🔥 Problem Statement  
With the increasing focus on fitness, tracking calories burned during exercise is crucial for individuals aiming to maintain a healthy lifestyle. However, manual tracking is often inaccurate. This project builds a **machine learning model** to predict **calories burned** based on exercise parameters like **duration, pulse, and max pulse**.  

---

## 💡 **Objective**  
The goal of this project is to:  
✅ Predict the number of **calories burned** based on **exercise data**.  
✅ Implement **Exploratory Data Analysis (EDA)** to understand patterns.  
✅ Train a **regression model** to make accurate predictions.  
✅ Deploy the model using **Streamlit** for easy accessibility.  

---

## 🔍 **Dataset Overview**  
| Feature   | Description                                  |  
|-----------|----------------------------------------------|  
| `Duration`  | Time spent exercising (minutes)          |  
| `Pulse`     | Heart rate during exercise (bpm)         |  
| `MaxPulse`  | Maximum recorded pulse rate (bpm)        |  
| `Calories`  | Calories burned (Target variable)        |  

📂 **Dataset Source**: Kaggle

---

## 📈 **Exploratory Data Analysis (EDA)**  
Key insights from data visualization and analysis:  
📌 **Calories burned increases with exercise duration and pulse.**  
📌 **There is a positive correlation between MaxPulse and Calories.**  
📌 **Outliers were detected and handled appropriately.**  

🔎 *Visualizations included: Scatter plots, histograms, and correlation heatmaps.*  

---

## 🏢 **Model Development**  
1️⃣ **Preprocessing**:  
   - Handled missing values  
   - Normalized data (if needed)
   -  
3️⃣ **Model Selection**:  
   - Trained **Linear Regression** and **Random Forest** and **GradientBoostingRegressOR** models  
   - Evaluated using **Mean Squared Error (MSE)**  
   - **Final Model:** *Linear Regression (achieved lowest error)*  

📊 **Performance Metrics**:  
| Model            | MSE   | R² Score |  
|-----------------|------|----------|  
| Linear Regression | 852.53 | 0.82 |  
| Random Forest    | 1314.08 | 0.74 |  
| Graident Boosting    | 1671.33 | 0.67 | 

✅ **Random Forest was selected for deployment!** 

---

## 🚀 **Deployment**  
📌 **Framework Used:** Streamlit  
📌 **Model Saved as:** `calories_regressor.pkl`  
📌 **Deployed on:** Streamlit Cloud  

### 🔥 **Try It Live:**  
👉 [Calories Predictor Web App](https://caloriespredictor-lqvipksxryatlzstyupu5l.streamlit.app)  

---

## 📌 **Future Enhancements**  
✅ Add **more features** like age, weight, and workout type.  
✅ Improve **model accuracy** using deep learning models.  
✅ Develop a **mobile-friendly UI** for ease of access.  

---

## 🏆 **Key Takeaways**  
🚀 **Machine learning can significantly enhance calorie tracking accuracy.**  
📈 **EDA helps uncover valuable insights for feature selection.**  
💻 **Deploying models via Streamlit makes them accessible to users easily.**  




