import locale

from flask import Blueprint, render_template, request, jsonify

sbepmodule = Blueprint('sbepmodule', __name__)


@sbepmodule.route('/stock-break-even-profit', methods=['GET', 'POST'])
def stockbreakevenprofit():
    return render_template('calculators/stock-break-even-profit.html')


@sbepmodule.route('/sendData', methods=['POST'])
def sendData():
    price = request.form.getlist('price[]')
    share = request.form.getlist('share[]')
    fee = request.form.getlist('fee[]')

    sPrice = request.form.get('sPrice')
    sShare = request.form.get('sShare')
    sFee = request.form.get('sFee')

    result = calculateStockBreakEvenProfit(price, share, fee, sPrice, sShare, sFee)
    return jsonify(result)


# Stock Break Even and Profit Calculation Function
def calculateStockBreakEvenProfit(price, share, fee, sPrice, sShare, sFee):

    res = dict()
    totalPrice = 0
    totalShares = 0
    for i in range(len(price)):
        totalPrice = totalPrice + (float(price[i]) * int(share[i]) + float(fee[i]))
        totalShares = totalShares + int(share[i])

    res['breakEvenPrice'] = locale.currency(round(totalPrice / totalShares, 2), grouping=True)
    tSaleValue = float(sPrice) * int(sShare) - float(sFee)
    res['totalSaleValue'] = locale.currency(tSaleValue, grouping=True)
    res['totalCost'] = locale.currency(totalPrice, grouping=True)
    res['sharesOwn'] = totalShares - int(sShare)
    tProfit = tSaleValue - totalPrice
    res['totalProfit'] = tProfit
    res['returnPer'] = round((tProfit / totalPrice) * 100, 2)
    res['totalShares'] = totalShares
    res['sharesSold'] = sShare

    res['price'] = price
    res['share'] = share
    res['fee'] = fee
    return res
