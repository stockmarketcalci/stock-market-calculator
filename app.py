from flask import Flask, render_template
from fibonacci import fibonaccimodule
from holdingperiodreturn import hprmodule
from pivotpoint import pivotpointmodule
from riskrewardratio import riskrewardratiomodule
from stockbreakevenprofit import sbepmodule
from stockpriceaverage import spamodule
from stockreturn import stockreturnmodule
from sip import sipmodule
from positionsize import positionsizemodule
from weightedaveragecost import wacmodule
from pages import pagesmodule

import os

# App configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'StockMarketCalculator'
app.register_blueprint(pivotpointmodule)
app.register_blueprint(fibonaccimodule)
app.register_blueprint(hprmodule)
app.register_blueprint(spamodule)
app.register_blueprint(sbepmodule)
app.register_blueprint(stockreturnmodule)
app.register_blueprint(riskrewardratiomodule)
app.register_blueprint(sipmodule)
app.register_blueprint(positionsizemodule)
app.register_blueprint(wacmodule)
app.register_blueprint(pagesmodule)


@app.route('/')
def home():
    return render_template('pages/home.html', cardList1=cardList1, cardList2=cardList2, cardList3=cardList3,
                           cardList4=cardList4)


cardList1 = [
    {
        "title": "Pivot Point Calculator",
        "desc": "This is short description of pivot point",
        "image": "http://127.0.0.1:5000/static/icons/pivot-point-icon.png",
        "onclick": "/pivot-point"
    },
    {
        "title": "Fibonacci Calculator",
        "desc": "This is short description of fibonacci",
        "image": "http://127.0.0.1:5000/static/icons/fibonacci-icon.png",
        "onclick": "/fibonacci"
    },
    {
        "title": "Holding Period Return Calculator",
        "desc": "This is short description of holding period return",
        "image": "http://127.0.0.1:5000/static/icons/holding-period-return-icon.png",
        "onclick": "/holding-period-return"
    },
]

cardList2 = [
    {
        "title": "Stock Price Average Calculator",
        "desc": "This is short description of stock price average",
        "image": "http://127.0.0.1:5000/static/icons/stock-price-average-icon.png",
        "onclick": "/stock-price-average"
    },
    {
        "title": "Stock Break Even and Profit Calculator",
        "desc": "This is short description of stock break even and profit",
        "image": "http://127.0.0.1:5000/static/icons/stock-break-even-profit-icon.png",
        "onclick": "/stock-break-even-profit"
    },
    {
        "title": "Stock Return Calculator",
        "desc": "This is short description of stock return",
        "image": "http://127.0.0.1:5000/static/icons/stock-return-icon.png",
        "onclick": "/stock-return"
    }
]

cardList3 = [
    {
        "title": "Risk Reward Ratio Calculator",
        "desc": "This is short description of risk reward ratio",
        "image": "http://127.0.0.1:5000/static/icons/risk-reward-icon.png",
        "onclick": "/risk-reward-ratio"
    },
    {
        "title": "SIP Calculator",
        "desc": "This is short description of systematic investment plan",
        "image": "http://127.0.0.1:5000/static/icons/sip-icon.png",
        "onclick": "/sip"
    },
    {
        "title": "Position Size",
        "desc": "This is short description of position size",
        "image": "http://127.0.0.1:5000/static/icons/position-size-icon.png",
        "onclick": "/position-size"
    }
]

cardList4 = [
    {
        "title": "Weighted Average Cost Calculator",
        "desc": "This is short description of weighted average cost",
        "image": "http://127.0.0.1:5000/static/icons/profit-loss-icon.png",
        "onclick": "/weighted-average-cost"
    }
]


@app.errorhandler(404)
def not_found(e):
    return render_template("pages/404.html", error=e)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,port=port)
