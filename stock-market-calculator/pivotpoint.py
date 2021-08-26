from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

pivotpointmodule = Blueprint('pivotpointmodule', __name__)


@pivotpointmodule.route('/pivot-point', methods=['GET', 'POST'])
def pivotpoint():
    form = PivotPointForm()
    if form.validate_on_submit():
        high = float(request.form.get('high'))
        low = float(request.form.get('low'))
        close = float(request.form.get('close'))
        result = calculatePivotPoint(high, low, close)
        return render_template('calculators/pivot-point.html', form=form, result=result)
    return render_template('calculators/pivot-point.html', form=form)


# Pivot Point Calculation Function
def calculatePivotPoint(high, low, close):
    res = dict()

    pp = (high + low + close) / 3
    r1 = 2 * pp - low
    r2 = pp + (high - low)
    r3 = high + 2 * (pp - low)
    s1 = 2 * pp - high
    s2 = pp - (high - low)
    s3 = pp - 2 * (high - low)

    res['pp'] = round(pp, 4)
    res['r1'] = round(r1, 4)
    res['r2'] = round(r2, 4)
    res['r3'] = round(r3, 4)
    res['s1'] = round(s1, 4)
    res['s2'] = round(s2, 4)
    res['s3'] = round(s3, 4)

    return res


# Pivot Point Calculation Form
class PivotPointForm(FlaskForm):
    high = FloatField('High', validators=[DataRequired('Enter valid value', ),
                                          NumberRange(min=0, message='High value must be greater than 0')])
    low = FloatField('Low', validators=[DataRequired('Enter valid value'),
                                        NumberRange(min=0, message='Low value must be greater than 0')])
    close = FloatField('Close', validators=[DataRequired('Enter valid value'),
                                            NumberRange(min=0, message='Close value must be greater than 0')])
    submit = SubmitField('Calculate')
