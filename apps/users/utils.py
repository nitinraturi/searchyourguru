from rest_framework_simplejwt.tokens import RefreshToken
from .models import AllZipCode
import requests
import pandas as pd


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def fetch_zipcode_from_api(zipcode):
    zipcode_api_endpoint = "https://api.postalpincode.in/pincode/{zipcode}".format(
        zipcode=zipcode)
    response = requests.get(zipcode_api_endpoint)
    if response.status_code == 200:
        result = response.json()[0]
        return result['PostOffice'] if result['Status'] == 'Success' else None


def fetch_zipcodes_from_excel_file(file_path):
    df = pd.read_excel(file_path)
    try:
        for pincode in df['PINCODE']:
            pincode_data = fetch_zipcode_from_api(pincode)
            if pincode_data is not None:
                for data in pincode_data:
                    try:
                        AllZipCode.objects.create(
                            po_name=data['Name'],
                            district=data['District'],
                            state=data['State'],
                            country=data['Country'],
                            zipcode=data['Pincode']
                        )
                        # objects.append(obj)
                    except:
                        pass

            else:
                continue
        return True
    except:
        return None
