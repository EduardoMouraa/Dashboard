from flask import Flask, render_template, request, redirect, url_for
from pusher import Pusher

from models import *
from utils import *
from datetime import datetime
from jinja2 import environment
from template_tag.filtros import * 
from decouple import config
from init import create_app

# Variáveis #
APP_ID = config('APP_ID', cast=str)
KEY = config('KEY', cast=str)
SECRET = config('SECRET', cast=str)
CLUSTER = config('CLUSTER', cast=str)
SSL = config('SSL', cast=bool)
DEBUG= config('DEBUG', cast=bool)
HOST= config('HOST', cast=str)
# \Variáveis #

app = create_app()

pusher = Pusher(
  app_id=APP_ID,
  key=KEY,
  secret=SECRET,
  cluster=CLUSTER,
  ssl=True
)

# FiltrosformatedMessage
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['datetimeformatMessage'] = datetimeformatMessage
app.jinja_env.filters['formatMessage'] = formatMessage
app.jinja_env.filters['formatSizeBoxMessage'] = formatSizeBoxMessage

@app.route('/')
def index():
	data = {}
	return render_template('index.html', data=data)

@app.route('/dashboard')
def dashboard():
	order_Data = {}

	today = datetime.today()
	year = today.strftime("%Y")
	month = today.strftime("%m")

	order = getVal(Order)
	data = {
		'customers': Customer.query.all(),
		'messages': Messages.query.all(),
		'order': order if order else ''
	}
	return render_template('dashboard.html', data=data)

@app.route('/orders', methods=['POST'])
def order():
	data = request.form
	# Salvar na tabela Order
	orders = Order(int(data['units']), data['month'])
	db.session.add(orders)
	db.session.commit()

	# Tratar o mês
	month = data['month'][5:7]
	# Sumir atualização para o Pusher - order
	pusher.trigger(u'order', u'place', {
		u'units': data['units'],
		u'month': month
	})

	return redirect(url_for('index', data={'aviso': "Sucesso"}))

@app.route('/message', methods=['POST'])
def message():
	data = request.form

	# Salvar na tabela Messages
	messages = Messages(data['name'], data['message'])
	db.session.add(messages)
	db.session.commit()

	# Sumir atualização para o Pusher - message
	pusher.trigger(u'message', u'send', {
		u'name': data['name'],
		u'message': data['message']
	})

	return redirect(url_for('index', data={'aviso': "Sucesso"}))

@app.route('/customer', methods=['POST'])
def customer():
	data = request.form
	
	# Salvar no banco
	custumer_result = Customer(data['name'], data['position'], data['office'], data['age'], data['salary'])
	db.session.add(custumer_result)
	db.session.commit()

	# Sumir atualização para o Pusher - customer
	pusher.trigger(u'customer', u'add', {
		u'name': data['name'],
		u'position': data['position'],
		u'office': data['office'],
		u'age': data['age'],
		u'salary': data['salary'],
	})
	return redirect(url_for('index', data={'aviso': "Sucesso"}))

@app.route('/tasks')
def tasks():
	data = {
		'all_tasks': False,
		'tasks': False,
		'user': ''
	}
	return render_template('to_do/tasks/dashboard.html', data=data)

if __name__ == '__main__':	
	app.run(debug=DEBUG, host=HOST)
