from flask import Blueprint, render_template

pagesmodule = Blueprint('pagesmodule', __name__)


@pagesmodule.route('/about')
def about():
    return render_template('pages/about.html')


@pagesmodule.route('/contact')
def contact():
    return render_template('pages/contact.html')


@pagesmodule.route('/help')
def helps():
    return render_template('pages/help.html')
