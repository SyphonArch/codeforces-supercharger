import requests
import re
from bs4 import BeautifulSoup

codeforces_url = 'http://codeforces.com'
def fetch_problems(contest_no):
    contest_url = f'/contest/{contest_no}'
    target_url = codeforces_url + contest_url

    html = requests.get(target_url)
    soup = BeautifulSoup(html.text, 'html.parser')
    links = soup.find('table', {'class', 'problems'}).find_all('a')

    problem_infos = []

    for link in links:
        link_match = re.match(f'{contest_url}/problem/(.*)', link['href'])
        if link_match is not None:
            problem_number = link_match.group(1)
            link_text = link.text.strip()
            if link_text != problem_number:
                problem_name = link_text
                data = [problem_number, problem_name, codeforces_url + link['href']]
                problem_infos.append(data)

    return problem_infos