from bottle import run, route, request


@route('/', method='POST')
def hello():
    contentType = request.get_header('Content-Type')
    if contentType == "application/json":
        print(request.json)
    return 'OK'


run(host='0.0.0.0', port=8001)
