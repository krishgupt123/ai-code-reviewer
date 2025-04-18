# AI-Driven Code Review and Debugging System

## Overview
The **AI-Driven Code Review and Debugging System** is a tool designed to assist developers by automatically analyzing code for errors, optimizations, and best practices. The system leverages **Google Gemini 1.5 Flash** for AI-powered analysis and provides an intuitive **Streamlit** interface for user interaction.

## Features
### Implemented:
- **AI-Powered Code Review**: Uses **Google Gemini 1.5 Flash** to analyze code for syntax errors, logical issues, and optimizations.
- **Streamlit Web UI**: Provides a user-friendly interface for uploading and reviewing code.

### Upcoming Features:
- **FastAPI Backend**: For enhanced API interactions.
- **Security Scanning with OWASP ZAP**: To detect and mitigate vulnerabilities.
- **Docker Deployment**: Containerization for better scalability and portability.
- **Kubernetes Orchestration**: Managing multiple instances for high availability.

## Installation
To set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/ai-code-review.git
   cd ai-code-review
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   export GEMINI_API_KEY="your-api-key"
   ```
   (For Windows PowerShell)
   ```powershell
   $env:GEMINI_API_KEY="your-api-key"
   ```

5. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

## Usage
- Upload a code snippet via the Streamlit UI.
- The AI will analyze the code and provide a report highlighting issues and suggestions.
- Future updates will include security scanning and additional optimizations.

## Future Work
- **FastAPI integration** to support API-based code analysis.
- **Security vulnerability scanning** using **OWASP ZAP**.
- **Deployment via Docker and Kubernetes** for scalable architecture.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with suggested improvements.

## License
This project is licensed under the MIT License.

