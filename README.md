# Zero-Shot Text Classification API
A Python HTTP frontend for zero-shot text classification using a Large Language Model (LLM)
## Overview
The Zero-Shot Text Classification API provides a simple way to classify text according to a set of labels
without requiring any labeled training data. It takes two inputs in the body of the POST request: "text" and
"labels". The API uses these inputs to query a LLM and returns a classification result as a JSON object.

**Note**: This project is designed for use in a secure environment only. Running this API in a production
environment without proper security measures in place may compromise the confidentiality, integrity, and
availability of your data. Please ensure you have implemented appropriate security controls before deploying
this API.

## Get Started
To start using the Zero-Shot Text Classification API, you will need:
1. **Python 3.11 or greater**: Make sure your Python version meets this requirement.
2. **A Python virtual environment setup**: Install a virtual environment tool like `virtualenv` or `conda`,
   and set up a new environment.
3. **Activated virtual environment**: Activate the virtual environment using the command provided by the tool
   you chose.

Once your virtual environment is active, you can install the requirements for the project by running:
```shell
pip install -r requirements.txt
```
This will install all the necessary dependencies listed in the `requirements.txt` file.

## Usage
To use the Zero-Shot Text Classification API, send a POST request to the API endpoint with the following
format:

```json
{
  "text": "<your text here>",
  "labels": ["label1", "label2", "..."]
}
```
Replace `<your text here>` with the text you want to classify. Replace `"label1"`, `"label2"`, etc. with the
classification labels you want to use.

## API Endpoints
The Zero-Shot Text Classification API has a single endpoint: `/classify`. This is where you should send your
POST request with the "text" and "labels" inputs as described above.

### Example Request
Here is an example of what a valid request might look like:

```shell
curl -X POST \
  http://localhost:8000/classify \
  -H 'Content-Type: application/json' \
  -d '{"text": "This is a test", "labels": ["positive", "negative", "neutral"]}'
```
### Example Response
The response to this request might look like:

```json
{
   "sequence": "This is a test",
   "labels": ["neutral", "negative", "positive"],
   "scores": [0.998625357, 0.228435, 0.3134532]
}
```
In this example, the API returns a JSON object with three key-value pairs: `sequence`, `labels`, and
`scores`. The value of `sequence` is the input text, the value of `labels` is the list of labels provided by
the user, sorted in order of their corresponding scores. The value of `scores` is the list of confidence
scores between 0 and 1 for each label.