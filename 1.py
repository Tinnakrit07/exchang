import streamlit as st
import requests
import pandas as pd

st.title("💵 เปรียบเทียบค่าเงิน : 1 USD เท่ากับเท่าไหร่ในสกุลอื่น")

# URL ของ API
url = "https://v6.exchangerate-api.com/v6/5da0e03925526bf0ce5a6ee3/latest/USD"

# ดึงข้อมูลจาก API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    rates = data.get("conversion_rates", {})

    # แปลงเป็น DataFrame
    df = pd.DataFrame(list(rates.items()), columns=["สกุลเงิน", "อัตราแลกเปลี่ยนต่อ 1 USD"])
    df = df.sort_values(by="สกุลเงิน").reset_index(drop=True)

    # ✨ ย้ายช่องกรอกขึ้นมาไว้ด้านบนก่อนแสดงวันที่
    st.subheader("💰 คำนวณอัตราแลกเปลี่ยน (จาก 1 USD)")
    user_currency = st.text_input(
        "กรอกสกุลเงิน (เช่น THB, JPY, EUR, GBP, CNY):",
        value="THB"
    ).upper()

    if user_currency in rates:
        st.success(f"1 USD = {rates[user_currency]:,.2f} {user_currency}")
    else:
        st.warning("⚠️ ไม่พบสกุลเงินนี้ในข้อมูล กรุณากรอกใหม่ (ใช้รหัสสกุลเงิน 3 ตัว เช่น THB, EUR)")

    # แสดงวันที่อัปเดต (อยู่ใต้ช่องกรอก)
    st.caption(f"📅 อัปเดตล่าสุด: {data.get('time_last_update_utc')}")

    # แสดงตารางข้อมูลทั้งหมด
    st.dataframe(df, use_container_width=True)

else:
    st.error(f"❌ ไม่สามารถดึงข้อมูลได้ (HTTP {response.status_code})")
