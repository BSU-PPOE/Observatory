from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('README.md')

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        search_results = perform_search(search_query)
        return render_template('search_results.md', query=search_query, results=search_results)
    return 'Method not allowed', 405
if __name__ == '__main__':
    app.run()