from bottle import route, run

@route('/single')
def returnsingle():
    return { "id": 1, "name": "Test Item 1" }

@route('/containsarray')
def returncontainsarray():
    return { "items": [{ "id": 1, "name": "Test Item 1" }, { "id": 2, "name": "Test Item 2" }] }

@route('/array')
def returnarray():
    return [{ "id": 1, "name": "Test Item 1" }, { "id": 2, "name": "Test Item 2" }]

@route('/addtwo/<one>/<two>')
def returnAddTwo(one, two):
    return { "sum": int(one) + int(two) }

run(host='localhost', port=8080, debug=True, reloader=True)


