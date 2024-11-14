import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = '623aacb3a391d7768bee3c1774d85b06bf619b6b'

# create an instance of the API class
api_instance = swagger_client.AthletesApi()

try:
    # Get Zones
    api_response = api_instance.getLoggedInAthleteZones()
    print(api_response)
except ApiException as e:
    print("Exception when calling AthletesApi->getLoggedInAthleteZones: %s\n" % e)



"""
Client Secret
3986e90770a637d0062d8eafe6bc7c2969b1bc55

Your Access Token
623aacb3a391d7768bee3c1774d85b06bf619b6b

Your Refresh Token
10fb511f94e31d4dff4c625657925c4a6de995b5

Overall Rate Limits
200 requests every 15 minutes, 2,000 daily
Read Rate Limits
100 requests every 15 minutes, 1,000 daily
"""