#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from flask import Flask, render_template, request, session, url_for, redirect

from rust_api import rust

app = Flask(__name__)


MODERATORS = {
    'rafael': {'name': 'Rafael Rocha', 'password': '2504rask'},
    'heigler': {'name': 'Heigler Rocha', 'password': '4532deb'},
}


@app.route('/', methods=['GET', 'POST'])
def home():
    error = ''

    if request.method == 'POST':
        name = request.form.get('username')
        if name in MODERATORS:
            user = MODERATORS[name]
            if user['password'] == request.form.get('password'):
                session['logged_user'] = user
                return redirect(url_for('dashboard'))
            else:
                error = 'Senha inválida'
        else:
            error = 'Usuário inválido'

    return render_template('home.html', error=error)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'logged_user' not in session:
        return redirect(url_for('home'))

    command = request.args.get('command')
    if command:
        arg1 = request.args.get('arg1')
        rust(command, session['logged_user']['name'], arg1)

    return render_template('dashboard.html')


if __name__ == '__main__':
    app.secret_key = '4\xc4 \xd7\xb9\x0c>\x03-\x9e\xf1F91\xe04iib\x8a'
    app.run(host='0.0.0.0', debug=True, port=5050)
