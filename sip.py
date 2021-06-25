from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

sipmodule = Blueprint('sipmodule', __name__)


@sipmodule.route('/sip', methods=['GET', 'POST'])
def sip():
    form = SIPForm()
    if form.validate_on_submit():
        result = calculateSIP()
        return render_template('calculators/sip.html', form=form, result=result)
    return render_template('calculators/sip.html', form=form)


# Systematic Investment Plan (SIP) Calculation Function
def calculateSIP():
    res = dict()
    return res


# SIP Calculation Form
class SIPForm(FlaskForm):
    high = FloatField('High', validators=[DataRequired('Enter valid value', ),
                                          NumberRange(min=0, message='High value must be greater than 0')])
    low = FloatField('Low', validators=[DataRequired('Enter valid value'),
                                        NumberRange(min=0, message='Low value must be greater than 0')])
    close = FloatField('Close', validators=[DataRequired('Enter valid value'),
                                            NumberRange(min=0, message='Close value must be greater than 0')])
    submit = SubmitField('Calculate')
