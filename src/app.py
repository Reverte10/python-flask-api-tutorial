from flask import Flask, jsonify, request

app = Flask("Reverte")

todos = [{"label": "My first task", "done": True },
         {"label": "My second task", "done": True }]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    json_text = jsonify(todos)
    return json_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)