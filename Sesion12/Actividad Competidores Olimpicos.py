# Actividad: Competidores Olímpicos
# Actividad: Básica

import pandas as pd
import numpy as np

datos = pd.read_csv("C:\\Users\\vmachuca\\Documents\\Python_Fundamentals\\Sesion12\\athlete_events.csv")

# Competidor más veterano que ha recibido medalla (oro, plata o bronce)
datos1 = datos[datos["Medal"].notna()]
datos1 = datos1[datos1["Age"]==datos1["Age"].max()]
print("Jugador mas veterano que ha ganado medalla es:")
print(datos1)

# Competidor más joven que ha recibido medalla de oro
datos2 = datos[datos["Medal"]=="Gold"]
datos2 = datos2[datos2["Age"]==datos2["Age"].min()]
print("Los jugadores mas jovenes que han ganado medalla de oro son:")
print(datos2)

# Competidor más ganador de la historia y crea un csv con toda su información.
datos[datos["Medal"].notna()]["Name"].value_counts()
datos3 = datos[datos["Name"]=="Michael Fred Phelps, II"]
datos3.to_csv("C:\\Users\\vmachuca\\Documents\\Python_Fundamentals\\Sesion12\\medallistas.csv",header=True,index=True)