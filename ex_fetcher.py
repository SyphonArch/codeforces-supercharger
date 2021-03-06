from get_problems import fetch_problems
import requests
import re
import os
from bs4 import BeautifulSoup
from sys import argv
from time import sleep

# Setup START
contest_no = 1492
# Setup END

if len(argv) > 1:
    delay = int(argv[1])
    print(f"Sleeping {delay} seconds...")
    sleep(delay)


print('\nFetching problem metadata...\n')
problems = fetch_problems(contest_no)

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
    if len(io_content) % 2 == 0:
        for i, content in enumerate(io_content):
            ex_num = i // 2
            if i % 2 == 0:
                ex_input = content.text[1:]
                with open(f"./{dir_name}/{number}_in_{ex_num}.txt", 'w') as f:
                    f.write(ex_input)
            else:
                ex_output = content.text[1:]
                with open(f"./{dir_name}/{number}_out_{ex_num}.txt", 'w') as f:
                    f.write(ex_output)
        print(' - Done')
    else:
        print(' - ERROR')
