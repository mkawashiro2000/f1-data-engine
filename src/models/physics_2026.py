import numpy as np

def calcular_despliegue_2026(velocidad_kmh):
    """
    Simulación del Modelo B (Reglamento 2026):
    Límite ICE: 350kW | Límite MGU-K: 350kW
    """
    # En 2026, el MGU-K entrega menos potencia a alta velocidad (clipping)
    # para evitar que se agote la batería en rectas largas.
    
    potencia_ice = 350.0  # kW (Fijo en 2026)
    
    if velocidad_kmh > 300:
        # Reducción de potencia eléctrica por encima de 300km/h
        factor_reduccion = 0.5 
        potencia_mguk = 350.0 * factor_reduccion
    else:
        potencia_mguk = 350.0
        
    return potencia_ice + potencia_mguk

if __name__ == "__main__":
    # Prueba rápida de la fórmula
    v = 320
    potencia_total = calcular_despliegue_2026(v)
    print(f"🏎️ A {v} km/h, la potencia total estimada para 2026 es: {potencia_total} kW")
