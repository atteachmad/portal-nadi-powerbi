import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Halaman Web
st.set_page_config(page_title="DB-NADI | Portal Analitik", layout="wide")

# --- SISTEM LOGIN SEDERHANA ---
def check_password():
    """Mengembalikan nilai True jika password benar."""
    def password_entered():
        # Cek kecocokan user dan password (bisa disesuaikan)
        if st.session_state["username"] == "admin" and st.session_state["password"] == "nadi123":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Hapus password dari memory demi keamanan
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # Tampilan Awal: Form Login
        st.markdown("<h1 style='text-align: center;'>Masuk ke DB-NADI</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.button("Login", on_click=password_entered)
        return False
    elif not st.session_state["password_correct"]:
        # Tampilan jika password salah
        st.markdown("<h1 style='text-align: center;'>Masuk ke DB-NADI</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.button("Login", on_click=password_entered)
            st.error("Username atau Password salah 😕")
        return False
    return True

# --- HALAMAN UTAMA DASHBOARD ---
if check_password():
    st.markdown("### Dashboard Kualitas Layanan & Sentimen")
    
    # Masukkan URL iFrame Power BI Anda di sini
    # Pastikan sudah ditambahkan parameter penutup nav dan filter
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiNzQ5NWJmZjMtNjQ2Yy00MzE5LThjZDMtZjFkNGU0ODdmMDY3IiwidCI6ImUyMjAwNGJkLWFjYmItNDJlMS05YmQ4LWExMTUzZDcwNDdlMCIsImMiOjEwfQ%3D%3D&navContentPaneEnabled=false&filterPaneEnabled=false"
    
    # Merender iframe di dalam web
    components.html(
        f'<iframe title="JNE Bandung" width="100%" height="800" src="{power_bi_url}" frameborder="0" allowFullScreen="true"></iframe>',
        height=800,
    )
