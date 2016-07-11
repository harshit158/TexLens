from flask import Flask, render_template, request
app = Flask(__name__)
from text_sum import *


@app.route("/")
def template_test():
    return render_template('index.html', my_string="Whedss!")

@app.route("/", methods=['POST'])
def template_test2():
	# return render_template('index.html', my_string="Whedss!")
	text=request.form["input"]
	text=summarize(text)
	return render_template('index.html', sum_text=text)

if __name__ == '__main__':
    app.run(debug=True)