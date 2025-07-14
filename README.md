# AI-Powered Technical Data Lineage Generator

## Overview
The AI-Powered Technical Data Lineage Generator is an open-source tool designed to visualize and analyze data lineage in codebases. It leverages AI techniques to extract meaningful insights from code, comments, and logs, providing users with a clear understanding of data flow and dependencies.

## Features
- **Code Parsing**: Supports parsing of Python, Java, and SQL code files to extract variables, functions, and classes.
- **NLP Processing**: Utilizes natural language processing to analyze comments and log files, identifying data flow patterns.
- **Graph Visualization**: Constructs and visualizes data lineage graphs using NetworkX and Mermaid.js.
- **Git Integration**: Allows users to analyze code from Git repositories, providing insights into committed changes.
- **Report Generation**: Generates detailed Markdown reports summarizing the data lineage.

## Technical Architecture
- **Backend**: Built with Python using Flask for the API, with various modules for parsing, processing, and generating reports.
- **Frontend**: Developed with React, providing a user-friendly interface for file uploads and lineage visualization.
- **Database**: Utilizes SQLite for storing lineage data, with plans for scalability in future versions.

## Getting Started

### Prerequisites
- Python 3.x
- Node.js and npm

### Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/yourusername/ai-data-lineage-generator.git
   cd ai-data-lineage-generator
   ```

2. **Backend Setup**:
   - Navigate to the backend directory:
     ```
     cd backend
     ```
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. **Frontend Setup**:
   - Navigate to the frontend directory:
     ```
     cd ../frontend
     ```
   - Install the required npm packages:
     ```
     npm install
     ```

### Running the Application

1. **Start the Backend**:
   ```
   cd backend
   python app.py
   ```

2. **Start the Frontend**:
   ```
   cd ../frontend
   npm start
   ```

3. Open your browser and navigate to `http://localhost:3000` to access the application.

## Usage
- Upload code files or provide a link to a Git repository to analyze data lineage.
- Customize the level of detail in lineage reports.
- Visualize the data lineage graph and generate reports in Markdown format.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.