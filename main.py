from flask import Flask, render_template

app = Flask(__name__)

mahsulotlar = ["Noutbuk", "Telefon", "Planshet", "Qulaqchin", "Kamera"]



@app.route('/mahsulot/<int:indeks>')
def mahsulot_detail(indeks):
    if 0 <= indeks < len(mahsulotlar):
        nom = mahsulotlar[indeks]
    else:
        nom = 'Bunday mahsulot mavjud emas'

    return render_template('detail.html', nom=nom)



if __name__ == '__main__':
    app.run(debug=True)
