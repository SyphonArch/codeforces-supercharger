# codeforces-supercharger
Tools for automating codeforces example pretests.

### What is this?
This repository was made to be a collection of useful scripts for usage during/after codeforces competitions.

The main function is a crawler which automatically fetches all example input/ouput of a contest.

It was made for my personal use, but if whoever stumbles upon this finds this useful, they may use it freely.

### Overview
This repository consists of one python module, two python scripts, and one bash script.
- `get_problems.py` is a module containing the function `fetch_problems`, which fetches problem names and links when given the competition number.
- `ex_fetcher.py` is a script to fetch all example input and output from the competition, and organize them in a subdirectory named `ex_io`.
- `checker.sh` performs automated checking of your code based on the example input/output.
- `review_template.py` is for creating a html template for my contest review posts - this is for my personal use.

### How to supercharge your contests
1. Run `ex_fetcher.py`. As the code can only crawl the problems after the contest has started, you can give a time delay in seconds to the script to delay its execution.
For example, you can do `python3 ex_fetcher.py 10` to give a 10 second delay.
2. The previous step will have downloaded all example input/output, and created two directories: `ex_io` and `output`.
3. Now, you can code your solution for the problems in either Python, C++, or C. The filename must be identical to the problem alphabet, i.e. a.py for problem A.
Capitalization does not matter.
4. Now you can run `./checker.sh a.py` to test your code. Replace `a.py` with the filename of your source.
The output of your code will be echoed, and the difference between the example output and your output will be shown.
Note that you may have to run `chmod +x ./checker.sh` to give the script execute permissions.
