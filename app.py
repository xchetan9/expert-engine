from flask import Flask, render_template
from bs4 import BeautifulSoup
import json
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/link/<url>',methods=['GET'])
def animekayo(url):
    response = requests.get("https://www.animekayo.in/p/"+url+".html")
    soup = BeautifulSoup(response.content, "html.parser")
    post_content = soup.find("div", class_="post-body entry-content")
    return str(post_content)

if __name__ == '__main__':
    app.run(debug=True)
