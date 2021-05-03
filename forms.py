from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, NumberRange, Optional

class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    first_name = StringField("First_Name", validators=[InputRequired()])
    last_name = StringField("Last_Name", validators=[InputRequired()])




class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])



class ListForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])    
    email = StringField("Email", validators=[InputRequired(), Email()])
    first_name = StringField("First_Name", validators=[InputRequired()])
    last_name = StringField("Last_Name", validators=[InputRequired()])


class FeedbackForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    content = StringField("Content", validators=[InputRequired()])


class DeleteForm(FlaskForm):
    """Delete form -- this form is intentionally blank."""

    