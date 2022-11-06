import streamlit as st
import pandas as pd
from datetime import time
st.header("Dental appointment scheduling dashboard")
name=st.text_input("Enter your name")
if name:
    appointment = st.slider(
        "Schedule your appointment:",
        value=(time(11, 30), time(14, 45)))
    if appointment:
        st.write(f"Hello, {name} you're scheduled for:", appointment[0].strftime('%H:%M'), "to", appointment[1].strftime('%H:%M'))
        st.image('https://www.semiosissoftware.com/wp-content/uploads/2020/01/Dental-Appointment.jpg', use_column_width=True)
