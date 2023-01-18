import streamlit as st
from streamlit_option_menu import option_menu as menu

with st.sidebar:
    mainmenu = menu("MR SAMAK", ["Home", "Luas Persegi", "Luas Segitiga"],
    icons=['house'], 
    default_index=0)

if (mainmenu == "Home"):
    st.write("# INI HALAMAN UTAMA")


if (mainmenu == "Luas Segitiga"):
    st.write("""
    # Aplikasi Luas Segitiga
    Ini adalah aplikasi sederhana untuk menghitung luas segitiga
    """)

    alas = st.number_input("Masukkan alas", 0)
    tinggi = st.number_input("Masukkan tinggi", 0)
    tombolhitung = st.button("hitung luas")

    if tombolhitung:
        luas = 0.5 * alas * tinggi
        st.success(f"Luas segitiga tersebut adalah {luas}")

if (mainmenu == "Luas Persegi"):
    st.write("""
    # Aplikasi Luas Persegi
    Ini adalah aplikasi sederhana untuk menghitung luas Persegi
    """)

    sisi = st.number_input("Masukkan sisi", 0)
    tombolhitung = st.button("hitung luas")

    if tombolhitung:
        luas = sisi * sisi
        st.success(f"Luas Persegi tersebut adalah {luas}")