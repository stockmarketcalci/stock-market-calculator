from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import DateField

stockreturnmodule = Blueprint('stockreturnmodule', __name__)


@stockreturnmodule.route('/stock-return', methods=['GET', 'POST'])
def stockreturn():
    form = StockReturnForm()
    if form.validate_on_submit():
        result = calculateStockReturn()
        return render_template('calculators/stock-return.html', form=form, result=result)
    return render_template('calculators/stock-return.html', form=form)


# Stock Return Calculation Function
def calculateStockReturn():
    res = dict()
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

    purchaseDate = DateField('Date')
    soldDate = DateField('Date')

    sharesOwned = FloatField('Share Owned', validators=[DataRequired('Enter valid value', ),
                                                       NumberRange(min=0, message='Fee must be greater than 0')])
    tax = FloatField('Tax in (%)', validators=[DataRequired('Enter valid value', ),
                                               NumberRange(min=0, message='Fee must be greater than 0')])
    submit = SubmitField('Calculate')