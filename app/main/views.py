from . import main
from flask import render_template

@main.route('/')
def index():
	return render_template('main.html')

@main.route('/purchase')
def purchase():
	return render_template('purchase.html')