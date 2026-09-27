"""Funciones de limpieza del proyecto."""
import numpy as np
import pandas as pd

def limpiar(df: pd.DataFrame) -> pd.DataFrame:    
    """Quita duplicados, atípicos extremos del ingreso (> Q3 + 3·IQR) y nulos."""
    df = df.drop_duplicates(subset="id_persona")
    q1, q3 = df["ingreso"].quantile([.25, .75])
    df = df[(df["ingreso"].isna()) | (df["ingreso"] <= q3 + 3 * (q3 - q1))]
    df = df.dropna(subset=["ingreso", "anios_educ"]).copy()
    return df

def agregar_variables(df: pd.DataFrame) -> pd.DataFrame:    
    """Crea log_ingreso y grupo_edad."""
    df = df.copy()
    df["log_ingreso"] = np.log(df["ingreso"])
    df["grupo_edad"] = pd.cut(df["edad"], bins=[17, 29, 44, 65],
                              labels=["18-29", "30-44", "45-65"])
    return df


def anonimizar(df: pd.DataFrame, sal: str) -> pd.DataFrame:
    """Elimina identificadores directos, seudonimiza la cedula y generaliza edad e ingreso."""
    import hashlib
    df = df.drop(columns=["nombre", "fecha_nac"]).copy()
    df["id_seudonimo"] = df["cedula"].apply(
        lambda c: hashlib.sha256((sal + str(c)).encode("utf-8")).hexdigest()[:12])
    df = df.drop(columns=["cedula", "id_persona"])
    df["rango_edad"] = pd.cut(df["edad"], bins=[10, 20, 30, 40, 50, 60, 70], right=False,
                             labels=["10-19", "20-29", "30-39", "40-49", "50-59", "60-69"])
    df = df.drop(columns=["edad"])
    df["ingreso"] = df["ingreso"].round(-1)
    return df
