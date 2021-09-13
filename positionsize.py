import locale

from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

positionsizemodule = Blueprint('positionsizemodule', __name__)


@positionsizemodule.route('/position-size', methods=['GET', 'POST'])
def positionsize():
    form = PositionSizeForm()
    if form.validate_on_submit():
        accountSize = float(request.form.get('accountSize'))
        riskPerTrade = float(request.form.get('riskPerTrade'))
        buyPrice = float(request.form.get('buyPrice'))
        stopLoss = float(request.form.get('stopLoss'))
        targetPrice = float(request.form.get('targetPrice'))

        if int(buyPrice) >= int(targetPrice):
            form.targetPrice.errors = ['Target Price must be greater than Buy Price']
            print('Target Price must be greater than Current Price')
            return render_template('calculators/position-size.html', form=form)
        elif int(buyPrice) <= int(stopLoss):
            form.stopLoss.errors = ['Stop Loss must be lesser than Buy Price']
            print('Stop Loss must be lesser than Current Price')
            return render_template('calculators/position-size.html', form=form)
        else:
            result = calculatePositionSize(accountSize, riskPerTrade, buyPrice, stopLoss, targetPrice)
            return render_template('calculators/position-size.html', form=form, result=result)
    return render_template('calculators/position-size.html', form=form)


# Position Size Calculation Function
def calculatePositionSize(accountSize, riskPerTrade, buyPrice, stopLoss, targetPrice):
    res = dict()

    riskValue = (accountSize * riskPerTrade) / 100
    temp = riskValue / (buyPrice - stopLoss)
    positionSize = temp * buyPrice
    profit = (targetPrice - buyPrice) * temp
    loss = (buyPrice - stopLoss) * temp
    riskRewardRatio = profit / loss

    res['riskValue'] = locale.currency(round(riskValue, 4), grouping=True)
    res['positionSize'] = locale.currency(round(positionSize, 4), grouping=True)
    res['profit'] = locale.currency(round(profit, 4), grouping=True)
    res['loss'] = locale.currency(round(loss, 4), grouping=True)
    res['riskRewardRatio'] = round(riskRewardRatio, 2)

    return res


# Position Size Calculation Form
class PositionSizeForm(FlaskForm):
    accountSize = FloatField('Account Size', validators=[DataRequired('Enter valid value', ),
                                          NumberRange(min=0, message='Account size must be greater than 0')])
    riskPerTrade = FloatField('Risk Per Trade', validators=[DataRequired('Enter valid value'),
                                        NumberRange(min=0, message='Risk per trade must be greater than 0')])
    buyPrice = FloatField('Buy Price', validators=[DataRequired('Enter valid value'),
                                            NumberRange(min=0, message='Buy price must be greater than 0')])
    targetPrice = FloatField('Target Price', validators=[DataRequired('Enter valid value'),
                                                 NumberRange(min=0, message='Target price must be greater than 0')])
    stopLoss = FloatField('Stop Loss', validators=[DataRequired('Enter valid value'),
                                               NumberRange(min=0, message='Stop Loss value must be greater than 0')])
    submit = SubmitField('Calculate')