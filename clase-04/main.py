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


language = "ES"

def translate(text, language):
    return f"{text} traducido a {language}"

@app.route("/translations/stateful")
def conversation_stateful():
    global language
    text = request.args.get('text')
    if not text:
        return {"error": "missing text"}

    return {
        "translation": translate(text, language)
    }


@app.route("/translations/stateless")
def conversation_stateless():
    text = request.args.get('text')
    language = request.args.get('language')

    if not text:
        return {"error": "missing text"}
    elif not language:
        return {"error": "missing language"}

    return {
        "translation": translate(text, language)
    }

