from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def generate_random():
    # Default range: 1 to 100
    min_value = request.args.get('min', default=1, type=int)
    max_value = request.args.get('max', default=100, type=int)

    if min_value > max_value:
        return jsonify({
            "error": "min must be less than or equal to max"
        }), 400

    number = random.randint(min_value, max_value)

    return jsonify({
        "random_number": number,
        "min": min_value,
        "max": max_value
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "UP"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

