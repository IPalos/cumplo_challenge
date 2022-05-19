import pandas as pd
import numpy as np
import requests
from utils.constants import *

#Configuración inicial de conexión
url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/"
headers = {"Bmx-token":"febbceb34cc8f93a885e46c3302a31da0fe1356a6a46af1e7aa642518c3d6968"}


def get_udis_usd(series, f_inicio, f_fin):
    '''
    Llamada de API que trae los datos de las UDIS y USD, los coloca en un DataFrame y obtiene el promedio, mínimo y máximo de cada dato, dentro de la fecha inicial y final
    '''
    response = requests.get(f"{url}{series}/datos/{f_inicio}/{f_fin}",headers=headers)
    if response.status_code == 200:
        result = response.json()
        if result["bmx"]["series"][0]["idSerie"] == s_udis:
            udi = pd.DataFrame(result["bmx"]["series"][0]["datos"])
            dlr = pd.DataFrame(result["bmx"]["series"][1]["datos"])
        else:
            udi = pd.DataFrame(result["bmx"]["series"][1]["datos"])
            dlr = pd.DataFrame(result["bmx"]["series"][0]["datos"]) 
        df = udi.merge(dlr, on="fecha")
        df[["dato_x","dato_y"]] = df[["dato_x","dato_y"]].astype(np.float64)
        df.rename(columns={"dato_x":"UDIS/MXN", "dato_y":"USD/MXN"}, inplace=True)
        u = df["UDIS/MXN"]
        mean_u = u.mean()
        mi_u = u.min()
        ma_u = u.max()
        d = df["USD/MXN"]
        mean_d = d.mean()
        mi_d = d.min()
        ma_d = d.max()
        return df, (mean_u, mi_u, ma_u), (mean_d, mi_d, ma_d)


def get_tiies(series, f_inicio, f_fin):
    '''
    Llamada de API que obtiene las series de tiempo de diversas TIIEs
    '''
    response = requests.get(f"{url}{series}/datos/{f_inicio}/{f_fin}",headers=headers)
    if response.status_code == 200:
        result = response.json()
        cols = []
        data =[]
        for i in result["bmx"]["series"]:
            cols.append(series_code[i["idSerie"]])
            data.append(i["datos"])

        df = pd.DataFrame(data[0])
        df["dato"] = df["dato"].astype(np.float64)
        df.rename(columns={"dato":cols[0]}, inplace=True)
        for i in range(1,len(data)):
            _=pd.DataFrame(data[i])
            _["dato"]=_["dato"].astype(np.float64)
            _.rename(columns={"dato":cols[i]}, inplace=True)

            df=df.merge(_, on="fecha")
        return df
