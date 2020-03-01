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
    df = pd.read_csv(file_path)
    objects = []
    for index, row in df.iterrows():
        try:
            data = {
                'po_name': row['officename'],
                'district': row['Districtname'],
                'state': row['statename'],
                'zipcode': row['pincode'],
                'country': "India",
            }
            obj = AllZipCode(**data)
            objects.append(obj)
            if index+1 % 10000 == 0:
                print(index+1)
        except Exception as e:
            print(e)
            pass

    AllZipCode.objects.all().delete()
    total = AllZipCode.objects.bulk_create(objects)
    return total
