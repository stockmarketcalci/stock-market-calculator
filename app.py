import locale

from flask import Flask, render_template
from fibonacci import fibonaccimodule
from holdingperiodreturn import hprmodule
from pivotpoint import pivotpointmodule
from riskrewardratio import riskrewardratiomodule
from stockbreakevenprofit import sbepmodule
from stockpriceaverage import spamodule
from stockreturn import stockreturnmodule
from positionsize import positionsizemodule
from systematicinvestmentplan import sipmodule
from weightedaveragecost import wacmodule

from pages import pagesmodule
locale.setlocale(locale.LC_MONETARY, 'en_IN')


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
        "desc": "A technical analysis indicator used to determine the overall trend of the market over different time frames.",
        "image": "/static/icons/pivot-point-icon.png",
        "onclick": "/pivot-point"
    },
    {
        "title": "Fibonacci Calculator",
        "desc": "A series of numbers, where a number is found by adding up two numbers before it.",
        "image": "/static/icons/fibonacci-icon.png",
        "onclick": "/fibonacci"
    },
    {
        "title": "Holding Period Return Calculator",
        "desc": "The amount of time the investment is held by an investor.",
        "image": "/static/icons/holding-period-return-icon.png",
        "onclick": "/holding-period-return"
    },
]

cardList2 = [
    {
        "title": "Stock Price Average Calculator",
        "desc": "Is calculated by dividing the amount invested with shares purchased.",
        "image": "/static/icons/stock-price-average-icon.png",
        "onclick": "/stock-price-average"
    },
    {
        "title": "Stock Break Even and Profit Calculator",
        "desc": "Is the amount of money, or change in value, for which an asset must be sold to cover the costs of acquiring and owning it.",
        "image": "/static/icons/stock-break-even-profit-icon.png",
        "onclick": "/stock-break-even-profit"
    },
    {
        "title": "Stock Return Calculator",
        "desc": "The change in price of an asset, investment, or project over time.",
        "image": "/static/icons/stock-return-icon.png",
        "onclick": "/stock-return"
    }
]

cardList3 = [
    {
        "title": "Risk Reward Ratio Calculator",
        "desc": "Measures the difference between a trade entry point to a stop-loss and a sell or take-profit order.",
        "image": "/static/icons/risk-reward-icon.png",
        "onclick": "/risk-reward-ratio"
    },
    {
        "title": "SIP Calculator",
        "desc": "A plan in which investors make regular, equal payments into a mutual fund, trading account.",
        "image": "/static/icons/sip-icon.png",
        "onclick": "/sip"
    },
    {
        "title": "Position Size",
        "desc": "The size of a position within a particular portfolio.",
        "image": "/static/icons/position-size-icon.png",
        "onclick": "/position-size"
    }
]

cardList4 = [
    {
        "title": "Weighted Average Cost Calculator",
        "desc": "For track the cost basis of shares bought at varying times.",
        "image": "/static/icons/profit-loss-icon.png",
        "onclick": "/weighted-average-cost"
    }
]


@app.errorhandler(404)
def not_found(e):
    return render_template("pages/404.html", error=e)


if __name__ == '__main__':
    app.run(debug=True)
