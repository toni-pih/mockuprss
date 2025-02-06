from flask import Flask, Response
from feedgen.feed import FeedGenerator

app = Flask(__name__)

def generate_rss():
    fg = FeedGenerator()
    fg.title("Mi Feed RSS de Ejemplo")
    fg.link(href="https://tu-sitio.com/rss")
    fg.description("Este es un ejemplo de feed RSS generado con Python.")

    # Agregar elementos al feed
    entry = fg.add_entry()
    entry.title("Primer artículo")
    entry.link(href="https://tu-sitio.com/articulo1")
    entry.description("Este es el primer artículo de prueba en nuestro feed.")

    entry2 = fg.add_entry()
    entry2.title("Segundo artículo")
    entry2.link(href="https://tu-sitio.com/articulo2")
    entry2.description("Este es el segundo artículo de prueba.")

    return fg.rss_str(pretty=True)

@app.route("/rss")
def rss_feed():
    rss_content = generate_rss()
    return Response(rss_content, mimetype="application/rss+xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
