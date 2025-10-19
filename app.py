import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Caminho do arquivo de dados
DATA_PATH = "data/estudos.csv"

# Garante que o arquivo exista
if not os.path.exists(DATA_PATH):
    df = pd.DataFrame(columns=["Matéria", "Data", "Horas"])
    df.to_csv(DATA_PATH, index=False)

# Carrega os dados
df = pd.read_csv(DATA_PATH)

st.title("Study Tracker — ODS 4 Educação de Qualidade")
st.write("Acompanhe suas horas de estudo e alcance suas metas semanais!")

# --- Seções do app ---
menu = st.sidebar.radio("Navegação", ["Registrar Estudo", "Ver Gráficos", "Sobre"])

if menu == "Registrar Estudo":
    st.header("Registrar horas de estudo")

    materia = st.text_input("Matéria", placeholder="Ex: Matemática")
    horas = st.number_input("Horas estudadas", min_value=0.0, step=0.5)
    data = st.date_input("Data")

    if st.button("Salvar registro"):
        novo_registro = pd.DataFrame([[materia, data, horas]], columns=["Matéria", "Data", "Horas"])
        df = pd.concat([df, novo_registro], ignore_index=True)
        df.to_csv(DATA_PATH, index=False)
        st.success("Registro salvo com sucesso!")

elif menu == "Ver Gráficos":
    st.header("Gráficos de Estudo")

    if df.empty:
        st.warning("Nenhum dado registrado ainda!")
    else:
        materia_sel = st.selectbox("Selecione a matéria", options=["Todas"] + df["Matéria"].dropna().unique().tolist())

        if materia_sel != "Todas":
            dados_filtrados = df[df["Matéria"] == materia_sel]
        else:
            dados_filtrados = df

        # Gráfico simples de horas por data
        if not dados_filtrados.empty:
            fig, ax = plt.subplots()
            dados_filtrados.groupby("Data")["Horas"].sum().plot(kind="bar", ax=ax)
            ax.set_title("Horas de Estudo por Dia")
            ax.set_xlabel("Data")
            ax.set_ylabel("Horas")
            st.pyplot(fig)
        else:
            st.info("Sem dados para essa matéria.")

elif menu == "Sobre":
    st.header("Sobre o Projeto")
    st.write("""
    Este sistema foi desenvolvido para apoiar estudantes na organização do tempo de estudo,
    contribuindo com o **ODS 4 - Educação de Qualidade**.
    
    **Funções atuais:**
    - Registrar horas estudadas
    - Visualizar gráficos de progresso
    - Armazenar dados localmente em CSV
    
    **Próximos passos (TP4):**
    - Adicionar metas semanais
    - Criar alertas e relatórios automáticos
    """)
