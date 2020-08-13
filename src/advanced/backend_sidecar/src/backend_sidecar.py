from flask import Flask, request

LOGFILE = '/log/yoisho.log'

app = Flask(__name__)

@app.route('/', methods=["GET"])
def make_response():
	try:
		with open(LOGFILE, mode='r') as f:
			res = '<html><body>'
			for l in f.readlines():
				res = res + l + '</br>'
			res = res + '</body></html>'
			return res.encode('utf-8')
			
	except:
		return '^^;;;;;;', 500


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
