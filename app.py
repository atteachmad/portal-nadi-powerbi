import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Halaman Web
st.set_page_config(page_title="DB-NADI | Portal Analitik", layout="wide", initial_sidebar_state="collapsed")

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
        
        if user in USERS and USERS[user]["password"] == passwd:
            st.session_state["password_correct"] = True
            st.session_state["user_role"] = USERS[user]["role"] 
            del st.session_state["password"]  
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Jika belum login atau password salah
    if "password_correct" not in st.session_state or not st.session_state["password_correct"]:
        
        # --- CSS KHUSUS HALAMAN LOGIN ---
        st.markdown("""
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

                html, body, [class*="css"] {
                    font-family: 'Poppins', sans-serif;
                }

                .stApp {
                    background: linear-gradient(135deg, #0f2027, #203a43, #2ca1bd);
                    background-size: 400% 400%;
                    animation: gradientBG 15s ease infinite;
                }

                @keyframes gradientBG {
                    0% { background-position: 0% 50%; }
                    50% { background-position: 100% 50%; }
                    100% { background-position: 0% 50%; }
                }

                .block-container {
                    padding-top: 8rem !important;
                }

                div[data-testid="column"]:nth-of-type(2) {
                    background: rgba(255, 255, 255, 0.05);
                    backdrop-filter: blur(15px);
                    -webkit-backdrop-filter: blur(15px);
                    border-radius: 20px;
                    padding: 3rem;
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                }

                .login-title {
                    text-align: center;
                    font-size: 3rem;
                    font-weight: 800;
                    background: -webkit-linear-gradient(#ffffff, #b3e5fc);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    margin-bottom: 0.2rem;
                    letter-spacing: 2px;
                }
                .login-subtitle {
                    text-align: center;
                    color: #b0bec5;
                    font-size: 1rem;
                    margin-bottom: 2.5rem;
                    font-weight: 300;
                    letter-spacing: 1px;
                }

                .stTextInput p {
                    color: #e0e0e0 !important;
                    font-weight: 600;
                    letter-spacing: 1px;
                }

                /* PERBAIKAN: Background putih terang, teks biru dongker/hitam agar sangat jelas */
                .stTextInput input {
                    background-color: #ffffff !important;
                    color: #0f172a !important; 
                    border: 2px solid transparent !important;
                    border-radius: 10px !important;
                    padding: 12px 15px !important;
                    font-weight: 600 !important;
                }
                .stTextInput input:focus {
                    border-color: #4fc3f7 !important;
                    box-shadow: 0 0 10px rgba(79, 195, 247, 0.5) !important;
                    outline: none !important;
                }

                /* PERBAIKAN: Memastikan tombol membentang penuh */
                .stButton > button {
                    width: 100% !important;
                    background: linear-gradient(90deg, #1cb5e0 0%, #000851 100%);
                    color: white !important;
                    font-weight: 600 !important;
                    border: none !important;
                    border-radius: 25px !important;
                    padding: 12px 0 !important;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    transition: all 0.3s ease;
                    margin-top: 1.5rem;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
                }
                .stButton > button:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 8px 25px rgba(28, 181, 224, 0.6);
                    background: linear-gradient(90deg, #000851 0%, #1cb5e0 100%);
                }

                header {visibility: hidden;}
                footer {visibility: hidden;}
            </style>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1.5, 2, 1.5]) 
        with col2:
            st.markdown("<div class='login-title'>DB-NADI</div>", unsafe_allow_html=True)
            st.markdown("<div class='login-subtitle'>Portal Analitik Eksekutif</div>", unsafe_allow_html=True)
            
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            
            # PERBAIKAN: Menambahkan use_container_width agar tombol tidak jadi bulat
            st.button("LOGIN", on_click=password_entered, use_container_width=True)
            
            if "password_correct" in st.session_state and not st.session_state["password_correct"]:
                st.error("Kredensial tidak valid. Silakan coba lagi.")
        return False
    return True

# --- HALAMAN UTAMA DASHBOARD ---
if check_password():
    role = st.session_state["user_role"]
    
    st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem !important;
                padding-bottom: 0rem !important;
                padding-left: 0rem !important;
                padding-right: 0rem !important;
                max-width: 100% !important;
            }
            header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiNzQ5NWJmZjMtNjQ2Yy00MzE5LThjZDMtZjFkNGU0ODdmMDY3IiwidCI6ImUyMjAwNGJkLWFjYmItNDJlMS05YmQ4LWExMTUzZDcwNDdlMCIsImMiOjEwfQ%3D%3D&navContentPaneEnabled=false&filterPaneEnabled=false"
    
    html_code = f"""
    <div style="position: relative; width: 100%; height: 720px; overflow: hidden;">
        
        <iframe 
            title="JNE Bandung" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 760px; border: none;" 
            src="{power_bi_url}" 
            allowFullScreen="true">
        </iframe>

        <div id="loading-curtain" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: white; z-index: 10; display: flex; justify-content: center; align-items: center; flex-direction: column;">
            <div style="border: 4px solid #f3f3f3; border-top: 4px solid #1cb5e0; border-radius: 50%; width: 60px; height: 60px; animation: spin 1s linear infinite;"></div>
            <p style="font-family: 'Poppins', sans-serif; color: #333; margin-top: 25px; font-weight: 600; font-size: 18px; letter-spacing: 1px;">Memuat Ruang Kendali DB-NADI...</p>
            <style>
                @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
            </style>
        </div>

        <script>
            setTimeout(function() {{
                var curtain = document.getElementById('loading-curtain');
                if (curtain) {{
                    curtain.style.transition = "opacity 0.8s ease";
                    curtain.style.opacity = "0"; 
                    setTimeout(function() {{ curtain.style.display = "none"; }}, 800); 
                }}
            }}, 4000); 
        </script>

    </div>
    """
    
    components.html(html_code, height=720)
