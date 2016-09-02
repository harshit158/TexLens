import os
import sys

# sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
# sys.path.insert(0, "D:\Projects\TexSum\lib")

from flask import Flask, render_template, request
app = Flask(__name__)
# from texsum import *


@app.route('/')
def template_test():
    return "hello" #render_template('index.html'), my_string="Whedss!")

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

# @app.route("/", methods=['POST'])
# def template_test2():
# 	# return render_template('index.html', my_string="Whedss!")
# 	text=request.form["input"]
# 	txt={}
# 	return render_template('index.html', sum_text=summarize(text))

if __name__ == "__main__":
	app.debug=True
    app.run()