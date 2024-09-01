

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mahedishato/cold-email-generator-GANAI.git
   cd cold-email-generator-GANAI
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Start the API

To start the API, run the following command:

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`.

### API Endpoints

#### Process Data

- **Endpoint**: `/process`
- **Method**: `POST`
- **Description**: Extracts job data from the provided URL, matches skills with portfolio links, and returns email drafts.
  
**Request Body**:

```json
{
  "url": "https://www.example.com/job-posting"
}
```

**Response**:

```json
{
  "emails": [
    "Generated email content 1",
    "Generated email content 2",
    ...
  ]
}
```

If an error occurs, the response will include an error message:

```json
{
  "error": "Description of the error"
}
```

## Example

To process a job posting from a URL, send a `POST` request to the `/process` endpoint with the URL in the request body.

Example using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/process -H "Content-Type: application/json" -d '{"url": "https://www.asthait.com/career/machine-learning-engineer/"}'
```

## Dependencies

- **Flask**: Web framework for building the API.
- **langchain_community**: Provides the `WebBaseLoader` for loading web pages.
- **sorce**: Custom library used for job extraction, text cleaning, and portfolio management.

Install these dependencies using:

```bash
pip install Flask langchain_community sorce
```

## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

