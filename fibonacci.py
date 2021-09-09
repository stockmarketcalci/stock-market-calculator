from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

fibonaccimodule = Blueprint('fibonaccimodule', __name__)


@fibonaccimodule.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    form = FibonacciForm()
    if form.validate_on_submit():
        high = float(request.form.get('high'))
        low = float(request.form.get('low'))
        if low > high:
            form.high.errors = ['High must be greater than Low']
            return render_template('calculators/fibonacci.html', form=form)
        else:
            result = calculateFibonacci(high, low)
            return render_template('calculators/fibonacci.html', form=form, result=result)
    return render_template('calculators/fibonacci.html', form=form)


# Fibonacci Calculation Function
def calculateFibonacci(high, low):
    res = dict()

    # To Calculate Uptrend Retracement
    res['ut-r-0'] = round(high - (high - low) * 0.0, 2)
    res['ut-r-23.6'] = round(high - (high - low) * 0.236, 2)
    res['ut-r-38.2'] = round(high - (high - low) * 0.382, 2)
    res['ut-r-50'] = round(high - (high - low) * 0.50, 2)
    res['ut-r-61.8'] = round(high - (high - low) * 0.618, 2)
    res['ut-r-76.4'] = round(high - (high - low) * 0.762, 2)
    res['ut-r-100'] = round(high - (high - low) * 1, 2)
    res['ut-r-138.2'] = round(high - (high - low) * 1.382, 2)

    # To Calculate Uptrend Extension
    res['ut-e-261.8'] = round(high + (high - low) * 2.618, 2)
    res['ut-e-200'] = round(high + (high - low) * 2.0, 2)
    res['ut-e-161.8'] = round(high + (high - low) * 1.618, 2)
    res['ut-e-138.2'] = round(high + (high - low) * 1.382, 2)
    res['ut-e-100'] = round(high + (high - low) * 1.0, 2)
    res['ut-e-61.8'] = round(high + (high - low) * 0.618, 2)
    res['ut-e-50'] = round(high + (high - low) * 0.5, 2)
    res['ut-e-38.2'] = round(high + (high - low) * 0.382, 2)
    res['ut-e-23.6'] = round(high + (high - low) * 0.236, 2)

    # To Calculate Downtrend Retracement
    res['dt-r-0'] = round(low + (high - low) * 0.0, 2)
    res['dt-r-23.6'] = round(low + (high - low) * 0.236, 2)
    res['dt-r-38.2'] = round(low + (high - low) * 0.382, 2)
    res['dt-r-50'] = round(low + (high - low) * 0.50, 2)
    res['dt-r-61.8'] = round(low + (high - low) * 0.618, 2)
    res['dt-r-76.4'] = round(low + (high - low) * 0.762, 2)
    res['dt-r-100'] = round(low + (high - low) * 1, 2)
    res['dt-r-138.2'] = round(low + (high - low) * 1.382, 2)

    # To Calculate Downtrend Extension
    res['dt-e-261.8'] = round(low - (high - low) * 2.618, 2)
    res['dt-e-200'] = round(low - (high - low) * 2.0, 2)
    res['dt-e-161.8'] = round(low - (high - low) * 1.618, 2)
    res['dt-e-138.2'] = round(low - (high - low) * 1.382, 2)
    res['dt-e-100'] = round(low - (high - low) * 1.0, 2)
    res['dt-e-61.8'] = round(low - (high - low) * 0.618, 2)
    res['dt-e-50'] = round(low - (high - low) * 0.5, 2)
    res['dt-e-38.2'] = round(low - (high - low) * 0.382, 2)
    res['dt-e-23.6'] = round(low - (high - low) * 0.236, 2)

    return res


# Fibonacci Calculation Form
class FibonacciForm(FlaskForm):
    high = FloatField('High', validators=[DataRequired('Enter valid value', ),
                                          NumberRange(min=0, message='High value must be greater than 0')])
    low = FloatField('Low', validators=[DataRequired('Enter valid value'),
                                        NumberRange(min=0, message='Low value must be greater than 0')])
    submit = SubmitField('Calculate')
