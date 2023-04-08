from flask import Flask
import requests

from app import creat_app


app: Flask = creat_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25000)

