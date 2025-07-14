from flask import Flask, send_from_directory
from controllers.lineage_controller import LineageController

def create_app():
    app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

    # Initialize the LineageController
    lineage_controller = LineageController()

    # Set up routes
    app.add_url_rule('/upload', view_func=lineage_controller.upload_file, methods=['POST'])
    app.add_url_rule('/lineage-report', view_func=lineage_controller.get_lineage_report, methods=['GET'])

    @app.route('/')
    def serve():
        return send_from_directory(app.static_folder, 'index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)