import os
import uuid
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
	# random_hex = secrets.token_hex(8)
	random_hex = uuid.uuid4().hex
	f_name, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
	return picture_fn

def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', sender='no-reply@smtp.mailtrap.io', recipients=[user.email])
	msg.body = ''' To reset password visit the following link
		{}
		If you din not make this request simply ignore this email

		'''.format(url_for('users.reset_token', token=token, _external=True))
	mail.send(msg)