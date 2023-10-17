from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def strlen():
    data = request.json
    string = data.get("input", "")
    count = len(string)
    return jsonify({"length": count})

if __name__ == '__main__':
    app.run(debug=True)