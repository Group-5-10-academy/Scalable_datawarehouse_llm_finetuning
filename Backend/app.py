from flask import Flask, jsonify

app = Flask(__name__)

# Mock data
mock_data = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Alice", "age": 25},
    {"id": 3, "name": "Bob", "age": 35}
]

# Route to get all mock data
@app.route('/api/mock-data', methods=['GET'])
def get_mock_data():
    return jsonify(mock_data)

# Route to get mock data by ID
@app.route('/api/mock-data/<int:id>', methods=['GET'])
def get_mock_data_by_id(id):
    data = [item for item in mock_data if item['id'] == id]
    if len(data) == 0:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(data[0])

if __name__ == '__main__':
    app.run(debug=True)
