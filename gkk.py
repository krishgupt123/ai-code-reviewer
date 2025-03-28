import streamlit as st
import logging
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
GOOGLE_API_KEY='AIzaSyB0fmBalqm8rQp-UetPimImYNcpObJEX70'
# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)  # Set your API key in environment variables

def analyze_code(code):
    """Send code to Gemini Flash 2.0 model for AI analysis"""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')  # Use Gemini Flash 1.5
        prompt = f"Analyze the following code and provide a review, including potential improvements and bug detection:\n\n{code}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Failed to analyze code with Gemini Flash 1.5: {e}")
        return None

def main():
    """AI Code Reviewer - Frontend (Streamlit with Gemini Flash 1.5)"""
    logger.info("Frontend started")

    st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖", layout="wide")

    st.title("🚀 AI Code Reviewer & Debugger")
    st.write("Analyze, review, and optimize your code with AI-powered insights using Gemini Flash 1.5.")

    # File Upload Section
    uploaded_file = st.file_uploader("Upload your code file", type=["py", "java", "cpp"])

    if uploaded_file is not None:
        try:
            # Read file content
            code_content = uploaded_file.getvalue().decode("utf-8")
            st.text_area("📜 Uploaded Code:", code_content, height=250)

            # Send code for analysis
            if st.button("Analyze Code"):
                logger.info("Sending code for analysis to Gemini Flash 1.5")
                analysis_result = analyze_code(code_content)

                if analysis_result:
                    st.success("✅ Analysis Complete")
                    st.markdown(analysis_result)  # Display the analysis result
                else:
                    st.error("❌ Failed to analyze code. Please try again.")
        except Exception as e:
            logger.error(f"Error processing file: {e}")
            st.error("An error occurred while reading the file.")

if __name__ == "__main__":
    main()