import os

def generate():
    links = []
    # Busca recursiva em todas as pastas
    for root, dirs, files in os.walk("."):
        # Ignora apenas a pasta interna do Git
        if ".git" in root:
            continue
            
        for file in files:
            # Verifica .html ou .HTML
            if file.lower().endswith(".html") and file != "index.html":
                # Cria o caminho relativo correto para o link
                path = os.path.join(root, file).replace("./", "")
                links.append(f'<li><a href="{path}">{path}</a></li>')
    
    # Se não encontrar nada, avisa no HTML
    if not links:
        content = "<html><body style='background:#1a1b26;color:white;'><h1>Nenhum HTML encontrado!</h1></body></html>"
    else:
        links_html = "\n".join(sorted(links))
        content = f"""
        <html>
        <body style="background:#1a1b26; color:#a9b1d6; font-family:monospace; padding:50px;">
            <h1 style="color:#ff9e64;">Indice de Arquivos</h1>
            <ul>{links_html}</ul>
        </body>
        </html>
        """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate()
