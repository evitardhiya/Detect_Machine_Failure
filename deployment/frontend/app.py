import streamlit as st
import requests
from PIL import Image

#set page
st.set_page_config(
    page_title="Tool Failure Prediction",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.github.com/evitardhiya',
        'Report a bug': 'https://www.google.com',
        'About': 'Milestone 2-Phase 1, by: Evita Ardhiya Ramadhani Batch 11-Hacktiv8 Full Time Data Science'
    }
)

# set dashboard
st.caption('Hacktiv8 Full Time Data Science')

image = Image.open('gambar.jpg')
st.image(image, caption=None)

st.title('Deteksi Ada Tidaknya Kegagalan Alat')
st.caption("Silahkan masukkan data alat Anda")

#data
suhu = st.number_input("Suhu Alat")
kec_rotasi = st.number_input("Kecepatan Rotasi")
torsi = st.number_input("Torsi")
lama_penggunaan = st.number_input("lama Penggunaan Alat")

#inference
data = {'suhu_proses': suhu,
        'kecepatan_rotasi': kec_rotasi,
        'torsi': torsi,
        'lama_penggunaan': lama_penggunaan}

URL = "https://evita-batch11-backend.herokuapp.com/predict"

#komunikasi
r = requests.post(URL, json=data)
res = r.json()
if r.status_code == 200:
    st.title(res['result']['class_name'])
elif r.status_code == 400:
    st.title('error')
    st.write(res['message'])