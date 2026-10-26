"""
server.py
=========
Servidor local para el Generador de Modelos Dimensionales en Estrella.
Evita la caché del navegador para cargar siempre el nuevo diseño idéntico a las capturas.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import time

DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Desactiva la caché del navegador para que siempre descargue la versión nueva
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0, post-check=0, pre-check=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run():
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True

    # Probamos puertos limpios primero para no chocar con caché vieja de navegadores
    preferred_ports = [8050, 8080, 8000, 8888]
    httpd = None
    active_port = 8050

    for port in preferred_ports:
        try:
            httpd = socketserver.TCPServer(("", port), NoCacheHandler)
            active_port = port
            break
        except OSError:
            continue

    if httpd is None:
        print("[AVISO] Los puertos de red estaban ocupados. Abriendo el archivo directamente...")
        index_file = os.path.join(DIRECTORY, "index.html")
        webbrowser.open(f"file:///{index_file.replace(os.sep, '/')}")
        return

    # Usamos un parámetro timestamp para que el navegador ignore cualquier caché previa
    timestamp = int(time.time())
    url = f"http://localhost:{active_port}/index.html?v={timestamp}"

    print("============================================================")
    print("  GENERADOR DE MODELOS DIMENSIONALES EN ESTRELLA")
    print("============================================================")
    print(f"  Servidor activo en: {url}")
    print("  Abriendo tu navegador con el nuevo diseno...")
    print("  (Presiona Ctrl+C en esta consola para detener)")
    print("============================================================")

    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido correctamente.")
        sys.exit(0)

if __name__ == "__main__":
    run()
