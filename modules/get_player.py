import requests

def get_player_info(account_id):
    response=requests.get(f'https://api.opendota.com/api/players/{account_id}').json()
    print(response)


if __name__=='__main__':
    get_player_info('86612847')