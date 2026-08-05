# Motor RIH v1.1.1 - ICI v2.0 y Métricas de Restauración
# Autor e Inventor: Adrián Castro Castillo

def calcular_ici(identidad, valores, conducta, proposito):
    """
    Calcula el Índice de Consistencia Identitaria (ICI v2.0).
    Escala de 0 a 1 (o 1 a 5 normalizado). Umbral de Soberanía >= 0.60
    """
    promedio = (identidad + valores + conducta + proposito) / 4.0
    estado = "SOBERANO" if promedio >= 0.60 else "CRIAPLE"
    return {"ici": round(promedio, 2), "estado": estado}

def evaluar_caso_piloto(nombre, identidad, valores, conducta, proposito):
    resultado = calcular_ici(identidad, valores, conducta, proposito)
    print(f"[AUDITORÍA RIH] Sujeto: {nombre} | ICI: {resultado['ici']} | Estado: {resultado['estado']}")
    return resultado

if __name__ == "__main__":
    print("Motor RIH inicializado correctamente.")
  
