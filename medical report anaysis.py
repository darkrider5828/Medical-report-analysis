import streamlit as st
import google.generativeai as genai
import PyPDF2
import json
import os
import tempfile
import time
from pyngrok import ngrok
from dotenv import load_dotenv

# 🔹 Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 🔹 Check if API key is set
if not api_key:
    st.error("Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# ✅ Extract text from PDF (Same as Main Script)
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = "".join([page.extract_text() or "" for page in pdf_reader.pages])
    return text

# ✅ Extract biomarkers using Gemini AI (Same as Main Script)
def extract_biomarkers(text):
    prompt = f"""
    Extract all medical biomarkers from the given text and format them as a JSON array.
    The JSON format should be:
    {{
        "biomarkers": [
            {{
                "name": "<Biomarker Name>",
                "value": "<Observed Value>",
                "test_name": "<Test Name>",
                "reference_range": "<Reference Range>"
            }}
        ]
    }}
    Here is the extracted medical report text:
    {text}
    """

    for attempt in range(3):  # Retry logic for robustness
        try:
            response = model.generate_content(prompt)
            json_output = json.loads(response.text)
            return json_output
        except Exception as e:
            if attempt < 2:
                time.sleep(2)  # Wait before retrying
            else:
                return {"error": str(e)}

# ✅ Explain Biomarkers Using Gemini AI
def explain_biomarkers(biomarkers_data):
    if "error" in biomarkers_data:
        return "Error in extracting biomarkers."

    prompt = f"""
    Please explain the following biomarkers in simple terms for a non-medical person.
    Provide what they indicate, if their values are normal or abnormal, and possible health implications.

    {json.dumps(biomarkers_data, indent=4)}
    """

    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if attempt < 2:
                time.sleep(2)  # Retry
            else:
                return f"Error in explanation: {str(e)}"

# ✅ Streamlit UI
def main():
    st.title("Medical Report Biomarker Extractor & Explainer")
    st.write("Upload a medical report PDF to extract biomarkers and get explanations.")

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file:
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)

        if st.button("Extract Biomarkers"):
            with st.spinner("Extracting biomarkers..."):
                biomarkers_data = extract_biomarkers(text)

            st.subheader("Extracted Biomarkers")
            st.json(biomarkers_data)

            if st.button("Explain Biomarkers"):
                with st.spinner("Generating Explanation..."):
                    explanation = explain_biomarkers(biomarkers_data)

                st.subheader("Biomarker Explanation")
                st.write(explanation)

if __name__ == "__main__":
    main()
