#coding:utf-8

template = '''
    <head><title>%(title)s</title></head>
    <body>
    <h1>%(title)s</h1>
    <p>%(text)s</p>
    </body>

'''

data = {'title':'My Home Page','text':'Welcome to My Page'}
print template % data