from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/programy.html')
def programy():
    return send_file('programy.html')

@app.route('/starsze.html')
def starsze():
    return send_file('starsze.html')

@app.route('/skargi_form', methods=['GET', 'POST'])
def skargi_form():
    if request.method == 'POST':
        tresc = request.form['tresc']
        with open('skargi.txt', 'a', encoding='utf-8') as f:
            f.write(tresc + '\n')
        return '''
        <p>Dziękujemy za zgłoszenie!</p>
        <button onclick="window.location.href='programy.html'">Wróć do Programy do pobrania</button>
        <br>
        <button onclick="window.location.href='index.html'">Wróć do strony głównej</button>
        '''
    else:
        return send_file('skargi_form.html')

@app.route('/sekretny_link_do_skarg_123abc')
def pobierz_skargi():
    try:
        return send_file('skargi.txt', as_attachment=True)
    except Exception:
        return '<p>Plik skargi.txt jeszcze nie istnieje.</p>'

if __name__ == '__main__':
    app.run(debug=False)
