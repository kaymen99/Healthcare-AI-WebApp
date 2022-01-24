from flask import Blueprint, render_template, request, redirect, url_for
from .models import Messages
from . import db

messages = Blueprint('messages', __name__)


@messages.route("/msg", methods=['GET', 'POST'])
def msg():
    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        new_message = Messages(name=name, email=email, messages=message)
        db.session.add(new_message)
        db.session.commit()

        return redirect("/")
    else:
        return render_template(r'base.html')
