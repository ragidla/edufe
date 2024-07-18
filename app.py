from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route ('/webhook', methods=['POST'])
def webhook():
	data = request.json
	print('Received message:',data)
	return jsonify(success=True, message='Response from Whatsapp bot')


@app.route('/',methods=['GET'])
def index():
	return "Hello world!, This is Whatsapp bot"


if __name__=='__main__':
	app.run(debug=True, port=5001)

