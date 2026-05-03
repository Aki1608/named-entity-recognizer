# Named Entity Recognition (NER) Analyzer

A full-stack Natural Language Processing (NLP) application designed to ingest unstructured text and automatically extract, classify, and highlight key information (such as People, Organizations, Locations, and Dates). This project utilizes a lightweight, production-ready spaCy pipeline to deliver lightning-fast token classification.

## Features
* **Real-Time Extraction:** Instantly processes text to identify and categorize specific entities without the latency of large cloud models.
* **Modular Engine:** The NLP pipeline logic is completely decoupled from the UI, making the application highly scalable.
* **Entity Highlighting:** Utilizes Gradio's color-mapped highlighting to provide a clear, visual breakdown of the extracted data.
* **Lightweight & Local:** Built on spaCy's highly optimized `en_core_web_sm` model, meaning it runs efficiently on standard CPUs with zero external API calls.

## Tech Stack
* **Python 3**
* **spaCy** (Core NLP Pipeline & Entity Recognizer)
* **Gradio** (Frontend Web UI & Interactive Highlighting)

## Project Structure
* `app.py` - The frontend application. It builds the user interface, captures the input text, and dynamically displays the categorized entities with custom color mapping.
* `ner_engine.py` - The core ML backend. It handles loading the pre-trained spaCy model, parsing the text document, and mapping the tokens to Gradio's required tuple format.
* `requirements.txt` - The strict list of dependencies required to run the environment.

## Quick Start Guide

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Set Up the Environment
It is highly recommended to run this inside a Virtual Environment.
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies & Download the Model
Install the required libraries, then explicitly download spaCy's English language model:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
*(Note: If you skip the second command, the application will launch but fail to extract entities).*

### 4. Launch the Dashboard
Start the local web server:
```bash
python app.py
```
Click the local URL generated in your terminal (e.g., `http://127.0.0.1:7860`) to open the web interface and start analyzing text!

---

## ⚙️ How It Works
1. **Ingestion:** The user submits a block of text via the `app.py` interface.
2. **Processing:** The text is routed to `ner_engine.py`, where it is passed through spaCy's optimized NLP pipeline. The pipeline tokenizes the text, assigns parts-of-speech, and runs its Statistical Entity Recognizer.
3. **Formatting:** The engine iterates through the processed document, extracting tokens that possess an `ent_type_` (like ORG, PERSON, or GPE).
4. **Output:** The data is formatted into a list of tuples and returned to the UI, where Gradio applies specific colors to the defined entity categories.
