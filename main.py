import json

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/member')
def member():
    with open('static/members.json', 'r', encoding='utf8') as f:
        members = json.load(f)['members']
    return render_template('member.html', members=members)


@app.route('/')
def index():
    return redirect('/member')


if __name__ == '__main__':
    app.run("", 8080)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
