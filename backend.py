import pandas as pd
import datetime as dt
import os

def carregar_dados(path):
    """Lê o CSV. Se não existir, cria um vazio."""
    if not os.path.exists(path):
        df = pd.DataFrame(columns=["Matéria", "Data", "Horas"])
        df.to_csv(path, index=False)
    else:
        df = pd.read_csv(path)
    return df

def salvar_dados(path, materia, data, horas):
    """Registra estudo no CSV."""
    df = carregar_dados(path)
    novo = pd.DataFrame([[materia, data, horas]], columns=["Matéria", "Data", "Horas"])
    df = pd.concat([df, novo], ignore_index=True)
    df.to_csv(path, index=False)

def calcular_horas_semana(df):
    """Retorna total de horas estudadas na semana atual."""
    if df.empty:
        return 0.0
    
    df["Data"] = pd.to_datetime(df["Data"])
    
    hoje = dt.date.today()
    inicio = hoje - dt.timedelta(days=hoje.weekday())  # segunda-feira
    fim = inicio + dt.timedelta(days=6)               # domingo
    
    semana = df[
        (df["Data"].dt.date >= inicio) &
        (df["Data"].dt.date <= fim)
    ]
    
    return semana["Horas"].sum()
