from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

spamodule = Blueprint('spamodule', __name__)


@spamodule.route('/stock-price-average', methods=['GET', 'POST'])
def stockpriceaverage():
    form = StockPriceAverageForm()
    if form.validate_on_submit():
        open = float(request.form.get('open'))
        close = float(request.form.get('close'))
        incomeReceived = float(request.form.get('incomeReceived'))
        result = calculateStockPriceAverage(open, close, incomeReceived)
        return render_template('calculators/stock-price-average.html', form=form, result=result)
    return render_template('calculators/stock-price-average.html', form=form)


# Stock Price Average Calculation Function
def calculateStockPriceAverage(open, close, incomeReceived):
    res = dict()
    hpr = ((close + incomeReceived - open) / open) * 100
    res['hpr'] = str(round(hpr, 4)) + '%'
    return res


# Stock Price Average Calculation Form
class StockPriceAverageForm(FlaskForm):
    open = FloatField('Begning Value', validators=[DataRequired('Enter valid value', ),
                                                   NumberRange(min=0, message='Begning value must be greater than 0')])
    close = FloatField('Ending Value', validators=[DataRequired('Enter valid value'),
                                                   NumberRange(min=0, message='Ending value must be greater than 0')])
    incomeReceived = FloatField('Income Received', validators=[DataRequired('Enter valid value'),
                                                               NumberRange(min=0,
                                                                           message='Income Received must be greater than 0')])
    submit = SubmitField('Calculate')
