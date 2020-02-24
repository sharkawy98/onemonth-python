#######
# Homework time! For your final project, you need to find an API 
# and write a Python script from scratch to access its data
#######

import facebook
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/info', methods=['POST'])
def info():
    access_token = request.form['token']

    graph = facebook.GraphAPI(access_token)
    fields = ['name','email','birthday','gender','hometown','friends','posts']
    fields = ','.join(fields)
    acc = graph.get_object('me',fields=fields)
    return render_template('display.html', data=acc)




if __name__ == '__main__':
    app.run(debug=True, host='localhost')










