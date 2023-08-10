from flask import Flask, render_template
import config

app = Flask(__name__)

@app.route('/')
def splash_page():
    return render_template('splash_page.html',url=config.base_grant_url)

if __name__ == '__main__':
    app.run(debug=True)