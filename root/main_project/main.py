from flask import Flask
from modules import application


@project_name.route('/')
def greeting():
	return "Congrat for deploying success and this message is from a docker container"


if __name__ == '__main__':
	application.run(host='0.0.0.0', port = 5000, debug=True, use_reloader=True, threaded=True)