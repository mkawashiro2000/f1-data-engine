import fastf1
import os

# 1. Configurar dónde se guardan los datos descargados
CACHE_DIR = './data/cache'
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

fastf1.Cache.enable_cache(CACHE_DIR)

def descargar_datos(year, gp, session_type='R'):
    print(f"📥 Descargando: {year} {gp}...")
    
    # Cargar la sesión de F1
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    
    # Definir la ruta de salida (Capa Bronce)
    ruta_archivo = f"data/bronze/{year}_{gp}_{session_type}.parquet"
    
    # Guardar los datos de las vueltas
    session.laps.to_parquet(ruta_archivo)
    print(f"✅ Archivo guardado en: {ruta_archivo}")

if __name__ == "__main__":
    descargar_datos(2024, 'Bahrain')
