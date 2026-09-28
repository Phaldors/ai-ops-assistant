from langchain_core.tools import tool
import joblib

model = joblib.load("maintenance_model.pkl")


@tool
def ariza_tahmini(sicaklik: float, titresim: float, bakimdan_gecen_saat: float) -> str:
    """Bir makinenin sicaklik, titresim ve bakimdan gecen saat verisine gore
    ariza riskini tahmin eder."""
    tahmin = model.predict([[sicaklik, titresim, bakimdan_gecen_saat]])
    if tahmin[0] == 1:
        return "ARIZA RISKI YUKSEK - bakim onerilir"
    return "Normal, ariza riski dusuk"