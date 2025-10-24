import streamlit as st

st.set_page_config(
    page_title="ประโยชน์การออกกำลังกาย",
    page_icon="🏃"
)

st.title("🏃 ประโยชน์มหัศจรรย์ของการออกกำลังกาย")

st.image("https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzNTU2NHwwfDF8c2VhcmNofDN8fGV4ZXJjaXNlfGVufDB8fHx8MTcwMDYyOTI4NHww&ixlib=rb-4.0.3&q=80&w=1080",
         caption="การออกกำลังกายสม่ำเสมอคือยาวิเศษ")

st.markdown("""
การออกกำลังกายอย่างสม่ำเสมอ เป็นหนึ่งในสิ่งที่ดีที่สุดที่คุณสามารถทำได้
เพื่อสุขภาพกายและสุขภาพจิตใจ
""")

st.subheader("ประโยชน์ต่อสุขภาพกาย (Physical Health)")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    * **หัวใจแข็งแรง:** ลดความเสี่ยงโรคหัวใจและความดันโลหิตสูง
    * **ควบคุมน้ำหนัก:** ช่วยเผาผลาญแคลอรีและสร้างกล้ามเนื้อ
    * **กระดูกและข้อต่อ:** เพิ่มความหนาแน่นของกระดูก ลดความเสี่ยงกระดูกพรุน
    * **ลดความเสี่ยงโรคเรื้อรัง:** เช่น เบาหวานชนิดที่ 2 และมะเร็งบางชนิด
    """)

with col2:
    st.image("https://images.unsplash.com/photo-1517836357463-d25dfeac3438?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzNTU2NHwwfDF8c2VhcmNofDEyfHxleGVyY2lzZXxlbnwwfHx8fDE3MDA2MjkyODR8MA&ixlib=rb-4.0.3&q=80&w=1080")


st.subheader("ประโยชน์ต่อสุขภาพจิต (Mental Health)")
col3, col4 = st.columns(2)

with col3:
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzNTU2NHwwfDF8c2VhcmNofDEwfHxtZWRpdGF0aW9ufGVufDB8fHx8MTcwMDYyOTM0NHww&ixlib=rb-4.0.3&q=80&w=1080")

with col4:
    st.markdown("""
    * **ลดความเครียด:** ร่างกายจะหลั่งสาร 'เอ็นดอร์ฟิน' (Endorphins) ซึ่งเป็นสารแห่งความสุข
    * **นอนหลับดีขึ้น:** ช่วยให้นอนหลับได้ลึกและสนิทมากขึ้น
    * **สมองปลอดโปร่ง:** เพิ่มการไหลเวียนเลือดไปเลี้ยงสมอง ช่วยเรื่องความจำ
    * **เพิ่มพลังงาน:** แม้จะเหนื่อย แต่ในระยะยาวจะทำให้คุณรู้สึกกระฉับกระเฉงขึ้น
    """)

st.divider()

st.header("เริ่มต้นอย่างไรดี?")
st.markdown("""
* **เริ่มจากน้อยๆ:** ไม่จำเป็นต้องหักโหม เริ่มต้นเดินเร็ว 15-30 นาทีต่อวัน
* **หาสิ่งที่ชอบ:** ลองเต้นแอโรบิก, ปั่นจักรยาน, วิ่ง, โยคะ หรือยกน้ำหนัก
* **ทำให้สม่ำเสมอ:** ตั้งเป้าหมายอย่างน้อย 150 นาทีต่อสัปดาห์

**แค่ขยับ ก็เท่ากับออกกำลังกายแล้ว!**
""")