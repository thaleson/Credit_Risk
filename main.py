import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
import joblib



# Configuração da página
st.set_page_config(page_title="Credit Risk Predictor", page_icon="💳")


# Aplicar estilos personalizados
st.markdown(
    f"""
    <style>
    {open("static/styles.css").read()}
    </style>
    """,
    unsafe_allow_html=True
)
# Carregar o modelo Random Forest
model = joblib.load('models/modelo_arvore_decisao.pkl')

# Função para carregar animações Lottie
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Configurar as opções do menu
with st.sidebar:
    selected = option_menu(
        "Menu",
        ["Home", "Sobre o Projeto", "Previsão de Crédito"],
        icons=["house", "info-circle", "graph-up"],
        menu_icon="cast",
        default_index=0,
    )

 
    st.markdown("""
        <p style="text-align: center;">Meus contatos</p>
        """, unsafe_allow_html=True)

    # Badges
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between;">
            <div>
                <a href="https://github.com/thaleson" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="https://www.linkedin.com/in/thaleson-silva-9298a0296/" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="mailto:thaleson177@gmail.com" target="_blank">
                    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" width="80" />
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Redirecionar para a página selecionada
if selected == "Home":
    from pages.nav import home
    home.show()
elif selected == "Sobre o Projeto":
    from pages.nav import sobre
    sobre.show()
elif selected == "Previsão de Crédito":
    from pages.nav import previsao
    previsao.show(model)
