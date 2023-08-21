import requests

def integrate_with_third_party_api(data):
    # Prepare the data to be sent to the third-party API
    payload = {
        'data': data
    }

    # Set custom headers for authentication or other purposes
    headers = {
        'Authorization': 'Bearer <access_token>',
        'Content-Type': 'application/json'
    }

    try:
        # Make a request to the third-party API
        response = requests.post('https://api.example.com/endpoint', json=payload, headers=headers)

        # Process the response from the third-party API
        if response.status_code == 200:
            result = response.json()
            # Do further processing with the result
            print('Integration successful. Result:', result)
        else:
            print('Integration failed. Status code:', response.status_code)
            print('Error message:', response.text)
    except requests.exceptions.RequestException as e:
        print('Error occurred during integration:', str(e))

# Example usage
data_to_send = {
    'name': 'John Doe',
    'email': 'johndoe@example.com'
}

integrate_with_third_party_api(data_to_send)
