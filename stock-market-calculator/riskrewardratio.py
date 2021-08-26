from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

riskrewardratiomodule = Blueprint('riskrewardratiomodule', __name__)


@riskrewardratiomodule.route('/risk-reward-ratio', methods=['GET', 'POST'])
def riskrewardratio():
    form = RiskRewardRatioForm()
    if form.validate_on_submit():
        open = float(request.form.get('open'))
        result = calculateRiskRewardRatio()
        return render_template('calculators/risk-reward-ratio.html', form=form, result=result)
    return render_template('calculators/risk-reward-ratio.html', form=form)


# Risk Reward Ratio Calculation Function
def calculateRiskRewardRatio():
    res = dict()
    return res


# Risk Reward Ratio Calculation Form
class RiskRewardRatioForm(FlaskForm):
    open = FloatField('Begning Value', validators=[DataRequired('Enter valid value', ),
                                                   NumberRange(min=0, message='Begning value must be greater than 0')])
    close = FloatField('Ending Value', validators=[DataRequired('Enter valid value'),
                                                   NumberRange(min=0, message='Ending value must be greater than 0')])
    submit = SubmitField('Calculate')
