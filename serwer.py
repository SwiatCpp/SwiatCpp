from flask import Flask, request, render_template_string, send_file, redirect, url_for

app = Flask(__name__)

# Strona główna z formularzem skargi
@app.route('/')
def home():
    return '''
    <h1>Świat C++</h1>
    <p>Masz problem z programem? Napisz skargę!</p>
    <form action="/skarga" method="post">
        <input type="text" name="tresc" placeholder="Napisz swoją skargę" required>
        <button type="submit">Wyślij skargę</button>
    </form>
    <p><a href="/pobierz_skargi">Pobierz wszystkie skargi</a></p>
    '''

# Odbieranie formularza i zapisywanie do pliku
@app.route('/skarga', methods=['POST'])
def skarga():
    tresc = request.form['tresc']
    with open('skargi.txt', 'a', encoding='utf-8') as f:
        f.write(tresc + '\n')
    return '''
    <p>Dziękujemy za zgłoszenie!</p>
    <p><a href="/">Wróć do strony głównej</a></p>
    '''

# Pobieranie pliku skargi.txt
@app.route('/pobierz_skargi')
def pobierz_skargi():
    try:
        return send_file('skargi.txt', as_attachment=True)
    except Exception:
        return '<p>Plik skargi.txt jeszcze nie istnieje.</p><p><a href="/">Wróć</a></p>'

if __name__ == '__main__':
    app.run(debug=False)