from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField,FileField
from wtforms.validators import DataRequired, Length,Regexp


class PostForm(FlaskForm):
    title= StringField("Title", validators=[DataRequired(), Length(3,20)
    ,Regexp(r'^[A-Za-z\s]+$', message="please type characters only")])
    description = StringField("Description",validators=[DataRequired(),Length(20,100)])
    number_of_pages=IntegerField("number_of_pages",validators=[DataRequired()])
    image= FileField("Image", validators=[DataRequired()])
    submit = SubmitField("Create Book")

class EditForm(FlaskForm):
    title = StringField("Name", validators=[ Length(3, 20)
    ,Regexp(r'^[A-Za-z\s]+$', message="please type characters only")])
    description = StringField("Description",validators=[Length(20,100)])
    number_of_pages=IntegerField("number_of_pages")
    image= FileField("Image")
    submit = SubmitField("Edit Book")
