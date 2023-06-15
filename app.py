from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    # Perform the search operation with the query and generate the search results
    # You can define the logic for the search operation here

    # Pass the search results to a template for rendering
    return render_template('search_results.md', query=query, results=results)