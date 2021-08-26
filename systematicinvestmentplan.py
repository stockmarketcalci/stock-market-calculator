from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, IntegerField
from wtforms.validators import DataRequired

sipmodule = Blueprint('sipmodule', __name__)


@sipmodule.route('/sip', methods=['GET', 'POST'])
def sip():
    form = SIPForm()
    if form.validate_on_submit():
        initalDeposit = float(request.form.get('initalDeposit'))
        # regularDeposit = float(request.form.get('regularDeposit'))
        expectedReturnRate = float(request.form.get('expectedReturnRate'))
        depositTerm = int(request.form.get('depositTerm'))
        result = calculateSIP(initalDeposit, expectedReturnRate, depositTerm)
        return render_template('calculators/sip.html', form=form, result=result)
    return render_template('calculators/sip.html', form=form)


# Systematic Investment Plan (SIP) Calculation Function
def calculateSIP(initalDeposit, expectedReturnRate, depositTerm):
    res = dict()

    Total_deposit = initalDeposit * depositTerm * 12
    deposit_term = depositTerm * 12
    return_rate = expectedReturnRate / 100
    return_rate /= 12
    amount = 0
    for month in range(deposit_term):
        amount = (amount + initalDeposit) * (1 + return_rate)

    tr = amount - Total_deposit

    res['totalReturn'] = round(tr, 4)
    res['totalDeposit'] = round(Total_deposit, 4)
    res['maturity'] = round(amount, 4)

    return res


# SIP Calculation Form
class SIPForm(FlaskForm):
    initalDeposit = FloatField('Inital Deposit (ID)', validators=[DataRequired()])
    # regularDeposit = FloatField('Regular Deposit (RD)',validators=[DataRequired()])
    expectedReturnRate = FloatField('Expected Return Rate', validators=[DataRequired()])
    depositTerm = IntegerField('Deposit Term (in Months)', validators=[DataRequired()])
    submit = SubmitField('Calculate')
