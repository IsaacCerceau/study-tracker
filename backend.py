import pandas as pd
import datetime as dt
import os

def carregar_dados(path):
    if not os.path.exists(path):
        df = pd.DataFrame(columns=["Matéria", "Data", "Horas"])
        df.to_csv(path, index=False)
    else:
        df = pd.read_csv(path)
    return df

def salvar_dados(path, materia, data, horas):
    df = carregar_dados(path)
    novo = pd.DataFrame([[materia, data, horas]], columns=["Matéria", "Data", "Horas"])
    df = pd.concat([df, novo], ignore_index=True)
    df.to_csv(path, index=False)

def calcular_progresso(df):
    if df.empty:
        return 0, 0
    df["Data"] = pd.to_datetime(df["Data"])
    hoje = dt.date.today()
    inicio_semana = hoje - dt.timedelta(days=hoje.weekday())
    fim_semana = inicio_semana + dt.timedelta(days=6)
    semana = df[(df["Data"].dt.date >= inicio_semana) & (df["Data"].dt.date <= fim_semana)]
    horas_semana = semana["Horas"].sum()
    return horas_semana, horas_semana
