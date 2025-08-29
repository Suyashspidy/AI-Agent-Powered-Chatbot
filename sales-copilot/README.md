# SalesCopilot Project

SalesCopilot is a full-stack, AI-powered sales assistant application designed to enhance sales conversations using advanced language models and embedding techniques. This project leverages Google's Gemini API for language processing and Deep Lake for vector storage.

## Project Structure

```
sales-copilot
├── src
│   ├── data_ingestion.py       # Functions for scraping content and computing embeddings
│   ├── agent.py                 # Main agent logic for handling customer queries
│   ├── config.py                # Configuration settings and API keys
│   ├── database.py              # Interactions with the Deep Lake vector database
│   ├── prompts.py               # Prompt templates for the Gemini LLM
│   └── utils.py                 # Utility functions for logging and error handling
├── app.py                       # Entry point for the Streamlit web application
├── requirements.txt             # List of necessary libraries for the project
├── .env.example                 # Template for environment variables
├── .gitignore                   # Files and directories to ignore by Git
└── README.md                    # Documentation for the project
```

## Getting Started

### Prerequisites

- Python 3.x
- A Google Gemini API key
- Deep Lake account for vector storage

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sales-copilot
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

4. Configure your environment variables:
   - Copy `.env.example` to `.env` and fill in the necessary API keys.

### Running the Application

To start the Streamlit web application, run:
```
streamlit run app.py
```

### Usage

- Enter a customer query in the designated input field.
- The application will simulate a live sales conversation by providing a recommended response based on the context retrieved from the Deep Lake knowledge base.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.