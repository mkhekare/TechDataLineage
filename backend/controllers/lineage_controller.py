from flask import Blueprint, request, jsonify
from models.graph_builder import GraphBuilder

lineage_bp = Blueprint('lineage', __name__)

@lineage_bp.route('/upload', methods=['POST'])
def upload_file():
    # This is a simplified placeholder. In a real scenario, you would
    # process the file and generate a graph definition.
    graph_builder = GraphBuilder()
    graph_builder.add_node("A", label="Uploaded File")
    graph_builder.add_node("B", label="Parsed Content")
    graph_builder.add_edge("A", "B", label="processed")
    
    # For now, we'll return a hardcoded Mermaid graph definition
    lineage_graph = "graph TD;\n    A[Uploaded File] -->|processed| B(Parsed Content);"
    
    return jsonify({'message': 'File processed successfully', 'lineage': lineage_graph}), 200

@lineage_bp.route('/report', methods=['GET'])
def get_report():
    # This endpoint can be expanded later
    report = "# Data Lineage Report\n\nThis is a sample report."
    return jsonify({'report': report}), 200

def register_routes(app):
    app.register_blueprint(lineage_bp, url_prefix='/lineage')