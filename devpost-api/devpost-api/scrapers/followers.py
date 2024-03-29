import requests
from bs4 import BeautifulSoup

base_url = 'https://devpost.com'

class Followers:
    soup = None

    def __init__(self, username):
        req = requests.get(f'https://devpost.com/{username}/followers')
        self.soup = BeautifulSoup(req.text, 'lxml')

    def get_followers(self) -> [str]:
        followers = self.soup.select('#follow-entries div a[href]')
        followers = [base_url + x['href'] for x in followers]
        return followers
