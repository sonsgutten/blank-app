import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner  

qr_code = qrcode_scanner(key='qrcode_scanner')  


if qr_code:
  st.write(qr_code) 


#st.write(f"{item['name']} has a :{item['pet']}:")
st.write(f"Test på linje")
