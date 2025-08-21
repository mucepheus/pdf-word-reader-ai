# PDF & Word Reader AI

This project reads documents in various formats, extracts text, tables, and images (with optional OCR), and answers questions based on the content.

## Features
- Read `.pdf`, `.docx`, `.txt`, and `.xlsx` files
- Extract text, tables, and images
- OCR on images and image-based tables when Tesseract is installed
- TF-IDF based question answering with structured bullet point responses
- Optional web interface via Flask

## Installation
1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## CLI Usage
```bash
python main.py --file path/to/document.pdf --question "Your question here"
```

## Web Interface
```bash
python web_app.py
```
Open `http://localhost:5000` in your browser and upload a document to ask questions.

## Testing
Run the test suite:
```bash
pytest
```
