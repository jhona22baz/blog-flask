#!python2.7/bin/python
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    """ Displays the index page accesible at '/'  """
    return render_template('index.html', title = 'Home')

@app.route('/hello/<name>/')
def hello(name):
    """ Displays the page greats who ever comes to visit it.
    """
    return render_template('hello.html', name=name, title = 'hello page')
    
@app.route('/blog')
def blog():
    user = {'nickname':'jhona22baz'}
    post = [
        {
            'author':{'nickname':'Jhona'},
            'titlepost':'beautiful',
            'body':'Something greatefull happend'
        },
        {
            'author':{'nickname':'Vianey'},
            "titlepost":"It's so Cool",
            "body": " I'm so prety and cool "
        }
        ]

    return render_template("blog.html",
        title = 'blog',
        user = user,
        posts = post)    

@app.route('/about')
def about():
    return render_template("about.html",title = "about")

if __name__ == '__main__':
    APP.debug=True
    APP.run(host='0.0.0.0',debug=True,port=80)
    
#host='0.0.0.0',debug=True,port=80    

