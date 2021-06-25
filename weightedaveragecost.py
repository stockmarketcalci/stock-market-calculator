from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

wacmodule = Blueprint('wacmodule', __name__)


@wacmodule.route('/weighted-average-cost', methods=['GET', 'POST'])
def weightedaveragecost():
    form = WeightedAverageCostForm()
    if form.validate_on_submit():
        result = calculateWeightedAverageCost()
        return render_template('calculators/weighted-average-cost.html', form=form, result=result)
    return render_template('calculators/weighted-average-cost.html', form=form)


# Weighted Average Cost Calculation Function
def calculateWeightedAverageCost():
    res = dict()
    return res


# WeightedAverageCost Calculation Form
class WeightedAverageCostForm(FlaskForm):
    high = FloatField('High', validators=[DataRequired('Enter valid value', ),
                                          NumberRange(min=0, message='High value must be greater than 0')])
    low = FloatField('Low', validators=[DataRequired('Enter valid value'),
                                        NumberRange(min=0, message='Low value must be greater than 0')])
    close = FloatField('Close', validators=[DataRequired('Enter valid value'),
                                            NumberRange(min=0, message='Close value must be greater than 0')])
    submit = SubmitField('Calculate')
