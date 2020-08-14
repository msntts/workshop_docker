from flask import Flask, request
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import HTTPError
import os

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def make_response():
	req = os.environ['dst']
	
	try:
		if request.method == 'GET':
			with urlopen(req) as res:
				return res.read()
		else:
			name = request.form['name']
			if len(name) == 0:
				name = 'No name'	

			post_data = urlencode({'name': name})
			post_form_header = {'content-type': 'application/x-www-form-urlencoded'}	
		
			with urlopen(Request(req, data=post_data.encode(), method='POST', headers=post_form_header)) as res:
				return res.read()
	except HTTPError as e:
		return e.reason, e.code

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
