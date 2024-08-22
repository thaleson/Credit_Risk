import streamlit as st
import numpy as np
import joblib  # Para carregar o modelo salvo

def show(model):
    st.title("Previsão de Crédito")
    st.write("Preencha as informações abaixo para prever a probabilidade de inadimplência do crédito.")

    # Coletar dados de entrada do usuário com descrições mais detalhadas
    LIMIT_BAL = st.number_input("Limite de Crédito (LIMIT_BAL)", min_value=0, help="O valor total do limite de crédito disponível.")
    SEX = st.selectbox("Sexo (SEX)", options=[1, 2], format_func=lambda x: "Masculino" if x == 1 else "Feminino")
    EDUCATION = st.selectbox("Educação (EDUCATION)", options=[1, 2, 3, 4], format_func=lambda x: "Graduação" if x == 1 else "Universitário" if x == 2 else "Ensino Médio" if x == 3 else "Outros")
    MARRIAGE = st.selectbox("Estado Civil (MARRIAGE)", options=[1, 2, 3], format_func=lambda x: "Casado" if x == 1 else "Solteiro" if x == 2 else "Outros")
    AGE = st.number_input("Idade (AGE)", min_value=18, help="Idade do cliente.")
    PAY_0 = st.number_input("Histórico de Pagamento - Mês Atual (PAY_0)", min_value=-2, max_value=8, help="Histórico de pagamento do mês atual (-1: pago, 1: atraso 1 mês, 2: atraso 2 meses, etc.).")
    PAY_2 = st.number_input("Histórico de Pagamento - Mês Anterior (PAY_2)", min_value=-2, max_value=8, help="Histórico de pagamento do mês anterior.")
    PAY_3 = st.number_input("Histórico de Pagamento - Dois Meses Anteriores (PAY_3)", min_value=-2, max_value=8, help="Histórico de pagamento de dois meses atrás.")
    PAY_4 = st.number_input("Histórico de Pagamento - Três Meses Anteriores (PAY_4)", min_value=-2, max_value=8, help="Histórico de pagamento de três meses atrás.")
    PAY_5 = st.number_input("Histórico de Pagamento - Quatro Meses Anteriores (PAY_5)", min_value=-2, max_value=8, help="Histórico de pagamento de quatro meses atrás.")
    PAY_6 = st.number_input("Histórico de Pagamento - Cinco Meses Anteriores (PAY_6)", min_value=-2, max_value=8, help="Histórico de pagamento de cinco meses atrás.")
    BILL_AMT1 = st.number_input("Valor da Fatura - Mês Atual (BILL_AMT1)", min_value=0, help="Valor da fatura do mês atual.")
    BILL_AMT2 = st.number_input("Valor da Fatura - Mês Anterior (BILL_AMT2)", min_value=0, help="Valor da fatura do mês anterior.")
    BILL_AMT3 = st.number_input("Valor da Fatura - Dois Meses Anteriores (BILL_AMT3)", min_value=0, help="Valor da fatura de dois meses atrás.")
    BILL_AMT4 = st.number_input("Valor da Fatura - Três Meses Anteriores (BILL_AMT4)", min_value=0, help="Valor da fatura de três meses atrás.")
    BILL_AMT5 = st.number_input("Valor da Fatura - Quatro Meses Anteriores (BILL_AMT5)", min_value=0, help="Valor da fatura de quatro meses atrás.")
    BILL_AMT6 = st.number_input("Valor da Fatura - Cinco Meses Anteriores (BILL_AMT6)", min_value=0, help="Valor da fatura de cinco meses atrás.")
    PAY_AMT1 = st.number_input("Pagamento - Mês Atual (PAY_AMT1)", min_value=0, help="Pagamento feito no mês atual.")
    PAY_AMT2 = st.number_input("Pagamento - Mês Anterior (PAY_AMT2)", min_value=0, help="Pagamento feito no mês anterior.")
    PAY_AMT3 = st.number_input("Pagamento - Dois Meses Anteriores (PAY_AMT3)", min_value=0, help="Pagamento feito dois meses atrás.")
    PAY_AMT4 = st.number_input("Pagamento - Três Meses Anteriores (PAY_AMT4)", min_value=0, help="Pagamento feito três meses atrás.")
    PAY_AMT5 = st.number_input("Pagamento - Quatro Meses Anteriores (PAY_AMT5)", min_value=0, help="Pagamento feito quatro meses atrás.")
    PAY_AMT6 = st.number_input("Pagamento - Cinco Meses Anteriores (PAY_AMT6)", min_value=0, help="Pagamento feito cinco meses atrás.")

    # Criar um array com todas as características
    features = np.array([[LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
                          BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1, PAY_AMT2,
                          PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6]])

    if st.button("Prever"):
        with st.spinner("Realizando a previsão..."):
            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0][1]

            # Identificar as características mais influentes
            if hasattr(model, 'feature_importances_'):
                importances = model.feature_importances_
                feature_names = ["LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6",
                                 "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2",
                                 "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]
                sorted_indices = np.argsort(importances)[::-1]
                top_features = [(feature_names[i], importances[i] * 100) for i in sorted_indices[:3]]  # Convertendo para porcentagem
                feature_labels = {
                    "LIMIT_BAL": "Limite de Crédito",
                    "SEX": "Sexo",
                    "EDUCATION": "Educação",
                    "MARRIAGE": "Estado Civil",
                    "AGE": "Idade",
                    "PAY_0": "Histórico de Pagamento - Mês Atual",
                    "PAY_2": "Histórico de Pagamento - Mês Anterior",
                    "PAY_3": "Histórico de Pagamento - Dois Meses Anteriores",
                    "PAY_4": "Histórico de Pagamento - Três Meses Anteriores",
                    "PAY_5": "Histórico de Pagamento - Quatro Meses Anteriores",
                    "PAY_6": "Histórico de Pagamento - Cinco Meses Anteriores",
                    "BILL_AMT1": "Valor da Fatura - Mês Atual",
                    "BILL_AMT2": "Valor da Fatura - Mês Anterior",
                    "BILL_AMT3": "Valor da Fatura - Dois Meses Anteriores",
                    "BILL_AMT4": "Valor da Fatura - Três Meses Anteriores",
                    "BILL_AMT5": "Valor da Fatura - Quatro Meses Anteriores",
                    "BILL_AMT6": "Valor da Fatura - Cinco Meses Anteriores",
                    "PAY_AMT1": "Pagamento - Mês Atual",
                    "PAY_AMT2": "Pagamento - Mês Anterior",
                    "PAY_AMT3": "Pagamento - Dois Meses Anteriores",
                    "PAY_AMT4": "Pagamento - Três Meses Anteriores",
                    "PAY_AMT5": "Pagamento - Quatro Meses Anteriores",
                    "PAY_AMT6": "Pagamento - Cinco Meses Anteriores"
                }
            else:
                top_features = []

            # Mostrar o resultado da previsão
            if probability > 0.5:
                st.markdown(
                    f"<h2 style='color:red;'>Sua chance de inadimplência é: {probability * 100:.2f}% (Alta)</h2>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    "<div style='background-color: #f8d7da; padding: 10px; border-radius: 5px;'>"
                    "<p style='color: #721c24;'>⚠️ Seu risco de inadimplência é alto. É essencial tomar medidas para melhorar sua situação financeira. Considere revisar seus gastos e buscar orientação financeira.</p>"
                    "</div>", unsafe_allow_html=True
                )
                if top_features:
                    st.write("### 🔍 Indicadores Principais:")
                    for feature, importance in top_features:
                        st.write(f"- **{feature_labels.get(feature, feature)}**: {importance:.2f}%")

            elif 0.2 < probability <= 0.5:
                st.markdown(
                    f"<h2 style='color:orange;'>Sua chance de inadimplência é: {probability * 100:.2f}% (Média)</h2>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    "<div style='background-color: #fff3cd; padding: 10px; border-radius: 5px;'>"
                    "<p style='color: #856404;'>⚠️ Seu risco de inadimplência é médio. Continue monitorando suas finanças e evite gastos desnecessários. Mantenha um bom histórico financeiro para reduzir o risco.</p>"
                    "</div>", unsafe_allow_html=True
                )
                if top_features:
                    st.write("### 🔍 Indicadores Principais:")
                    for feature, importance in top_features:
                        st.write(f"- **{feature_labels.get(feature, feature)}**: {importance:.2f}%")

            else:
                st.markdown(
                    f"<h2 style='color:green;'>Sua chance de inadimplência é: {probability * 100:.2f}% (Baixa)</h2>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    "<div style='background-color: #d4edda; padding: 10px; border-radius: 5px;'>"
                    "<p style='color: #155724;'>✅ Seu risco de inadimplência é baixo. Continue mantendo um bom histórico financeiro. Isso pode ajudar a melhorar sua situação financeira a longo prazo.</p>"
                    "</div>", unsafe_allow_html=True
                )
                if top_features:
                    st.write("### 🔍 Indicadores Principais:")
                    for feature, importance in top_features:
                        st.write(f"- **{feature_labels.get(feature, feature)}**: {importance:.2f}%")
