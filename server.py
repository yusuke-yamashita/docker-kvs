import os, flask
PORT = int(os.environ['PORT'])
app = flask.Flask('app server')
@app.route('/api/vl/hello')
def index():
  return 'hello Dockerfile'
app.run(debug=False, host='0.0.0.0', port=PORT)
