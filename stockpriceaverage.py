from flask import Blueprint, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

spamodule = Blueprint('spamodule', __name__)


@spamodule.route('/stock-price-average', methods=['GET', 'POST'])
def stockpriceaverage():
    form = StockPriceAverageForm()
    if form.validate_on_submit():
        sharePurchased = float(request.form.get('sharePurchased'))
        purchasePrice = float(request.form.get('purchasePrice'))
        result = calculateStockPriceAverage(sharePurchased, purchasePrice)
        return render_template('calculators/stock-price-average.html', form=form, result=result)
    return render_template('calculators/stock-price-average.html', form=form)


@spamodule.route('/sendData2', methods=['POST'])
def sendData2():
    sharePurchased = request.form.getlist('sharePurchased[]')
    purchasePrice = request.form.getlist('purchasePrice[]')

    result = calculateStockPriceAverage(sharePurchased, purchasePrice)
    return jsonify(result)


# Stock Price Average Calculation Function
def calculateStockPriceAverage(sharePurchased, purchasePrice):
    res = dict()

    totalPurchasePrice = 0
    totalSharePurchased = 0
    tPurchasePrice = 0
    for i in range(min(len(sharePurchased), len(purchasePrice))):
        totalPurchasePrice += (int(sharePurchased[i]) * int(purchasePrice[i]))
        totalSharePurchased += int(sharePurchased[i])
        # tPurchasePrice += int(purchasePrice[i])

    # totalPurchasePrice = purchasePrice * sharePurchased
    # totalSharePurchased = sharePurchased
    res['stockAveragePrice'] = round(totalPurchasePrice / totalSharePurchased, 4)
    res['totalShares'] = totalSharePurchased
    res['totalStockCost'] = totalPurchasePrice
    return res


# Stock Price Average Calculation Form
class StockPriceAverageForm(FlaskForm):
    sharePurchased = FloatField('Share Purchased', validators=[DataRequired('Enter valid value', ),
                                                   NumberRange(min=0, message='Share purchased must be greater than 0')])
    purchasePrice = FloatField('Purchase Price', validators=[DataRequired('Enter valid value'),
                                                   NumberRange(min=0, message='Purchase Price must be greater than 0')])
    submit = SubmitField('Calculate')
