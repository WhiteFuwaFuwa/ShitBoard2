class CreateHtmlTemplate:
    def __init__(self, text = 'テキストがありません'):
        self.text  = text
        self.branch = ''
    
    def content_type(self):
        return print("Content-Type: text/html\n")
    
    def create_form(self,form):
        self.form = form
        self.form = f'''<form action = "{self.form}" method = "POST">
            <input type = "text" name = "txt">
            <input type = "submit" value = "投稿">
        </form>
'''
 
    def create_branch(self,branch):
        for i in branch:
            self.branch += f'<li><a href = "shitboard2.py?{i[2]}">{i[0]} : {i[1]}</a></li>'

    def create_html(self):
        self.html = f'''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>仮</title>
    </head>
    <body>
        {self.form}
        <ul>{self.branch}</ul>
    </body>
</html>
'''
        return print(self.html)