import streamlit as st
import hashlib
import streamlit.components.v1 as components

# Função para criptografar senha
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Banco de dados de usuários (exemplo com senha criptografada)
usuarios = {
    "projeta": hash_password("senha123"),
    "admin": hash_password("admin456")
}

# Função para validar login
def login(usuario, senha):
    if usuario in usuarios:
        return usuarios[usuario] == hash_password(senha)
    return False

# Configurações da página
st.set_page_config(page_title="Área Restrita Power BI", layout="centered")

# Sessão de autenticação
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

# Se não autenticado, mostra tela de login
if not st.session_state['autenticado']:
    st.title("🔒 Área Restrita - Login")

    usuario_input = st.text_input("Usuário")
    senha_input = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if login(usuario_input, senha_input):
            st.session_state['autenticado'] = True
            st.success("Login realizado com sucesso!")
        else:
            st.error("Usuário ou senha inválidos.")
else:
    # Se autenticado, mostra o conteúdo
    st.title("📊 Relatório Power BI")

    # Link do seu relatório Power BI (exemplo fictício - troque pelo seu)
    powerbi_link = "https://app.powerbi.com/view?r=eyJrIjoiZWI2ZTc1OWUtMmYyNC00NWI3LWJhMWItN2NhYzlkYjk4MTNlIiwidCI6ImNmOTlkZGRjLTViN2EtNDBjZi1iNTg3LTJkY2M3MDRlNTEwNCJ9"

    components.iframe(src=powerbi_link, width=1920, height=1080)

    if st.button("Sair"):
        st.session_state['autenticado'] = False
        st.experimental_rerun()
