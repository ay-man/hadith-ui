from flask import Blueprint, render_template, request
from .search.search import search_query  

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['search']
        results = search_query(query)
        return render_template('index.html', results=results)
    return render_template('index.html', results=None)

