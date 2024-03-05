from flask import Flask, render_template, request, jsonify
from pysimplestplus import run_lexical, run_syntax

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        code = request.form.get('editorContent', '')
        analyzer = request.form.get('analyzer', '')

        if analyzer == 'lexical':
            tokens, errors = run_lexical('', code)
            data = {
                'tokens': [[token.lexeme_str(), token.token_type_str()] for token in tokens],
                'errors': [error.as_string() for error in errors]
            }
            print(jsonify(data))
            return jsonify(data)
        elif analyzer == 'syntax':
            tokens, nodes, errors = run_syntax('', code)
            data = {
                'tokens': [[token.lexeme_str(), token.token_type_str()] for token in tokens],
                'errors': [error.as_string() for error in errors] if errors else []
            }
            print(data)
            return jsonify(data)


app.run(debug=True)
