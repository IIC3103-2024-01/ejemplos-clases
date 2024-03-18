from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/servicio", methods=['GET', 'POST'])
def servicio():
    args = request.args
    action = args.get('action')

    if action == 'suma':
        data = request.json

        return data.get('sum1') + data.get('sum2')
    
    else:
        return 'Error', 400
