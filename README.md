# Medical Report Biomarker Extractor & Explainer

## 📌 Overview
This is a **Streamlit-based web application** that extracts biomarkers from medical reports (PDFs) and provides explanations for their significance using **Google Gemini AI**. The app utilizes **PyPDF2** for text extraction, **Gemini AI** for biomarker identification and explanation, and **Streamlit** for an interactive UI.

## 🛠 Features
- 📄 **Upload a medical report (PDF)**
- 🔍 **Extract biomarkers (name, value, test name, reference range)**
- 💡 **Explain biomarkers in simple terms**
- ⏳ **Retry logic for better response stability**
- 🏥 **Useful for patients and healthcare professionals**

## 🚀 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/biomarker-extractor.git
cd biomarker-extractor
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then install the required dependencies:
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the project directory and add your **Google Gemini API key**:
```
GEMINI_API_KEY=your_api_key_here
```

## ▶️ Usage
Run the Streamlit app using:
```sh
streamlit run app.py
```

## 🏗 Project Structure
```
biomarker-extractor/
│-- app.py            # Main Streamlit application
│-- .env              # Environment variables
│-- requirements.txt  # Python dependencies
│-- README.md         # Project documentation
```

## 📝 How It Works
1. **User uploads a PDF** containing medical test results.
2. The app **extracts text** using `PyPDF2`.
3. The extracted text is **processed by Gemini AI** to identify biomarkers.
4. The identified biomarkers are **displayed as JSON**.
5. Upon request, Gemini AI **explains the biomarkers** in simple terms.

## 🛡 Error Handling
- If the API key is missing, the app will display an error and stop execution.
- If the Gemini API fails, the app retries up to 3 times before returning an error message.

## 📜 License
MIT License

## 🤝 Contributing
Feel free to fork this repository and submit pull requests for improvements.

## 📧 Contact
For issues or suggestions, reach out via [your-email@example.com](mailto:your-email@example.com).

