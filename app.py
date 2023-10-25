from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def strlen():
    data = request.json
    print(data)
    #string = data.get("input")
    #count = len(string)
    #print(string,"=",count)
    #return jsonify({"length": count})

if __name__ == '__main__':
    app.run(debug=True)
