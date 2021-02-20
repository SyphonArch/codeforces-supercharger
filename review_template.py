from get_problems import fetch_problems
problems = fetch_problems(1486)

def problem_layout(problem_info):
    number, name, url = problem_info
    return (f'<p style="text-align: left;" data-ke-size="size18">'
            f'<b>{number}: <a href="{url}" target="_blank" rel="noopener">{name}</a></b></p>'
            f'\n<p>{number} content</p>'
            f'\n<p><b><span style="background-color: #9feec3;">AC: 분</span></b></p>')

problem_separator = '\n<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style6" />\n'

template = f'''<p>Header</p>
<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style7" />
{problem_separator.join(problem_layout(problem_info) for problem_info in problems)}
<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style7" />
<p style="text-align: left;" data-ke-size="size18"><b>총평</b></p>
<p>Summary content</p>
<p>&nbsp;</p>
<p><span style="background-color: #99cefa;"><b>레이팅 변화: x + y = z</b></span></p>
<p><b><span style="background-color: #c1bef9;">My Performance: ★★★☆☆</span></b></p>
<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style7" />
<p style="text-align: left;" data-ke-size="size18"><b>연습지</b></p>
'''

print(template)