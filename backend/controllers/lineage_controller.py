from flask import Blueprint, request, jsonify
from models.ast_parser import ASTParser
from models.nlp_processor import NLPProcessor
from models.graph_builder import GraphBuilder
from services.report_generator import ReportGenerator

lineage_bp = Blueprint('lineage', __name__)

@lineage_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file provided'}), 400

    # Process the uploaded file
    ast_parser = ASTParser()
    nlp_processor = NLPProcessor()
    graph_builder = GraphBuilder()

    code_data = ast_parser.parse(file)
    data_flow_patterns = nlp_processor.process_comments(code_data)
    lineage_graph = graph_builder.build_graph(code_data, data_flow_patterns)

    return jsonify({'message': 'File processed successfully', 'lineage': lineage_graph}), 200

@lineage_bp.route('/report', methods=['GET'])
def get_report():
    report_generator = ReportGenerator()
    report = report_generator.generate_report()

    return jsonify({'report': report}), 200

def register_routes(app):
    app.register_blueprint(lineage_bp, url_prefix='/lineage')