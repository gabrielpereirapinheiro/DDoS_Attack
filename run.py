from flask import Flask
import os

cwd = os.getcwd()
app = Flask(__name__, static_url_path = '/static', static_folder = cwd+'/shop/static')

def get_str_from_resource(rsc):
    page = ''
    with open('shop/'+rsc, 'r') as f:
        page = f.read()
    return page

@app.route("/")
def main():
    return get_str_from_resource('index.html')

@app.route("/<path>")
def resources(path):
    if 'css' in path or 'js' in path or 'html' in path:
    	return get_str_from_resource(path)
    return get_str_from_resource('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="192.168.43.208",port=8000,threaded=True)
