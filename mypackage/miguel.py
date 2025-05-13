import requests
"""
    Checks if the device has an active internet connection by attempting to reach Google.

    Sends a GET request to "https://www.google.com" with a timeout of 5 seconds.
    If the request is successful, it prints a message indicating the internet is active.
    If a connection error occurs, it prints a message indicating no internet connection.
    """

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        print("✅ Internet connection is active.")
    except requests.ConnectionError:
        print("❌ No internet connection.")