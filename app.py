import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def fibonacci():
    a = 1
    b = 0
    limite = 49
    count = 0
    saida = "0, "
    while count < limite:
        t = a
        a = a+b
        b = t
        count = count+1
        saida += str(a) + ", "

    return saida


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
