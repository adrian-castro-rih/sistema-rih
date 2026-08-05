# ==========================================
# SISTEMA RIH: MOTOR DE AUDITORÍA IDENTITARIA
# Autor: Adrián Castro Castillo
# ==========================================

def calcular_ici(alineacion_mental, ejecucion_diaria):
    """Calcula el Índice de Coherencia Identitaria (ICI)."""
    return (alineacion_mental * 0.4) + (ejecucion_diaria * 0.6)

def calcular_iif(presion_externa, resistencia_interna):
    """Calcula el Índice de Integridad Funcional (IIF)."""
    if presion_externa == 0:
        return 100.0
    return round((resistencia_interna / presion_externa) * 100, 2)

if __name__ == "__main__":
    print("=== AUDITORÍA DEL SISTEMA MASTER (RIH) ===")
    
    # Ejemplo de prueba de trinchera
    mental = float(input("Ingrese nivel de alineación mental (0-100): "))
    ejecucion = float(input("Ingrese nivel de ejecución diaria (0-100): "))
    
    ici_resultado = calcular_ici(mental, ejecucion)
    print(f">> Índice de Coherencia Identitaria (ICI): {ici_resultado}%")
    
    if ici_resultado < 50:
        print("[ALERTA] Deriva identitaria detectada. Activar protocolo de trinchera.")
    else:
        print("[ESTABLE] Soberanía identitaria en rango operativo.")
  
