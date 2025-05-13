import requests

def check_internet():
    """
    Checks if the device has an active internet connection
    by attempting to reach Google.
    """
    print("\n-------------------------------------------------------")
    try:
        requests.get("https://www.google.com", timeout=5)
        print("\n✅ Internet connection is active.")
    except requests.ConnectionError:
        print("\n❌ No internet connection.")
