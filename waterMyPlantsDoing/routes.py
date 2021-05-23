from flask import render_template, url_for, redirect, request, flash
from waterMyPlantsDoing import app
from datetime import datetime


@app.route('/')
def home():
    return render_template('main.html', bonsai=True, bigboi=True)
