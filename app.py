from flask import Flask, request, jsonify
from qa_data import qa_pairs
from difflib import get_close_matches

app = Flask(__name__)

def get_best_match(question):
    questions = list(qa_pairs.keys())
    matches = get_close_matches(question, questions, n=1, cutoff=0.5)  # Adjust cutoff for sensitivity
    if matches:
        return matches[0]
    return None

@app.route('/api/', methods=['POST'])
def get_answer():
    question = request.form.get('question')
    print(f"Received question: {question}")
    
    best_match = get_best_match(question)
    
    if best_match:
        answer = qa_pairs[best_match]
        return jsonify({"answer": answer})
    else:
        return jsonify({"answer": "Question not found."})

if __name__ == '__main__':
    app.run(debug=True)
