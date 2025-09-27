---

```markdown
# 🎬 IMDB Movie Review Sentiment Analysis – Simple RNN  

An **Artificial Neural Network (ANN)** project for **sentiment classification** of IMDB movie reviews.  
Built using **TensorFlow/Keras** with a **Simple RNN** model and deployed with **Streamlit** for real-time predictions.  

---

## ✅ Project Overview  
- Dataset: **IMDB Movie Review Dataset** (`tensorflow.keras.datasets.imdb`)  
- Model: **SimpleRNN with Embedding Layer**  
- Task: **Binary Classification (Positive / Negative review)**  
- Deployment: **Streamlit Web App** (`main.py`)  
- Support Files: Jupyter notebooks for training & predictions  

---

## 📂 Repository Structure  

```

IMDB-Movie-Review-Sentiment-Analysis/
├── main.py                 # 🚀 Streamlit app (main entry point)
├── simplernn.ipynb         # Training notebook (model building & saving)
├── prediction.ipynb        # Testing notebook (manual prediction)
├── simple_rnn_imdb.h5      # Trained model (used by Streamlit app)
├── requirements.txt        # Python dependencies

````

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/THOWFI/IMDB-Movie-Review-Sentiment-Analysis.git
cd IMDB-Movie-Review-Sentiment-Analysis
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

* Windows → `.venv\Scripts\activate`
* Linux/Mac → `source .venv/bin/activate`

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

*(If GPU not available, you can install `tensorflow-cpu` instead of `tensorflow`)*

---

## 🚀 Run the Streamlit App

```bash
streamlit run main.py
```

* A local server will start → Open in browser (default: `http://localhost:8501`)
* Enter any **movie review text** in the input box
* Click **Classify** → Get prediction:

  * **Positive ✅**
  * **Negative ❌**
* Probability score also displayed

---

## 🧪 Model Workflow

1. **Data Ingestion**

   * Load IMDB dataset (`num_words=10000`)
   * Pad/truncate sequences (`maxlen=500`)

2. **Model Training** (in `simplernn.ipynb`)

   * Embedding (10000 × 128)
   * SimpleRNN(128, ReLU)
   * Dense(1, Sigmoid)
   * Optimizer: Adam | Loss: Binary Crossentropy
   * Saved as `simple_rnn_imdb.h5`

3. **Inference (main.py / prediction.ipynb)**

   * Convert review → sequence of word indices
   * Pad sequence → fixed length
   * Predict sentiment using trained model

---

## 🌐 Example Run

Input:

```
This movie was fantastic! The story and acting were top-notch.
```

Output:

```
Sentiment: Positive ✅
Probability (positive): 0.97
```

---

## 📌 Notes

* `main.py` is the **primary application** for end users.
* `simplernn.ipynb` → For training/re-training model.
* `prediction.ipynb` → For manual inference testing.
* `simple_rnn_imdb.h5` → Pre-trained model (used directly by Streamlit app).

---

## 🔮 Future Enhancements

* Upgrade to **LSTM/GRU** for better accuracy.
* Add **Tokenizer-based preprocessing** (to replace word_index mapping).
* Deploy on **Docker + Cloud (AWS/Heroku/Streamlit Cloud)**.

---

## 📜 License

For **educational and research** purposes. Validate and test thoroughly before using in production.

---
