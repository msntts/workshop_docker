from flask import Flask, request
from urllib.parse import unquote
import logging
from time import gmtime

LOGFILE = '/log/yoisho.log'

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(LOGFILE)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(message)s')
fh.setFormatter(formatter)
app.logger.addHandler(fh)

YOISHOS = ["キレてるよ！", "でかいよ！", "腹筋6LDKかい！", "パワー！！"]

@app.route('/', methods=["GET"])
def make_response():
		user = unquote(request.args.get('name'))
		if len(user) > 0:
			app.logger.info(user + 'さんが利用しました^^')
			return user + 'さん！' + YOISHOS[gmtime().tm_sec % len(YOISHOS)]
		else:
			app.logger.info('名前ぐらい入れるやろ常識的に考えて')
			return '<html><body><h1>¯\\_(ツ)_/¯<h1></body></html>', 500


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
