from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField, SelectField, SubmitField, ValidationError
from wtforms.validators import Required, Email

class UpdateProfile (FlaskForm):
    """
    Class to update user profile
    """
    bio = TextAreaField ('Write something about you...', validators = [Required()])
    submit = SubmitField ('Submit')

# Class for creating a pitch  
class PitchForm(FlaskForm):

    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Tech','Tech'),('Meme','Meme'),('Fashion','Fashion')],validators=[Required()])
    post = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a Comment',validators = [Required()])
    submit = SubmitField('Submit')  
    
class CategoryForm(FlaskForm):
     name = StringField ('Category Name', validators = [Required()])
     submit = SubmitField('Add')