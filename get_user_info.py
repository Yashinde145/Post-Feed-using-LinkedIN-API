import requests
 
from ln_oauth import auth, headers
 
def user_info(headers):
    '''
        Get user information from Linkedin
    '''
    response = requests.get('https://api.linkedin.com/v2/me', headers = headers)
    user_info = response.json()
    return user_info
 
if __name__ == '__main__':
    credentials = 'credentials.json'
    access_token = auth(credentials) # Authenticate the API
    headers = headers(access_token) # Make the headers to attach to the API call.
    user_info = user_info(headers) # Get user info
    print(user_info)