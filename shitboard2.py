import cgi
import cgitb
cgitb.enable()
import sys
sys.stdout.reconfigure(encoding='utf-8')
import bleach
import csv
import glob
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import CreateHtmlTemplate
import CreateBranch

ch = CreateHtmlTemplate.CreateHtmlTemplate()

form = cgi.FieldStorage()
articles = []
get_hash = os.environ.get('QUERY_STRING')
if form:
    value = form.getvalue('txt')
    cvalue = bleach.clean(value)
    cb = CreateBranch.CreateBranch(cvalue)
    log = cb.create_log()
    if os.path.isfile(f'./csv/{get_hash}.csv'):
        with open(f'./csv/{get_hash}.csv','a') as f:
            writer = csv.writer(f)
            writer.writerow([log[0],log[1],log[2]])
    else:
        with open(f'./csv/{log[2]}.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow([log[0],log[1],log[2]])

if get_hash:
    if os.path.isfile(f'./csv/{get_hash}.csv'):
        with open(f"./csv/{get_hash}.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                #謎の空白対策
                if row:
                    articles.append(row)
    else:
        data_list = glob.glob('./csv/*.csv')
        for i in data_list:
            with open(i,'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if get_hash in row:
                        new_branch = row
                        articles.append(row)
        with open(f'./csv/{get_hash}.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow([new_branch[0],new_branch[1],new_branch[2]])
else:
    data_list = glob.glob('./csv/*.csv')
    for i in data_list:
        with open(i,'r') as f:
            reader = csv.reader(f)
            for num,row in enumerate(reader):
                if num == 0:
                    articles.append(row)

ch.content_type()
ch.create_form(f'shitboard2.py?{get_hash}')
ch.create_branch(articles)
ch.create_html()