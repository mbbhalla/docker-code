from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello():
    return 'Hello page'

@app.route('/blog/<int:post_id>')
def getPost(post_id):
    return 'You requested post: %d' % post_id

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
    