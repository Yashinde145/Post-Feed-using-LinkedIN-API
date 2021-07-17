import requests
 
from ln_oauth import auth, headers
 
credentials = 'credentials.json'
access_token = auth(credentials) # Authenticate the API
headers = headers(access_token) # Make the headers to attach to the API call.
organization_id = 'Your organization_id here'
 
def user_info(headers):
    '''
    Get user information from Linkedin
    '''
    response = requests.get('https://api.linkedin.com/v2/me', headers = headers)
    user_info = response.json()
    return user_info
 
# Get user id to make a UGC post
user_info = user_info(headers)
urn = user_info['id']
 
# UGC will replace shares over time.

api_url = 'https://api.linkedin.com/v2/ugcPosts'
author = f"urn:li:organization:"+organization_id
 
message = '''
Python example for use of symtable
'''
link = 'https://cppsecrets.com/users/12679117971219711510411749525364103109971051084699111109/Python-Example-illustrating-the-use-of-symbol-table.php'
link_text = 'Complete tutorial using the LinkedIn API'
 
post_data = {
    "author": "urn:li:organization:"+organization_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": message
                },
                "shareMediaCategory": "ARTICLE",
                "media": [
                    {
                        "status": "READY",
                        "description": {
                            "text": message
                        },
                        "originalUrl": link,
                        "title": {
                            "text": link_text
                        }
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

response = requests.post(api_url, headers=headers, json=post_data)

if response.status_code == 201:
    print("Success")
    print(response.content)
else:
    print(response.content)
 
if __name__ == '__main__':
    r = requests.post(api_url, headers=headers, json=post_data)
    r.json()