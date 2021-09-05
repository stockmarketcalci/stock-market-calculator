import locale

from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

stockreturnmodule = Blueprint('stockreturnmodule', __name__)


@stockreturnmodule.route('/stock-return', methods=['GET', 'POST'])
def stockreturn():
    form = StockReturnForm()
    if form.validate_on_submit():
        purchaseFee = float(request.form.get('purchaseFee'))
        soldFee = float(request.form.get('soldFee'))
        sharesOwned = float(request.form.get('sharesOwned'))
        purchasePrice = float(request.form.get('purchasePrice'))
        soldPrice = float(request.form.get('soldPrice'))
        tax = float(request.form.get('tax'))
        year = int(request.form.get('year'))
        result = calculateStockReturn(purchaseFee, soldFee, sharesOwned, purchasePrice, soldPrice, tax, year)
        return render_template('calculators/stock-return.html', form=form, result=result)
    return render_template('calculators/stock-return.html', form=form)


# Stock Return Calculation Function
def calculateStockReturn(purchaseFee, soldFee, sharesOwned, purchasePrice, soldPrice, tax, year):
    res = dict()

    totalFees = purchaseFee + soldFee
    capitalInvested = sharesOwned * purchasePrice
    profitPrice = soldPrice - purchasePrice
    taxAmount = (capitalInvested * tax) / 100

    roi = (profitPrice * sharesOwned * 100) / (capitalInvested + tax)
    simpleRoi = roi / year
    gainLoss = profitPrice * sharesOwned - totalFees
    compoundRoi = ((profitPrice * sharesOwned) - (year * totalFees)) / (capitalInvested * year) * 100

    res['taxAmount'] = locale.currency(taxAmount, grouping=True)
    res['roi'] = round(roi, 2)
    res['simpleRoi'] = round(simpleRoi, 2)
    res['gainLoss'] = locale.currency(gainLoss, grouping=True)
    res['compoundRoi'] = round(compoundRoi, 2)
    res['investmentPeriod'] = year
    return res


# Stock Return Calculation Form
class StockReturnForm(FlaskForm):
    purchasePrice = FloatField('Price', validators=[DataRequired('Enter valid value', ),
                                                    NumberRange(min=0, message='Price must be greater than 0')])
    soldPrice = FloatField('Price', validators=[DataRequired('Enter valid value', ),
                                                NumberRange(min=0, message='Price must be greater than 0')])

    purchaseFee = FloatField('Fee', validators=[DataRequired('Enter valid value', ),
                                                NumberRange(min=0, message='Fee must be greater than 0')])
    soldFee = FloatField('Fee', validators=[DataRequired('Enter valid value', ),
                                            NumberRange(min=0, message='Fee must be greater than 0')])
    year = IntegerField('Year', validators=[DataRequired('Enter valid value', ),
                                            NumberRange(min=0, max=100,message='Enter valid Year')])
    sharesOwned = IntegerField('Share Owned', validators=[DataRequired('Enter valid value', ),
                                                          NumberRange(min=0, message='Fee must be greater than 0')])
    tax = FloatField('Tax in (%)', validators=[DataRequired('Enter valid value', ),
                                               NumberRange(min=0,max=100, message='Enter valid Tax')])
    submit = SubmitField('Calculate')
