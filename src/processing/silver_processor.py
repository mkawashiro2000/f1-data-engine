import pandas as pd
import numpy as np
import fastf1
import os

# 1. Configurar la misma caché que en el paso de Ingesta
CACHE_DIR = './data/cache'
fastf1.Cache.enable_cache(CACHE_DIR)

def procesar_a_plata(year, gp, session_type='R'):
    print(f"🥈 Procesando Capa Plata: {year} {gp} ({session_type})")
    
    # 2. Cargar la sesión (FastF1 la tomará de la caché, será instantáneo)
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    
    # 3. Ahora sí tenemos los "superpoderes"
    # Filtrado (Sección 1.B): Solo vueltas rápidas
    quick_laps = session.laps.pick_quicklaps(threshold=1.07)
    
    # Tomar la vuelta más rápida de la sesión
    fastest_lap = quick_laps.pick_fastest()
    
    # Obtener telemetría de esa vuelta
    telemetry = fastest_lap.get_telemetry()

    # 4. Interpolación (Sección 1.B de tu doc)
    # Eje de distancia común con 5000 puntos
    distancia_comun = np.linspace(0, telemetry['Distance'].max(), 5000)

    # Interpolamos velocidad y acelerador
    velocidad_interp = np.interp(distancia_comun, telemetry['Distance'], telemetry['Speed'])
    throttle_interp = np.interp(distancia_comun, telemetry['Distance'], telemetry['Throttle'])

    # Crear el DataFrame de la Capa Plata
    df_silver = pd.DataFrame({
        'Distance': distancia_comun,
        'Speed': velocidad_interp,
        'Throttle': throttle_interp
    })

    # 5. Guardar el resultado
    ruta_salida = f"data/silver/{year}_{gp}_{session_type}_silver.parquet"
    df_silver.to_parquet(ruta_salida)
    
    print(f"✅ Capa Plata generada con éxito en: {ruta_salida}")

if __name__ == "__main__":
    # Procesamos los mismos datos que bajamos en Bronce
    procesar_a_plata(2024, 'Bahrain')
