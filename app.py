from flask import Flask
from scrap import scrape_top_animes
from email_sender import send_email

app = Flask(__name__)

@app.route("/")
def index():
    dados = scrape_top_animes()
    send_email("📩 Seus animes do dia!", dados, "DESTINATARIO@gmail.com")  # <-- Troque aqui
    return "✅ Email enviado com sucesso!"

if __name__ == "__main__":
    app.run(debug=True)
