import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_animation(file_path):
    """Carregar a animação Lottie a partir do arquivo JSON"""
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {file_path}")
        return None
    except json.JSONDecodeError:
        st.error(f"Erro ao decodificar o arquivo JSON: {file_path}")
        return None

def show():
    # Configurar o título da página
    st.title("Bem-vindo ao Sistema de Previsão de Risco de Crédito! 📊")

    # Adicionar subtítulo
    st.subheader("Avalie a probabilidade de inadimplência com nossa ferramenta precisa 👋")

    # Carregar animações
    animation_1 = load_lottie_animation("assets/lottie/animation3.json")
    animation_2 = load_lottie_animation("assets/lottie/animationproduct.json")  # Substitua por um arquivo diferente, se necessário

    if animation_1 and animation_2:
        # Configurar layout em colunas
        col1, col2 = st.columns(2)

        # Conteúdo da coluna 1
        with col1:
            st_lottie(animation_1, height=350, width=350, key="animation1")
            st.markdown(
                """
                <div style='margin-top: 10px;'>
                    <h5 style='text-align: justify;'>Este sistema utiliza um modelo de aprendizado de máquina para prever a probabilidade de inadimplência com base em dados financeiros fornecidos. Você pode inserir suas informações e obter uma avaliação precisa do risco de crédito.</h5>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Conteúdo da coluna 2
        with col2:
            st.markdown(
                """
                <div style='margin-top: 10px;'>
                    <h5 style='text-align: justify;'>O sistema foi projetado para ajudar você a entender melhor sua situação financeira e tomar decisões informadas. Nossos modelos foram treinados com dados reais e podem fornecer insights valiosos para sua gestão financeira.</h5>
                </div>
                """,
                unsafe_allow_html=True
            )
            st_lottie(animation_2, height=550, width=350, key="animation2")

        # Adicionar um aviso
        st.markdown(
            """
            <div style='background-color: #d4edda; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #155724;'>Aviso:</h4>
                <p style='color: #155724;'>Este sistema é uma ferramenta de previsão e não substitui o aconselhamento financeiro profissional. Utilize os resultados como uma referência adicional para suas decisões financeiras.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Não foi possível carregar as animações.")

if __name__ == "__main__":
    show()
