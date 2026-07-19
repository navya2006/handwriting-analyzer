# ✍️ Handwriting Analyzer

An AI-powered handwriting analysis application that extracts handwritten text from images and evaluates handwriting quality using computer vision and machine learning techniques.

## 📌 Overview

Handwriting Analyzer allows users to upload an image of handwritten text and receive:

- 📝 Extracted text using OCR
- 📊 Handwriting quality analysis
- 🔍 Readability assessment
- 💡 Insights into handwriting characteristics

The goal of this project is to combine OCR with handwriting analysis to provide meaningful feedback rather than just recognizing text.

---

## ✨ Features

- Upload handwritten images
- OCR-based text extraction
- Handwriting quality evaluation
- Clean and intuitive interface
- Fast processing pipeline

---

## 🛠️ Tech Stack

### Frontend
- HTML/CSS/JavaScript *(or React if applicable)*

### Backend
- Python
- Flask/FastAPI *(whichever you're using)*

### AI / Machine Learning
- OpenCV
- EasyOCR
- NumPy
- Pillow

---

## 📂 Project Structure

```
handwriting-analyzer/
│
├── .ipynb_checkpoints/      # Jupyter notebook checkpoints
├── analyzer.py              # Handwriting scoring and analysis logic
├── app.py                   # Main application
├── test_models.py           # checking which gemini models are compatible
├── TrOcr_module.ipynb       # Experiments with Microsoft's TrOCR model
├── process.jpeg             # Sample image for testing
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/navya2006/handwritting-analyzer.git
cd handwritting-analyzer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

or

```bash
uvicorn main:app --reload
```

(depending on the backend framework)

---

## 📸 How It Works

1. Upload an image containing handwritten text.
2. The image is preprocessed using OpenCV.
3. OCR extracts the handwritten content.
4. The application analyzes handwriting characteristics.
5. Results are displayed with extracted text and handwriting insights.

---

## 🧠 Model Exploration

During development, I experimented with **Microsoft's TrOCR (Transformer-based OCR)** for handwritten text recognition.

While TrOCR produced good results on certain samples, it was **not efficient enough for this project's requirements** due to its relatively high inference time and inconsistent performance across different handwriting styles. To provide a faster and more practical user experience, I chose a lighter OCR pipeline for the final implementation.

This exploration helped compare transformer-based OCR with traditional OCR approaches and understand the trade-offs between accuracy and speed.

---

## 🔮 Future Improvements

- Support multiple handwriting styles
- Handwriting score with detailed metrics
- Grammar and spelling suggestions
- PDF support
- Mobile-friendly interface
- Fine-tune TrOCR on a custom handwriting dataset

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Navya Arora**

If you found this project useful, consider giving it a ⭐ on GitHub!
