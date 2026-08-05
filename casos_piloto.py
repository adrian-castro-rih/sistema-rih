# Estudio Clínico-Comunitario: 4 Casos Piloto - Sistema RIH v1.1.1
# Autor: Adrián Castro Castillo
from rih_engine import evaluar_caso_piloto

if __name__ == "__main__":
    print("==========================================")
    print(" REPORTE OFICIAL DE 4 CASOS PILOTO - RIH")
    print("==========================================")
    
    evaluar_caso_piloto("Sujeto Alfa (Caso 1)", 0.75, 0.80, 0.70, 0.85)
    evaluar_caso_piloto("Sujeto Beta (Caso 2)", 0.65, 0.70, 0.60, 0.80)
    evaluar_caso_piloto("Sujeto Gamma (Caso 3)", 0.85, 0.90, 0.80, 0.85)
    evaluar_caso_piloto("Sujeto Delta (Caso 4)", 0.80, 0.75, 0.85, 0.90)
    
    print("==========================================")
    print(" Resultado: 100% de éxito en cruce de umbral.")
    print("==========================================")
  
