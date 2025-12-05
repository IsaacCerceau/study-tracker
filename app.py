import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from backend import carregar_dados, salvar_dados, calcular_horas_semana

# Caminho do arquivo de dados
DATA_PATH = "data/estudos.csv"

# Carrega os dados (ou cria automaticamente)
df = carregar_dados(DATA_PATH)

st.title("📘 Study Tracker — ODS 4 Educação de Qualidade")
st.write("Acompanhe suas horas de estudo, visualize progresso e atinja suas metas semanais!")

# --- Menu lateral ---
menu = st.sidebar.radio(
    "Navegação",
    ["Registrar Estudo", "Ver Gráficos", "Metas Semanais", "Sobre"]
)

# ------------------ Registrar ------------------
if menu == "Registrar Estudo":
    st.header("✍️ Registrar horas de estudo")

    materia = st.text_input("Matéria", placeholder="Ex: Matemática")
    horas = st.number_input("Horas estudadas", min_value=0.0, step=0.5)
    data = st.date_input("Data")

    if st.button("Salvar registro"):
        if materia.strip() == "" or horas <= 0:
            st.error("Preencha a matéria e informe horas maiores que zero.")
        else:
            salvar_dados(DATA_PATH, materia, data, horas)
            df = carregar_dados(DATA_PATH)  # recarrega
            st.success("Registro salvo com sucesso! ✔️")

# ------------------ Gráficos ------------------
elif menu == "Ver Gráficos":
    st.header("📊 Gráficos de Estudo")

    if df.empty:
        st.warning("Nenhum dado registrado ainda!")
    else:
        materia_sel = st.selectbox(
            "Selecione a matéria",
            ["Todas"] + df["Matéria"].dropna().unique().tolist()
        )

        if materia_sel != "Todas":
            dados = df[df["Matéria"] == materia_sel]
        else:
            dados = df

        if not dados.empty:
            fig, ax = plt.subplots()
            dados.groupby("Data")["Horas"].sum().plot(kind="bar", ax=ax)
            ax.set_title("Horas de Estudo por Dia")
            ax.set_xlabel("Data")
            ax.set_ylabel("Horas")
            st.pyplot(fig)
        else:
            st.info("Sem dados dessa matéria.")

# ---------------- Metas Semanais -----------------
elif menu == "Metas Semanais":
    st.header("🎯 Metas Semanais")

    meta = st.number_input(
        "Defina sua meta semanal (em horas):",
        min_value=1.0,
        step=1.0,
        value=10.0
    )

    horas_semana = calcular_horas_semana(df)

    # Indicadores
    col1, col2 = st.columns(2)
    col1.metric("Horas estudadas na semana", f"{horas_semana:.1f}")
    col2.metric("Meta semanal", f"{meta:.1f}")

    progresso = horas_semana / meta if meta > 0 else 0

    st.progress(min(progresso, 1.0))

    # Alertas
    if horas_semana == 0:
        st.info("Nenhum registro de estudo nesta semana.")
    elif horas_semana < meta:
        st.warning("⚠️ Você ainda não atingiu sua meta semanal. Continue estudando!")
    else:
        st.success("🎉 Parabéns! Você atingiu ou superou sua meta semanal!")

# ---------------- Sobre ------------------
elif menu == "Sobre":
    st.header("ℹ️ Sobre o Projeto")
    st.write("""
    Aplicação desenvolvida para apoiar estudantes na organização do tempo de estudo,
    contribuindo com o **ODS 4 – Educação de Qualidade**.

    **Funções atuais:**
    - Registro de horas de estudo
    - Visualização de gráficos por matéria e por dia
    - Definição de meta semanal
    - Barra de progresso
    - Alertas motivacionais

    Dados armazenados localmente em CSV.
    """)
