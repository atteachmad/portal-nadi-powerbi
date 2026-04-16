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
    
    # --- 1. CSS UNTUK MELEBARKAN LAYAR 16:9 (Menghapus margin pinggir) ---
    st.markdown("""
        <style>
            /* Memaksa kontainer utama Streamlit melebar ke ujung layar */
            .block-container {
                padding-top: 1rem !important;
                padding-bottom: 0rem !important;
                padding-left: 0rem !important;
                padding-right: 0rem !important;
                max-width: 100% !important;
            }
            /* Menyembunyikan tombol header bawaan Streamlit (opsional agar lebih bersih) */
            header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    
    # Link URL Power BI Anda
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiNzQ5NWJmZjMtNjQ2Yy00MzE5LThjZDMtZjFkNGU0ODdmMDY3IiwidCI6ImUyMjAwNGJkLWFjYmItNDJlMS05YmQ4LWExMTUzZDcwNDdlMCIsImMiOjEwfQ%3D%3D&navContentPaneEnabled=false&filterPaneEnabled=false"
    
    # --- 2. TRIK CROP + TIRAI LOADING CUSTOM ---
    html_code = f"""
    <div style="position: relative; width: 100%; height: 720px; overflow: hidden;">
        
        <iframe 
            title="JNE Bandung" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 760px; border: none;" 
            src="{power_bi_url}" 
            allowFullScreen="true">
        </iframe>

        <div id="loading-curtain" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: white; z-index: 10; display: flex; justify-content: center; align-items: center; flex-direction: column;">
            <div style="border: 4px solid #f3f3f3; border-top: 4px solid #1f77b4; border-radius: 50%; width: 50px; height: 50px; animation: spin 1s linear infinite;"></div>
            <p style="font-family: sans-serif; color: #555; margin-top: 20px; font-weight: bold;">Menyiapkan Visual DB-NADI...</p>
            <style>
                @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
            </style>
        </div>

        <script>
            setTimeout(function() {{
                var curtain = document.getElementById('loading-curtain');
                if (curtain) {{
                    curtain.style.transition = "opacity 0.8s ease";
                    curtain.style.opacity = "0"; // Efek memudar
                    setTimeout(function() {{ curtain.style.display = "none"; }}, 800); // Hapus sepenuhnya
                }}
            }}, 4000); // 4000 milidetik = 4 detik
        </script>

    </div>
    """
    
    # Menampilkan ke layar
    components.html(html_code, height=720)
