from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

riskrewardratiomodule = Blueprint('riskrewardratiomodule', __name__)


@riskrewardratiomodule.route('/risk-reward-ratio', methods=['GET', 'POST'])
def riskrewardratio():
    form = RiskRewardRatioForm()
    if form.validate_on_submit():
        currentPrice = float(request.form.get('currentPrice'))
        stopLoss = float(request.form.get('stopLoss'))
        target = float(request.form.get('target'))
        result = calculateRiskRewardRatio(currentPrice, stopLoss, target)
        return render_template('calculators/risk-reward-ratio.html', form=form, result=result)
    return render_template('calculators/risk-reward-ratio.html', form=form)


# Risk Reward Ratio Calculation Function
def calculateRiskRewardRatio(currentPrice, stopLoss, target):
    res = dict()
    if currentPrice == stopLoss == target:
        res['rrr'] = 'Invalid Input '
    else:
        risk = (float(currentPrice) - float(stopLoss)) / float(currentPrice)
        reward = (float(target) - float(currentPrice)) / float(currentPrice)
        if risk is 0:
            risk = 1.0
        if reward is 0:
            reward = 1.0
        rrr = float(risk) / float(reward)
        res['rrr'] = str(round(rrr, 4)) + '%'
    return res


# Risk Reward Ratio Calculation Form
class RiskRewardRatioForm(FlaskForm):
    currentPrice = FloatField('Current Price', validators=[DataRequired('Enter valid value', ),
                                                           NumberRange(min=0,
                                                                       message='Begning value must be greater than 0')])
    stopLoss = FloatField('Stop Loss', validators=[DataRequired('Enter valid value'),
                                                   NumberRange(min=0, message='Ending value must be greater than 0')])
    target = FloatField('Target', validators=[DataRequired('Enter valid value'),
                                              NumberRange(min=0,
                                                          message='Income Received must be greater than 0')])
    submit = SubmitField('Calculate')
