from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

sbepmodule = Blueprint('sbepmodule', __name__)


@sbepmodule.route('/stock-break-even-profit', methods=['GET', 'POST'])
def stockbreakevenprofit():
    form = StockBreakEvenProfitForm()
    if form.validate_on_submit():
        open = float(request.form.get('open'))
        close = float(request.form.get('close'))
        incomeReceived = float(request.form.get('incomeReceived'))
        result = calculateStockBreakEvenProfit(open, close, incomeReceived)
        return render_template('calculators/stock-break-even-profit.html', form=form, result=result)
    return render_template('calculators/stock-break-even-profit.html', form=form)


# Stock Break Even and Profit Calculation Function
def calculateStockBreakEvenProfit(open, close, incomeReceived):
    res = dict()
    hpr = ((close + incomeReceived - open) / open) * 100
    res['hpr'] = str(round(hpr, 4)) + '%'
    return res


# Stock Break Even and Profit Calculation Form
class StockBreakEvenProfitForm(FlaskForm):
    open = FloatField('Begning Value', validators=[DataRequired('Enter valid value', ),
                                                   NumberRange(min=0, message='Begning value must be greater than 0')])
    close = FloatField('Ending Value', validators=[DataRequired('Enter valid value'),
                                                   NumberRange(min=0, message='Ending value must be greater than 0')])
    incomeReceived = FloatField('Income Received', validators=[DataRequired('Enter valid value'),
                                                               NumberRange(min=0,
                                                                           message='Income Received must be greater than 0')])
    submit = SubmitField('Calculate')
