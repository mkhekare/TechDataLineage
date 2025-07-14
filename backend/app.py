from flask import Flask, jsonify, send_from_directory, request
import os
import tempfile
import shutil
from git import Repo, GitCommandError

from backend.models.ast_parser import ASTParser
from backend.models.graph_builder import GraphBuilder

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    ast_parser = ASTParser()
    graph_builder = GraphBuilder()
    lineage_graph_definition = "graph TD;\n    Start[No Data Processed]"

    temp_dir = None

    try:
        # Handle file upload
        if 'file' in request.files:
            uploaded_file = request.files['file']
            if uploaded_file.filename == '':
                return jsonify({'error': 'No selected file'}), 400
            if uploaded_file:
                # Save to a temporary file to read content
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.filename)[1]) as tmp_file:
                    uploaded_file.save(tmp_file.name)
                    file_path = tmp_file.name

                parsed_data = ast_parser.parse(file_path)
                os.unlink(file_path) # Clean up temp file immediately

                if "error" in parsed_data:
                    return jsonify({'error': parsed_data["error"]}), 400

                # Build graph from parsed data
                graph_builder.add_node("File", label=f"File: {uploaded_file.filename}")
                if 'functions' in parsed_data:
                    for func in parsed_data['functions']:
                        graph_builder.add_node(f"Func_{func}", label=f"Function: {func}")
                        graph_builder.add_edge("File", f"Func_{func}", label="defines")
                if 'classes' in parsed_data:
                    for cls in parsed_data['classes']:
                        graph_builder.add_node(f"Class_{cls}", label=f"Class: {cls}")
                        graph_builder.add_edge("File", f"Class_{cls}", label="defines")
                if 'variables' in parsed_data:
                    for var in parsed_data['variables']:
                        graph_builder.add_node(f"Var_{var}", label=f"Variable: {var}")
                        graph_builder.add_edge("File", f"Var_{var}", label="uses")

                lineage_graph_definition = graph_builder.to_mermaid()
                return jsonify({'message': 'File processed successfully', 'lineage': lineage_graph_definition})

        # Handle repository link
        repo_link = request.form.get('repo_link')
        if repo_link:
            temp_dir = tempfile.mkdtemp()
            try:
                Repo.clone_from(repo_link, temp_dir)
                
                # Iterate through files in the cloned repo
                parsed_files_count = 0
                for root, _, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # Limit to relevant file types and avoid large files
                        if file_path.endswith(('.py', '.java', '.sql')) and os.path.getsize(file_path) < 1024 * 100: # Max 100KB per file
                            parsed_data = ast_parser.parse(file_path)
                            if "error" not in parsed_data:
                                parsed_files_count += 1
                                # Build graph from parsed data (simplified for now)
                                file_node_id = f"File_{os.path.basename(file_path).replace('.', '_')}"
                                graph_builder.add_node(file_node_id, label=f"File: {os.path.basename(file_path)}")
                                if 'functions' in parsed_data:
                                    for func in parsed_data['functions']:
                                        func_node_id = f"Func_{func}_{file_node_id}"
                                        graph_builder.add_node(func_node_id, label=f"Function: {func}")
                                        graph_builder.add_edge(file_node_id, func_node_id, label="defines")
                                # Add more graph building logic here based on parsed_data

                if parsed_files_count == 0:
                    lineage_graph_definition = "graph TD;\n    Repo[Repository] --> No[No supported files found or processed]"
                else:
                    lineage_graph_definition = graph_builder.to_mermaid()

                return jsonify({'message': f'Repository processed successfully. Parsed {parsed_files_count} files.', 'lineage': lineage_graph_definition})

            except GitCommandError as e:
                return jsonify({'error': f'Git command error: {e}'}), 400
            except Exception as e:
                return jsonify({'error': f'Error processing repository: {e}'}), 500
            finally:
                if temp_dir and os.path.exists(temp_dir):
                    shutil.rmtree(temp_dir)

        return jsonify({'error': 'No file or repository link provided'}), 400

    except Exception as e:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500

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