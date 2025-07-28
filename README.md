# Rag-Ollama-Mistral
Here’s a **professional README.md** for your GitHub repo:

---

# 🧠 Private AI Brain – RAG Pipeline with Ollama & Mistral

A **fully local Retrieval-Augmented Generation (RAG) pipeline** built to query your **own documents** securely, with **no cloud dependencies**, no API costs, and complete **privacy**.

---

## ✅ Features

* **Runs 100% locally** – No data leaves your machine.
* **Powered by open-source tools**:

  * **Model:** [Mistral](https://mistral.ai)
  * **Host:** [Ollama](https://ollama.ai)
  * **Framework:** [LangChain](https://www.langchain.com/)
  * **Vector Store:** [ChromaDB](https://www.trychroma.com/)
* **RAG pipeline**:

  * Ingest your documents
  * Create embeddings
  * Query with context-aware answers

---

## 🛠 Tech Stack

* **Python 3.10+**
* **Ollama** (for local LLM hosting)
* **LangChain** (RAG orchestration)
* **ChromaDB** (vector database)
* **Mistral model** (via Ollama)

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone (https://github.com/Vishnusai17/LLM-s.git)
```

2. **Create a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# OR
.venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install and run Ollama**

* [Download Ollama](https://ollama.ai/download)
* Pull the Mistral model:

```bash
ollama pull mistral
```

---

## 📂 Project Structure

```
private-ai-brain/
├── populate_database.py          # Script to process and store documents
├── query_data.py      # Query interface for RAG
├── test_rag.py        # Basic tests for validation
├── get_embedding_function.py
├── chroma/            # Local ChromaDB storage
└── requirements.txt
```

---

## ▶️ Usage

### 1. **Ingest your documents**

Put your PDFs or text files in a folder (e.g., `data/`) and run:

```bash
python populate_database.py
```

### 2. **Ask questions**

```bash
python query_data.py "What is in the document?"
```

---

## ✅ Example Query

```bash
$ python query_data.py "How much money does a Monopoly player start with?"
Response: Players start with $1500.
Sources: ['rules.pdf']
```

---

## 🔥 Why This Project?

* **Privacy-first:** No cloud services, your data stays local.
* **Cost-free:** No API charges.
* **Fast & Reliable:** Runs on your machine.

---

## 📸 Demo

*(Add screenshots or a GIF demo here)*

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

MIT License.

