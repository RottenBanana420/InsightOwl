# InsightOwl: AI-Powered News Research Tool

## Description

InsightOwl is a web app designed to process URLs of news articles, embed their content using Ollama LLaMA3, store the information in a FAISS index, and answer user queries based on the content. This tool is ideal for researchers, journalists, and anyone looking to efficiently extract insights from news articles.


## Features

- **Streamlined User Interface**: Built with Streamlit for an intuitive user experience.
- **Advanced Embeddings**: Utilizes Ollama LLaMA3 for high-quality content embeddings.
- **Efficient Storage & Retrieval**: Stores embeddings in a FAISS index for fast retrieval.
- **Interactive Q&A**: Allows users to input queries and retrieves answers along with sources.


## Prerequisites

- Python 3.7 or higher
- Streamlit
- FAISS
- Ollama LLaMA3

  
## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

- `LANGCHAIN_API_KEY`: Your API key for LangChain.

Example `.env` file:
```env
LANGCHAIN_API_KEY=your_langchain_api_key
```


## Installation

Clone the repository:

```bash
git clone https://github.com/RottenBanana420/InsightOwl.git
cd InsightOwl
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```


## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```
2. Open the app in your browser at http://localhost:8501.

3. Input up to three news article URLs in the sidebar.

4. Click the "Process URLs" button to fetch and process the content.

5. Once processing is complete, enter your query in the input field and get answers based on the indexed content.


## Screenshots

![Home Page](https://github.com/user-attachments/assets/c9877d10-d8ec-4ce1-b040-24b16eb5fd7c)

![Query and Answer](https://github.com/user-attachments/assets/b964449e-8bf8-4e4b-b792-5ba13e3e677e)


## Contributing

1. Fork the project.
2. Create your feature branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/YourFeature).
5. Open a pull request.


## FAQ

#### How do I get a LangChain API key?

You can obtain a LangChain API key by signing up on the LangChain website and subscribing to their service.

#### What is FAISS?

FAISS (Facebook AI Similarity Search) is a library for efficient similarity search and clustering of dense vectors. It is used in InsightOwl to store and retrieve embeddings.

#### Can I process more than three URLs at a time?

The current implementation supports up to three URLs. To process more URLs, you would need to modify the code to handle additional inputs and processing.

#### How can I contribute to this project?

I welcome contributions! Please fork the repository, make your changes, and submit a pull request. Ensure your code adheres to the project's coding standards and includes appropriate tests.


## License

[MIT](LICENSE)

