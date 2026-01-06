import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

st.set_page_config("Pharmevo | AI Sales Forecast", "💊", layout="wide")

st.title("💊 Pharmevo Pharmaceuticals")
st.subheader("Sales Forecasting & Inventory Intelligence")

# Load model & data
model = pickle.load(open("model.pkl","rb"))
df = pd.read_csv("future_forecast_inventory.csv")

menu = st.sidebar.radio(
    "Select View",
    [
        "Company Sales Forecast",
        "Top Medicines",
        "High-Value Medicines",
        "Inventory & Risk"
    ]
)

# 1️⃣ Company forecast
if menu == "Company Sales Forecast":
    company = df.groupby('Month')['Predicted_Units'].sum()
    st.line_chart(company)

# 2️⃣ Top medicines
elif menu == "Top Medicines":
    top = df.groupby('Product')['Predicted_Units'].sum().sort_values(ascending=False).head(10)
    st.dataframe(top)

# 3️⃣ High-value medicines
elif menu == "High-Value Medicines":
    df['Value'] = df['Predicted_Units'] * df['Price']
    high = df.groupby('Product')['Value'].sum().sort_values(ascending=False).head(10)
    st.dataframe(high)

# 4️⃣ Inventory & risk
elif menu == "Inventory & Risk":
    st.dataframe(
        df[['Product','Month','Predicted_Units','Recommended_Inventory','Risk']]
    )

st.caption("© Pharmevo Pharmaceuticals | AI Decision Support System")
