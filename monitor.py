import requests
import sys

# La web que queremos vigilar
URL = "https://www.google.com"

def comprobar_web():
    print(f"--- Iniciando test sobre {URL} ---")
    
    try:
        # Hacemos una petición GET (como entrar con el navegador)
        respuesta = requests.get(URL)
        
        # El código 200 significa "Todo OK"
        if respuesta.status_code == 200:
            print("✅ ÉXITO: La web está online y responde.")
            return True
        else:
            print(f"⚠️ ALERTA: La web respondió con código {respuesta.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ ERROR CRÍTICO: No se pudo conectar. {e}")
        return False

if __name__ == "__main__":
    exito = comprobar_web()
    
    # Esto es clave para el Pipeline:
    # Si salimos con sys.exit(1), el Pipeline se pondrá ROJO (fallo).
    # Si salimos con sys.exit(0), se pondrá VERDE (éxito).
    if exito:
        sys.exit(0)
    else:
        sys.exit(1)
