import os

class Config:
	SECRET_KEY = '34534543345ABACAA32434'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.mailtrap.io'
	MAIL_PORT = 2525
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'ef9cd3b392bece'
	MAIL_PASSWORD = 'a802660defa5a0'