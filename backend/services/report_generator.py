class ReportGenerator:
    def __init__(self):
        pass

    def generate_markdown_report(self, lineage_data):
        report = "# Data Lineage Report\n\n"
        report += "## Overview\n"
        report += "This report provides an overview of the data lineage.\n\n"
        
        for item in lineage_data:
            report += f"### {item['name']}\n"
            report += f"- **Type:** {item['type']}\n"
            report += f"- **Source:** {item['source']}\n"
            report += f"- **Dependencies:** {', '.join(item['dependencies'])}\n\n"
        
        return report

    def save_report_to_file(self, report, file_path):
        with open(file_path, 'w') as file:
            file.write(report)