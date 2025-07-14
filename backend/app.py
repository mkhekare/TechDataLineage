from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """A simplified endpoint to simulate file processing."""
    # In the future, you would parse the file and generate a real graph.
    lineage_graph = "graph TD;\n    A[Uploaded File] -->|processed| B(Parsed Content);"
    return jsonify({'message': 'File processed successfully', 'lineage': lineage_graph})

@app.route('/')
def serve():
    """Serves the React frontend."""
    return send_from_directory(app.static_folder, 'index.html')

@app.errorhandler(404)
def not_found(e):
    """Handles 404 errors by sending the React app, which can then handle routing."""
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)