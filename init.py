from bs4 import BeautifulSoup as bs
from markdownify import MarkdownConverter
from markdownify import markdownify as md # convert htlm to markdown
from time import sleep
import requests
import re
import nbformat as nbf
import os
import pyperclip

class LeetcodeConverter(MarkdownConverter):
    """
    Create a custom MarkdownConverter that adds two newlines after an image
    """
    def convert_img(self, el, text, convert_as_inline):
        return super().convert_img(el, text, convert_as_inline) + '\n'

# Create shorthand method for conversion
def md(html, **options):
    return LeetcodeConverter(**options).convert(html)

def parse_problem_name(s: str) -> str:
    """
    parse the problem name into xx-xx-xx form
    type 1: parse name
    type 2: URL
    """

    def url_parser(s: str) -> str:
        import re
        pattern = "(?<=problems/)([\w]?-?)+(?=/)"
        return re.search(pattern, s)[0]

    def name_parser(s: str) -> str:
        import re
        s = re.findall('[\w]+', s)
        return '-'.join(s)

    if s.startswith('https'):
        return url_parser(s)
    else:
        return name_parser(s)

def valid_name(s: str) -> bool:
    cwd = os.getcwd()
    code_dir = os.path.join(cwd, 'code')
    s = re.sub('-', ' ', s)
    for i in os.listdir(code_dir):
        if s in i:
            return False
    
    return True

# REF: https://stackoverflow.com/questions/56608480/parsing-leetcode-question-content-with-requests-and-beautifulsoup
content = None

while not content:
    problem_name = pyperclip.paste()
    r = None
    problem_name = parse_problem_name(problem_name)
    print(f'The problem name is {problem_name}')
    if not valid_name(problem_name):
        print('The file is already in the code folder, plz check again.')
        sleep(10)
        continue
    data = {"operationName":"questionData",
            "variables":{"titleSlug":problem_name},
            "query":"""
                    query questionData($titleSlug: String!) 
                    {\n  question(titleSlug: $titleSlug) 
                        {\n    questionId
                        \n    questionFrontendId
                        \n    boundTopicId
                        \n    title
                        \n    titleSlug
                        \n    content
                        \n    translatedTitle
                        \n    translatedContent
                        \n    isPaidOnly
                        \n    difficulty
                        \n    likes
                        \n    dislikes
                        \n    isLiked
                        \n    similarQuestions
                        \n    contributors 
                            {\n      username
                            \n      profileUrl
                            \n      avatarUrl
                            \n      __typename\n    }
                        \n    langToValidPlayground
                        \n    topicTags 
                            {\n      name
                            \n      slug
                            \n      translatedName
                            \n      __typename
                            \n    }
                        \n    companyTagStats
                        \n    codeSnippets 
                            {\n      lang
                            \n      langSlug
                            \n      code
                            \n      __typename
                            \n    }
                        \n    stats
                        \n    hints
                        \n    solution 
                            {\n      id
                            \n      canSeeDetail
                            \n      __typename
                            \n    }
                        \n    status
                        \n    sampleTestCase
                        \n    metaData
                        \n    judgerAvailable
                        \n    judgeType
                        \n    mysqlSchemas
                        \n    enableRunCode
                        \n    enableTestMode
                        \n    envInfo
                        \n    libraryUrl
                        \n    __typename
                        \n }
                        \n}
                    \n"""
        }
    # get the htlm data of the target problem
    while not r:
        try:
            r = requests.post('https://leetcode.com/graphql', json = data).json()
        except:
            sleep(5)
    # ensure the content has value == ensure the problem name or url is correct
    if r['data']['question']:
        content = str(bs(r['data']['question']['content']))

# shape content as str, otherwise it returns NoneType
md_content = md(r['data']['question']['content'], heading_style="ASTERISK", strong_em_symbol = '*')
md_content = md_content.replace('\xa0', '') # remove \xa0
pattern_1 = re.compile('(?<=\n)\n(?=\n)') # 3 new lines
pattern_2 = re.compile('(?<=```\n)\n(?=\*\*Input)') # 2 new liens after quote mark
pattern_3 = re.compile('(?<=\n)\n(?=```)') # 2 new liens before quote mark
md_content = re.sub(pattern_1, '', md_content)
md_content = re.sub(pattern_2, '', md_content)
md_content = re.sub(pattern_3, '', md_content)

# obtain the question ID and question title
problem_id, problem_title = r['data']['question']['questionId'], r['data']['question']['title']

# create the template of a new Jupyter notebook
nb = nbf.v4.new_notebook()
problem = "# Problem\n\n" + md_content
summary = "# Summary\n\n"
problem_dscp = "# Problem Description\n\n"
methods = "# Methods\n\n"
method_1 = "## Method 1\n\n"
code_1 = ""
footnotes = "# Footnotes\n\n"
code_readMe = """# add the doc information to README 
from tools.setup import generate_row as g

g()"""

nb['cells'] = [nbf.v4.new_markdown_cell(problem),
               nbf.v4.new_markdown_cell(summary),
               nbf.v4.new_markdown_cell(problem_dscp),
               nbf.v4.new_markdown_cell(methods),
               nbf.v4.new_markdown_cell(method_1),
               nbf.v4.new_code_cell(code_1),
               nbf.v4.new_markdown_cell(footnotes),
               nbf.v4.new_code_cell(code_readMe),
               ]

fname = problem_id + '. ' + problem_title + '.ipynb'

cwd = os.getcwd()
code_dir = os.path.join(cwd, 'code')

# set the path of the new file
dst_dir = os.path.join(code_dir, fname)

# save Jupyter notebook
with open(dst_dir, 'w') as f:
    nbf.write(nb, f)

# add escape character to whitespace
dst_dir = dst_dir.replace(' ', '\ ')

# open new file in a new vscode tab
# ref1: https://blog.csdn.net/Guo_ya_nan/article/details/103242652
# ref2: https://cloud.tencent.com/developer/article/1540943
open_file_command = 'code ' + dst_dir
os.system(open_file_command)