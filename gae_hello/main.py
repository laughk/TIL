from bottle import Bottle

app = Bottle()

@app.route('/', method='POST')
def hello():
    contentType = app.request.get_header('Content-Type')
    if contentType == "application/json":
        print(app.request.json)
    return 'OK'
