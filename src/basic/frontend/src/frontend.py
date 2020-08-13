from flask import Flask, request
from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError
import os

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def make_response():
	if request.method == 'GET':
		return '<html><body><form method="POST"><input type="text" name="name" placeholder="your name"><input type="submit" value="yoisho!"></form></body></html>'
	else:
		name_quoted = quote(request.form['name'])
		req = os.environ['dst'] + '/?name=' + name_quoted
		try:
			with urlopen(req) as res:
				return '<html><body><h1>'.encode('utf-8') + res.read() + u'</h1></body></html>'.encode('utf-8')
		except HTTPError as e:
			return e.read(), e.code

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
