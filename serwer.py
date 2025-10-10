from flask import Flask, request, send_file
import datetime
import os

app = Flask(__name__)

# Funkcja do serwowania plików HTML z bieżącego folderu
def html(filename):
    return send_file(os.path.join(os.getcwd(), filename))

@app.route('/')
def index():
    return html('index.html')

@app.route('/programy.html')
def programy():
    return html('programy.html')

@app.route('/starsze.html')
def starsze():
    return html('starsze.html')

@app.route('/skarga.html')
def skarga():
    return html('skarga.html')

@app.route('/skarga', methods=['POST'])
def zapisz_skarge():
    nazwa = request.form.get('nazwa_programu', 'Nie podano')
    tresc = request.form.get('wiadomosc', 'Brak treści')
    czas = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('skargi.txt', 'a', encoding='utf-8') as plik:
        plik.write(f"[{czas}] {nazwa}: {tresc}\n")

    return "<h2>Dziękujemy! Skarga została zapisana.</h2><a href='/programy.html'>Powrót</a>"

if __name__ == "__main__":
    app.run(port=5000)