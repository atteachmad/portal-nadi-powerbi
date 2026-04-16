import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Halaman Web
st.set_page_config(page_title="DB-NADI | Portal Analitik", layout="wide")

# --- SISTEM LOGIN SEDERHANA ---
def check_password():
    """Mengembalikan nilai True jika password benar."""
    
    # Database user sederhana dalam bentuk dictionary
    USERS = {
        "pao": {"password": "123", "role": "admin"},
        "iyus": {"password": "123", "role": "pelihat"}
    }

    def password_entered():
        user = st.session_state["username"]
        passwd = st.session_state["password"]
        
        # Cek apakah username ada di database dan password cocok
        if user in USERS and USERS[user]["password"] == passwd:
            st.session_state["password_correct"] = True
            st.session_state["user_role"] = USERS[user]["role"] # Menyimpan role user
            del st.session_state["password"]  
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center;'>Masuk ke DB-NADI</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.button("Login", on_click=password_entered)
        return False
    elif not st.session_state["password_correct"]:
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
    role = st.session_state["user_role"]
    st.success(f"Selamat datang, Anda login sebagai {role.capitalize()}")
    st.markdown("### Dashboard Kualitas Layanan & Sentimen")
    
    # Masukkan URL iFrame Power BI Anda di sini (biarkan linknya tetap seperti ini)
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiNzQ5NWJmZjMtNjQ2Yy00MzE5LThjZDMtZjFkNGU0ODdmMDY3IiwidCI6ImUyMjAwNGJkLWFjYmItNDJlMS05YmQ4LWExMTUzZDcwNDdlMCIsImMiOjEwfQ%3D%3D&navContentPaneEnabled=false&filterPaneEnabled=false"
    
    # --- TRIK CSS CROP UNTUK MENYEMBUNYIKAN FOOTER POWER BI ---
    # Kita membuat "bingkai" (div) setinggi 760px, 
    # tapi isinya (iframe) setinggi 800px.
    # overflow: hidden; akan memotong kelebihan 40px di bagian bawah (tempat logo berada).
    
    html_code = f"""
    <div style="width: 100%; height: 760px; overflow: hidden;">
        <iframe 
            title="JNE Bandung" 
            width="100%" 
            height="800" 
            src="{power_bi_url}" 
            frameborder="0" 
            allowFullScreen="true"
            style="margin-top: 0px;">
        </iframe>
    </div>
    """
    
    # Menampilkan ke Streamlit dengan tinggi bingkai 760px
    components.html(html_code, height=760)
