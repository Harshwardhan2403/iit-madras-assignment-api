from flask import Flask, request, jsonify
from qa_data import qa_data

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def get_answer():
    question = request.form.get('question')
    if question in qa_data:
        return jsonify({"answer": qa_data[question]})
    else:
        return jsonify({"answer": "Question not found."})

if __name__ == '__main__':
    app.run(debug=True)
