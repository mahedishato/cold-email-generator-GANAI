import requests

# Define the URL of the Flask API endpoint
api_url = "http://127.0.0.1:5000/process"

# Define the payload with the URL you want to process
payload = {
    "url": "https://www.asthait.com/career/machine-learning-engineer/"
}

# Send the POST request to the API
response = requests.post(api_url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Print the JSON response from the API
    emails = response.json().get('emails', [])
    for email in emails:
        print(email)
else:
    # Print the error message if the request failed
    print(f"Failed to get a response: {response.status_code}")
    print(response.json())
