from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Criando tabela Customer
class Customer(db.Model):
	id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
	name =  db.Column('name', db.String(150))
	position =  db.Column('position', db.String(150))
	office =  db.Column('office', db.String(150))
	age =  db.Column('age', db.Integer)
	salary =  db.Column('salary', db.String(150))
	created_at =  db.Column('created_at', db.DateTime, default=datetime.now())

	def __init__(self, name, position, office, age, salary):
		self.name =  name
		self.position = position
		self.office =  office
		self.age =  age
		self.salary =  salary

# Criando tabela Messages
class Messages(db.Model):
	id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
	name =  db.Column('name', db.String(150))
	message =  db.Column('message', db.String(150))
	created_at =  db.Column('created_at', db.DateTime, default=datetime.now())
	
	def __init__(self, name, message):
		self.name =  name
		self.message = message

# Criando tabela Order
class Order(db.Model):
	id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
	units = db.Column('units', db.Integer)
	month = db.Column('month', db.String(50))
	created_at =  db.Column('created_at', db.DateTime, default=datetime.now())

	def __init__(self, units, month):
		self.units =  units
		self.month =  month