import requests
import webbrowser

# Get the URL and cookie values from the user
url = input('Enter the website URL: ')
cookie_name = input('Enter the cookie name: ')
cookie_value = input('Enter the cookie value: ')

# Define the cookies as a dictionary
cookies = {cookie_name: cookie_value}

try:
    # Make a GET request to the website with the cookies attached
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()  # Raise an exception if the status code is not 200 OK

    # Save the response content to a file
    with open('website.html', 'wb') as f:
        f.write(response.content)

    # Open the website in a new window
    webbrowser.open('website.html', new=2)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
