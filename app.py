import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.title("🕒 تعديل عمود OrderDate +3 ساعات")

def add_3_hours(text):
    try:
        dt = datetime.strptime(str(text), '%m/%d/%Y %I:%M:%S %p')
        dt_plus3 = dt + timedelta(hours=3)
        return dt_plus3.strftime('%m/%d/%Y %I:%M:%S %p')
    except:
        return text

uploaded_file = st.file_uploader("اختر ملف CSV فقط", type=['csv'])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, encoding='latin1')  # 🔹 هنا الترميز
        if 'OrderDate' in df.columns:
            df['OrderDate'] = df['OrderDate'].apply(add_3_hours)
            st.success("✅ تم تعديل عمود OrderDate")
        else:
            st.warning("⚠️ الملف لا يحتوي على عمود OrderDate")

        st.dataframe(df)

        output_file = "OrderDate_updated.xlsx"
        df.to_excel(output_file, index=False)
        with open(output_file, "rb") as f:
            st.download_button(
                label="⬇️ تحميل النسخة المعدلة Excel",
                data=f,
                file_name="OrderDate_updated.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    except Exception as e:
        st.error(f"❌ حدث خطأ: {e}")
