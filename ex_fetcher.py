from get_problems import fetch_problems
import requests
import re
import os
from bs4 import BeautifulSoup
from sys import argv
from time import sleep

if len(argv) > 1:
    delay = int(argv[1])
    print(f"Sleeping {delay} seconds...")
    sleep(delay)


print('\nFetching problem metadata...\n')
problems = fetch_problems(1486)

dir_name = 'ex_io'
if not os.path.isdir(f'./{dir_name}'):
    os.mkdir(f'./{dir_name}')

output = 'output'
if not os.path.isdir(f'./{output}'):
    os.mkdir(f'./{output}')

for problem in problems:
    number, name, link = problem
    print(f"Fetching problem {number}", end='')
    html = requests.get(link)
    soup = BeautifulSoup(html.text, 'html.parser')
    io_content = soup.find_all('pre')
    if len(io_content) == 2:
        ex_input = io_content[0].text[1:]
        ex_output = io_content[1].text[1:]
    with open(f"./{dir_name}/{number}_in.txt", 'w') as f:
        f.write(ex_input)
    with open(f"./{dir_name}/{number}_out.txt", 'w') as f:
        f.write(ex_output)
    print(' - Done')