# Pruebas de Estrés y Validación - Sistema RIH
from rih_engine import calcular_ici

def test_umbral_soberania():
    res = calcular_ici(0.8, 0.85, 0.75, 0.9)
    assert res["estado"] == "SOBERANO", f"Error: Se esperaba SOBERANO, obtuvo {res['estado']}"
    print("[TEST PASADO] El umbral de soberanía funciona correctamente.")

def test_umbral_supervivencia():
    res = calcular_ici(0.4, 0.5, 0.45, 0.5)
    assert res["estado"] == "CRIAPLE", f"Error: Se esperaba CRIAPLE, obtuvo {res['estado']}"
    print("[TEST PASADO] La detección de supervivencia funciona correctamente.")

if __name__ == "__main__":
    print("Ejecutando pruebas unitarias del sistema RIH...")
    test_umbral_soberania()
    test_umbral_supervivencia()
    print("Todas las pruebas pasaron con éxito.")
  
