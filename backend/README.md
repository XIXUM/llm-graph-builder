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
   Replace `3.x` with your installed Python version (e.g., `3.12`).

b. **Retry the NLTK Download**:
   After installing the certificates, retry the download in your Python shell or script:
   ```python
   import nltk
   nltk.download('punkt')
   ```

c. **Alternative: Use HTTP Instead of HTTPS**:
   If the issue persists, you can manually download the `punkt` resource:
   - Visit [NLTK Data](https://www.nltk.org/nltk_data/) and download the `punkt` package.
   - Extract the downloaded files and place them in the appropriate directory (e.g., `/Users/felixschaller/nltk_data`).

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
