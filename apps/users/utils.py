from rest_framework_simplejwt.tokens import RefreshToken
import requests


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def fetch_zipcode_from_api(zipcode):
    zipcode_api_endpoint = "https://api.postalpincode.in/pincode/{zipcode}".format(zipcode=zipcode)
    response = requests.get(zipcode_api_endpoint)
    if response.status_code == 200:
        result = response.json()[0]
        return result['PostOffice'] if result['Status'] == 'Success' else None
