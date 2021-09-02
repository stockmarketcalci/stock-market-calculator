from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
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

    roi = (profitPrice * sharesOwned * 100) / (capitalInvested + taxAmount)

    simpleRoi = roi / year

    gainLoss = profitPrice * sharesOwned - (totalFees + taxAmount)

    compoundRoi = (((profitPrice * sharesOwned) - (year * (totalFees + taxAmount))) / (capitalInvested * year)) * 100

    investmentPeriod = year

    res['taxAmount'] = round(taxAmount, 4)
    res['roi'] = round(roi, 4)
    res['simpleRoi'] = round(simpleRoi, 4)
    res['gainLoss'] = round(gainLoss, 4)
    res['compoundRoi'] = round(compoundRoi, 4)
    res['investmentPeriod'] = round(investmentPeriod, 4)
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
    year = FloatField('Year', validators=[DataRequired('Enter valid value', ),
                                          NumberRange(min=0, message='year must be greater than 0')])
    sharesOwned = FloatField('Share Owned', validators=[DataRequired('Enter valid value', ),
                                                        NumberRange(min=0, message='Fee must be greater than 0')])
    tax = FloatField('Tax in (%)', validators=[DataRequired('Enter valid value', ),
                                               NumberRange(min=0, message='Fee must be greater than 0')])
    submit = SubmitField('Calculate')
