from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

positionsizemodule = Blueprint('positionsizemodule', __name__)


@positionsizemodule.route('/position-size', methods=['GET', 'POST'])
def positionsize():
    form = PositionSizeForm()
    if form.validate_on_submit():
        result = calculatePositionSize()
        return render_template('calculators/position-size.html', form=form, result=result)
    return render_template('calculators/position-size.html', form=form)


# Position Size Calculation Function
def calculatePositionSize():
    res = dict()
    return res


# Position Size Calculation Form
class PositionSizeForm(FlaskForm):
    high = FloatField('High', validators=[DataRequired('Enter valid value', ),
                                          NumberRange(min=0, message='High value must be greater than 0')])
    low = FloatField('Low', validators=[DataRequired('Enter valid value'),
                                        NumberRange(min=0, message='Low value must be greater than 0')])
    close = FloatField('Close', validators=[DataRequired('Enter valid value'),
                                            NumberRange(min=0, message='Close value must be greater than 0')])
    submit = SubmitField('Calculate')
