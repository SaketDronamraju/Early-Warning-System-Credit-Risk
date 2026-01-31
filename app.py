import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# PAGE CONFIG

st.set_page_config(
    page_title="Early Warning System (Credit Risk)",
    layout="wide"
)

st.title("🚨 Early Warning System – Credit Risk (6-Month Horizon)")
st.caption("Behavioral Risk Monitoring & Alerts")


# LOAD DATA

@st.cache_data
def load_data():
    return pd.read_csv("ews_scores.csv")

df = load_data()


# SIDEBAR CONTROLS

st.sidebar.header("Alert Configuration")

alert_rate = st.sidebar.slider(
    "Alert Rate (% of portfolio flagged)",
    min_value=10,
    max_value=50,
    value=30,
    step=5
) / 100

alert_threshold = np.quantile(df["ews_score"], 1 - alert_rate)

st.sidebar.markdown(f"""
**Alert Threshold (EWS score):**  
`{alert_threshold:.3f}`
""")


# APPLY ALERTS

df["alert_flag"] = (df["ews_score"] >= alert_threshold).astype(int)

# Risk buckets
df["risk_bucket"] = pd.qcut(
    df["ews_score"],
    q=[0, 0.7, 0.9, 1.0],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)


# KPIs

col1, col2, col3 = st.columns(3)

col1.metric(
    "Alert Rate",
    f"{df['alert_flag'].mean():.1%}"
)

col2.metric(
    "Default Rate (Alerted)",
    f"{df[df['alert_flag']==1]['default_6m'].mean():.1%}"
)

col3.metric(
    "Default Rate (Non-Alerted)",
    f"{df[df['alert_flag']==0]['default_6m'].mean():.1%}"
)


# RISK BUCKET PERFORMANCE

st.subheader("📊 Risk Bucket Performance")

bucket_perf = df.groupby("risk_bucket")["default_6m"].mean()

fig, ax = plt.subplots()
bucket_perf.plot(kind="bar", ax=ax)
ax.set_ylabel("Default Rate")
ax.set_title("Observed Default Rate by Risk Bucket")
st.pyplot(fig)

# SCORE DISTRIBUTION

st.subheader("📈 EWS Score Distribution")

fig, ax = plt.subplots()
ax.hist(df["ews_score"], bins=50)
ax.axvline(alert_threshold, linestyle="--", label="Alert Threshold")
ax.set_xlabel("EWS Score")
ax.set_ylabel("Number of Loans")
ax.legend()
st.pyplot(fig)


# ALERTED LOANS TABLE

st.subheader("📋 Flagged Accounts (Top Risk)")

st.dataframe(
    df[df["alert_flag"] == 1]
    .sort_values("ews_score", ascending=False)
    .head(50)
)



st.info("""
**How to interpret this dashboard**

• Loans are ranked by an Early Warning Score (EWS)  
• The alert threshold is set based on operational capacity  
• High-risk loans are flagged months before potential default  
• Risk buckets show monotonic deterioration patterns  

This system enables **early intervention instead of reactive collections**.
""")
