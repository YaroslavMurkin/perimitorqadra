from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/schitat')
def summa():
    a, b, c, d = 0, 0, 0, 0
    if "a" in request.args:
        a = request.args['a']
    if "b" in request.args:
        b = request.args['b']
    if "c" in request.args:
        c = request.args['c']
    if "d" in request.args:
        d = request.args['d']
    m = int(a) + int(c) + int(b) + int(d)
    return render_template('shitchik.html', m=m)


app.run(debug=True, port=8080)
