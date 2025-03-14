# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv


load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
# Add code for get requests to back end
def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
import requests

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # Call the GET method of the requests library with the URL and parameters
        response = requests.get(request_url)

        # Check if the response status code is 200 (successful)
        if response.status_code == 200:
            # Return the JSON response
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as err:
        # Handle unexpected exceptions
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None



# def post_review(data_dict):
# Add code for posting review

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
