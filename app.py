from flask import Flask, request, jsonify, render_template
from intent_detection import detect_intent
from response_generator import generate_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_query = request.json.get('query')
        intent = detect_intent(user_query)
        response = generate_response(intent)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
