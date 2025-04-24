from flask import Flask, render_template, request, redirect, url_for, send_file, session

app = Flask(__name__)
app.secret_key = 'gizli-anahtar'

# Basit kullanıcı adı ve şifre
KULLANICI = {'admin': '1234'}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        kullanici_adi = request.form['username']
        sifre = request.form['password']
        if kullanici_adi in KULLANICI and KULLANICI[kullanici_adi] == sifre:
            session['username'] = kullanici_adi
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Hatalı giriş")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/download_excel')
def download_excel():
    if 'username' not in session:
        return redirect(url_for('login'))
    return send_file('ip.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
