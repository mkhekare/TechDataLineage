from flask import Flask
from controllers.lineage_controller import LineageController

def create_app():
    app = Flask(__name__)

    # Initialize the LineageController
    lineage_controller = LineageController()

    # Set up routes
    app.add_url_rule('/upload', view_func=lineage_controller.upload_file, methods=['POST'])
    app.add_url_rule('/lineage-report', view_func=lineage_controller.get_lineage_report, methods=['GET'])

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)