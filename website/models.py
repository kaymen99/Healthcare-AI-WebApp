from . import db
from sqlalchemy.sql import func


class Messages(db.Model):
	"""model for stocking the messages from contact us"""
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime(timezone=True), default=func.now())
	name = db.Column(db.String(150))
	email = db.Column(db.String(150))
	messages = db.Column(db.String(10000))

	def __str__(self):

		return self.name
	
