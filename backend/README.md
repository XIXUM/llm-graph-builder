# Project Overview
Welcome to our project! This project is built using FastAPI framework to create a fast and modern API with Python.

## Feature
API Endpoint : This project provides various API endpoint to perform specific tasks.
Data Validation : Utilize FastAPI data validation and serialization feature.
Interactive Documentation : Access Swagger UI and ReDoc for interactive API documentation.

## Getting Started 

Follow these steps to set up and run the project locally:

1. Clone the Repository:

> git clone https://github.com/neo4j-labs/llm-graph-builder.git

> cd llm-graph-builder

2. Install Dependency :

> pip install -r requirements.txt

3. install punkt_tab by executing the following in your python console:

```
      import nltk
      nltk.download('punkt')
```

if you receive this error message:

```
      [nltk_data] Error loading punkt: <urlopen error [SSL:
      [nltk_data] CERTIFICATE_VERIFY_FAILED] certificate verify failed:
      [nltk_data] unable to get local issuer certificate (_ssl.c:1000)>
```

The error indicates that the SSL certificate verification failed while trying to download the `punkt` resource. This is a common issue with Python's SSL configuration on macOS. You can resolve it by following these steps:

### Fix SSL Certificate Issue on macOS

a. **Install Certificates for Python**:
   Run the following command in your terminal to install the necessary certificates for Python:
   ```bash
   /Applications/Python\ 3.x/Install\ Certificates.command
   ```
   __NOTE:__ Replace `3.x` with your installed Python version (e.g., `3.12`).

b. **Retry the NLTK Download**:
   After installing the certificates, retry the download in your Python shell or script:
   ```python
   import nltk
   nltk.download('punkt')
   ```

c. **Alternative: Use HTTP Instead of HTTPS**:
   If the issue persists, you can manually download the `punkt` resource:
   - Visit [NLTK Data](https://www.nltk.org/nltk_data/) and download the `punkt` package.
   - Extract the downloaded files and place them in the appropriate directory (e.g., `/Users/<user name>/nltk_data`).

d. **Verify Installation**:
   Ensure the `punkt` resource is available by running:
   ```python
   import nltk
   nltk.data.find('tokenizers/punkt')
   ```

e. **Restart Your Backend Server**:
   Restart the server to confirm the issue is resolved.

_NOTE:_ there is a script in /backend/test_SSL_Connection.py which does this installation and checks for the certificate first...

## Run backend project using unicorn
Run the server:
> uvicorn score:app --reload

the server then should reply with this output:

```bash
INFO:     Will watch for changes in these directories: ['/Users/XXXX/XXXXX/llm-graph-builder/backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [74154] using StatReload
2025-05-29 15:37:32,857 - PyTorch version 2.7.0 available.
2025-05-29 15:37:33,034 - Use pytorch device_name: mps
2025-05-29 15:37:33,034 - Load pretrained SentenceTransformer: all-MiniLM-L6-v2
2025-05-29 15:37:36,053 - Embedding: Using Langchain HuggingFaceEmbeddings , Dimension:384
2025-05-29 15:37:36,055 - USER_AGENT environment variable not set, consider setting it to identify your requests.
2025-05-29 15:37:36,147 - Use pytorch device_name: mps
2025-05-29 15:37:36,147 - Load pretrained SentenceTransformer: all-MiniLM-L6-v2
2025-05-29 15:37:37,710 - Embedding: Using Langchain HuggingFaceEmbeddings , Dimension:384
[nltk_data] Downloading package punkt to
[nltk_data]     /Users/<username>/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
2025-05-29 15:37:38,018 - Loading embedding model 'openai' for ragas evaluation
2025-05-29 15:37:38,060 - Embedding: Using OpenAI Embeddings , Dimension:1536
INFO:     Started server process [74156]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
## Run project using docker
## prerequisite 
Before proceeding, ensure the following software is installed on your machine

Docker: https://www.docker.com/

1. Build the docker image
   > docker build -t your_image_name .
   
   Replace `your_image_name` with the meaningful name for your Docker image

2. Run the Docker Container
   > docker run -it -p 8000:8000 your_image_name
   
   Replace `8000` with the desired port.

## Access the API Documentation
Open your browser and navigate to
http://127.0.0.1:8000/docs for Swagger UI or
http://127.0.0.1:8000/redocs for ReDoc.

## Project Structure
`score.py`: Score entry point for FastAPI application

## Configuration

Update the environment variable in `.env` file. Refer example.env in backend folder for more config.

`OPENAI_API_KEY`: Open AI key to use incase of openai embeddings

`EMBEDDING_MODEL` : "all-MiniLM-L6-v2" or "openai" or "vertexai"

`NEO4J_URI` : Neo4j URL

`NEO4J_USERNAME` : Neo4J database username

`NEO4J_PASSWORD` : Neo4j database user password

`AWS_ACCESS_KEY_ID` : AWS Access key ID

`AWS_SECRET_ACCESS_KEY` : AWS secret access key


## Contact
For questions or support, feel free to contact us at christopher.crosbie@neo4j.com or michael.hunger@neo4j.com
