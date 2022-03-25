import requests
from sys import argv

def main():
    # Get the user number from the command line
    poki_num = argv[1]

    # Get the user info from the API as a dictionary
    poki_info = get_user_info(poki_num)
    if poki_info:

        # Get the title and body text strings for PasteBin
        pb_strings = get_title_and_text(poki_info)

        # Post the title and body text to PasteBin
        pb_url = post_to_pastebin(pb_strings[0], pb_strings[1])

        # Print the URL of the new PasteBin paste
        print(pb_url)

def get_user_info(poki_num):
    print("Getting pokimon information...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(URL + str(poki_num))

    if response.status_code == 200:
        print('success')
        return response.json() #Convert response body to a dictionary
    else:
        print('failed. Response code:', response.status_code)
        return

def get_title_and_text(user_dict):
    title = user_dict['name'] + "'s Geographical Location"
    body_text = "Latitude: " + user_dict['address']['geo']['lat'] + "\n"
    body_text += "Longitude: " + user_dict['address']['geo']['lng']
    return (title, body_text)

def post_to_pastebin(title, body_text):
    print("Posting to PasteBin...", end='')

    params = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_format': title
    }
    URL = 'https://pastebin.com/api/api_post.php'
    response = requests.post(URL, data=params)

    if response.status_code == 200:
        print('succes')
        return response.text # Converts response body to a string
    else:
        print('failed. Response code:', response.status_code)
        return response.status_code

main()