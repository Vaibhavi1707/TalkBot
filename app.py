from flask import Flask,render_template
import voice_enabled_chatbot
app=Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html'),voice_enabled_chatbot.run()
if __name__=="__main__":
	app.run(host='127.0.0.1',port='7000',debug=True)
