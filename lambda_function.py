from flask import Flask, jsonify
import sys

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from AWS Lambda with containers!'})

def handler(event, context):
    return 'what the heaven from AWS Lambda using Python' + sys.version + '!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

