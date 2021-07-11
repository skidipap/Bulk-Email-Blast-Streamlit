import streamlit as st
import pandas as pd
import io

st.title("Blast Email from DataFrame")

st.write("## Upload Data : ")

multiple_files = st.file_uploader(
    "Load Data CSV Disini",
    type="csv",
    accept_multiple_files=True
)

st.write("## View Data")

for file in multiple_files:
    data = pd.read_csv(file)
    file.seek(0)
    st.write(data)

st.write("## Pilih Column Tujuan Email")


import session 
from mail import send_mail


session_state = session.get(name="", button_sent=False)
button_sent = st.button("Tekan Untuk Lanjut")

if button_sent:
    session_state.button_sent = True 

if session_state.button_sent:
    columns = list(data.columns)
    choice = st.selectbox("Select Email", options=columns)
    recepient_list = data[choice]
    st.write("## Email Tujuan")
    st.write(recepient_list)

    form = st.form(key='my-form')
    user_gmail = form.text_input("Masukan Alamat Email Pengirim")
    user_pass = form.text_input("Masukan Password/Token", type="password")
    subject = form.text_input("Masukan Subject")
    content = form.text_input("Masukan Content")
    submit = form.form_submit_button('Kirim Email')

    if submit: 
        send_mail(user_gmail, user_pass, recepient_list , subject, content)
