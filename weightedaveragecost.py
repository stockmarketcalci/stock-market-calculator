from flask import Blueprint, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

wacmodule = Blueprint('wacmodule', __name__)


@wacmodule.route('/weighted-average-cost', methods=['GET', 'POST'])
def weightedaveragecost():

    return render_template('calculators/weighted-average-cost.html')


@wacmodule.route('/sendWAC', methods=['GET','POST'])
def sendWAC():
    weight = request.form.getlist('weight[]')
    value = request.form.getlist('value[]')

    result = calculateWeightedAverageCost(weight, value)
    return jsonify(result)


# Weighted Average Cost Calculation Function
def calculateWeightedAverageCost(weight, value):
    res = dict()
    totalWAC = 0
    totalWeight = 0
    for i in range(min(len(weight), len(value))):
        totalWeight = totalWeight + float(weight[i])
        print(weight[i])
        print(value[i])
        totalWAC = totalWAC + (float(weight[i]) * float(value[i]))

    res['weightedAverageCost'] = round(totalWAC / totalWeight,2)
    res['totalWeight'] = round(totalWeight,2)
    return res
