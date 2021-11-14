def generate_row():

    import re
    import os
    s = input('plz type the title.')
    if not s.endswith('.ipynb'):
        s += '.ipynb'
    github_url = "https://github.com/lowspace/leetcode/blob/main/code/{}".format(re.sub(' ', '%20', s))
    s = s.rstrip('.ipynb').split('.')
    num = s[0]
    name = s[1].strip() # remove first whitespace
    leetcode_url = "https://leetcode.com/problems/{}".format(re.sub(' ', '-', name.lower()))
    summary = input('plz type the summary')
    summary = re.sub('(?<=\))\s', ' <br> ',summary).strip()
    tags = input('plz type the tags').strip(',;.')
    tags = '`' + tags + '`'
    tags = re.sub('[,;.]\s', '` `', tags)

    text = "| [{num}]({leetcode_url}) | [{name}]({github_url}) | {summary} | {tags} |\n".format(
        num = num, leetcode_url = leetcode_url, name = name, github_url = github_url, 
        summary = summary, tags = tags
    )

    path = os.getcwd()
    parent_path = os.path.dirname(path)
    file_name = 'README.md'
    file_path = os.path.join(parent_path, file_name)
    with open(file_path, 'r') as f:
        doc = f.readlines()

    doc.append(text)

    with open(file_path, 'w') as f:
        f.write(''.join(doc))

    return