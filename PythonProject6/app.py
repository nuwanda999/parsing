from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    volume = None
    if request.method == 'POST':
        try:
            length = float(request.form.get('length'))
            width = float(request.form.get('width'))
            height = float(request.form.get('height'))
            volume = length * width * height
            volume = round(volume, 2)
        except:
            volume = "Ошибка: введите корректные числа"
    return render_template('index.html', volume=volume)

if __name__ == '__main__':
    app.run(debug=True)
