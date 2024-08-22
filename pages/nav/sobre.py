import streamlit as st

def show():
    st.title("🌟 Sobre o Projeto 🌟")

    st.write("""
    **Bem-vindo ao nosso sistema de previsão de inadimplência!** 🎉

    O objetivo deste projeto é fornecer uma ferramenta útil para prever a probabilidade de inadimplência de clientes com base em dados financeiros. Utilizamos técnicas avançadas de aprendizado de máquina para criar um modelo preciso e confiável.

    ### 🎯 Objetivo
    O **principal objetivo** deste projeto é avaliar o risco de inadimplência de clientes, ajudando a tomar decisões mais informadas sobre concessão de crédito e gerenciamento de risco.

    ### 🔍 Metodologia
    1. **Coleta de Dados**: Reunimos um conjunto de dados real contendo informações financeiras detalhadas de clientes. Esses dados incluem:
        - Limite de crédito 💳
        - Histórico de pagamentos 📅
        - Valores de fatura e pagamentos realizados 💸

    2. **Pré-processamento**: Os dados foram cuidadosamente preparados e limpos para garantir precisão, incluindo normalização e tratamento de valores ausentes.

    3. **Treinamento do Modelo**: Utilizamos o algoritmo **Random Forest** 🌲, conhecido por sua eficácia em classificações. O modelo foi treinado com dados reais e alcançou uma acurácia de **81%**, mostrando-se eficaz na previsão de inadimplência.

    4. **Avaliação e Validação**: O desempenho do modelo foi avaliado com métricas específicas para garantir sua confiabilidade e utilidade.

    5. **Implementação**: Integrado a um sistema interativo, você pode facilmente inserir dados financeiros e obter uma previsão sobre o risco de inadimplência. A interface é intuitiva e fácil de usar.

    ### 🛠️ Como Funciona
    - **Entrada de Dados**: Insira informações financeiras como limite de crédito, histórico de pagamentos e valores de fatura.
    - **Previsão**: O modelo analisa os dados e calcula a probabilidade de inadimplência.
    - **Resultado**: Receba uma avaliação clara do risco, indicando se há baixa, média ou alta probabilidade de inadimplência.

    ### 💡 Importância
    Este projeto é uma **ferramenta valiosa** para instituições financeiras e indivíduos. Ele oferece uma análise detalhada do risco de crédito, ajudando a minimizar os riscos associados à concessão de crédito e a tomar decisões mais fundamentadas.

    **Se tiver dúvidas ou precisar de mais informações, não hesite em nos contatar!** 📩
    """)

