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
        if int(currentPrice) >= int(target):
            form.target.errors = ['Target Price must be greater than Current Price']
            print('Target Price must be greater than Current Price')
            return render_template('calculators/risk-reward-ratio.html', form=form)
        elif int(currentPrice) <= int(stopLoss):
            form.stopLoss.errors = ['Stop Loss must be lesser than Current Price']
            print('Stop Loss must be lesser than Current Price')
            return render_template('calculators/risk-reward-ratio.html', form=form)
        else:
            result = calculateRiskRewardRatio(currentPrice, stopLoss, target)
            return render_template('calculators/risk-reward-ratio.html', form=form, result=result)
    return render_template('calculators/risk-reward-ratio.html', form=form)


# Risk Reward Ratio Calculation Function
def calculateRiskRewardRatio(currentPrice, stopLoss, target):
    res = dict()
    risk = (float(currentPrice) - float(stopLoss)) / float(currentPrice)
    reward = (float(target) - float(currentPrice)) / float(currentPrice)
    if risk is 0:
        risk = 1.0
    if reward is 0:
        reward = 1.0
    rrr = float(risk) / float(reward)
    res['rrr'] = str(round(rrr, 2)) + '%'
    return res


# Risk Reward Ratio Calculation Form
class RiskRewardRatioForm(FlaskForm):
    currentPrice = FloatField('Current Price', validators=[DataRequired('Enter valid value', ),
                                                           NumberRange(min=0,
                                                                       message='Current Price must be greater than 0')])
    stopLoss = FloatField('Stop Loss', validators=[DataRequired('Enter valid value'),
                                                   NumberRange(min=0, message='Stop Loss must be greater than 0')])
    target = FloatField('Target Price', validators=[DataRequired('Enter valid value'),
                                              NumberRange(min=0,
                                                          message='Target Price must be greater than 0')])
    submit = SubmitField('Calculate')
