
# 🚨 Early Warning System (EWS) for Credit Risk

## 🔍 Overview
This project implements an **Early Warning System (EWS)** to proactively identify loans that are likely to **default within the next 6 months**, using **post-origination behavioral signals**.

The system complements a credit approval model by continuously **monitoring active loans**, flagging high-risk accounts early, and enabling timely intervention.

An interactive **Streamlit dashboard** is deployed to visualize risk scores, alert thresholds, and portfolio-level risk dynamics.

---

## 🚀 Live Demo
🔗 **Streamlit App:** *(add your deployed Streamlit Cloud URL here)*

---

## 🎯 Business Problem
After loan origination, borrower risk can deteriorate due to:
- Missed or reduced payments
- Rising credit utilization
- Delinquency patterns
- Financial stress

Most defaults show **early warning signals months in advance**, but traditional systems react only after serious delinquency.

---

## 🎯 Project Objective
To build an **Early Warning System** that:
- Predicts default risk over a **6-month horizon**
- Flags high-risk loans early
- Optimizes alerts for **high recall**
- Provides interpretable risk segmentation
- Supports operational decision-making

---

## 📂 Data
- **Source:** LendingClub accepted loans dataset (Kaggle)  
  https://www.kaggle.com/datasets/wordsforthewise/lending-club/data

- **Loan outcomes used:**  
  - Fully Paid → non-default  
  - Charged Off → default  

---

## 🛠️ Methodology

### Feature Engineering (Behavioral Signals)
Post-origination variables were used, including:
- Payment behavior (`last_pymnt_amnt`, `total_rec_prncp`)
- Delinquency indicators (`mths_since_last_delinq`, `num_tl_30dpd`)
- Credit utilization (`revol_util`, `bc_util`)
- Credit activity & recency (`inq_last_12m`, `mo_sin_rcnt_tl`)
- Stability controls (`annual_inc`, `dti`, `fico_range_low`)

---

### Modeling Approach
- **Model:** Logistic Regression  
- Chosen for interpretability and stability  
- Class imbalance handled via class weighting  

---

## 🚨 Alert Strategy
Alerts are calibrated using **portfolio-based thresholds**, flagging the **top X% highest-risk loans** to balance recall and operational capacity.

---

## 📊 Dashboard Features
- Alert-rate slider
- Risk bucket segmentation
- Default rate comparison
- EWS score distribution
- Ranked high-risk account list

---

## 📁 Project Structure
```
early-warning-system-credit-risk/
│
├── app.py
├── ews_scores.csv
├── requirements.txt
└── README.md
```

---

## 🧠 One-Line Summary
*Built an early warning system using behavioral credit signals to flag loans likely to default within 6 months, deployed via an interactive Streamlit dashboard.*
