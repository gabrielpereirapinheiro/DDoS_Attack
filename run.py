from flask import Flask, request
import os
import socket


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

cwd = os.getcwd()
app = Flask(__name__, static_url_path = '/', static_folder = cwd+'/web/static')

def get_str_from_resource(rsc):
    page = ''
    with open('web/'+rsc, 'r') as f:
        page = f.read()
    return page

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        return "Teste de post no servidor"
    if request.method == 'GET':
        return get_str_from_resource('index.html')

@app.route("/<path>")
def resources(path):
    if 'css' in path or 'js' in path or 'html' in path:
    	return get_str_from_resource(path)
    return get_str_from_resource('index.html')

if __name__ == "__main__":

    ip_address = get_ip_address()

    if not ip_address:
        ip_address = '127.0.0.0'

    app.run(debug=True, host=ip_address,port=8000,threaded=True)
