from flask import Flask, render_template
hello = Flask(__name__)

@hello.route('/', methods=['GET'])
def my_route_page_function():
    return render_template('index.html')
