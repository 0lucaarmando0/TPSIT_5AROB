from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
 {'id': 0, 
 'title': 'Il nome della Rosa', 
 'author': 'Umberto Eco',
 'published': '1980'},

 {'id': 1, 
 'title': 'Il problema dei tre corpi', 
 'author': 'Liu Cixin', 
 'published': '2008'},

 {'id': 2,
 'title': 'Fondazione', 
 'author': 'Isaac Asimov', 
 'published': '1951'} 
 ]



@app.route('/', methods=['GET'])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di web API.</p>"

@app.route('/api')
def api_all():
    return jsonify(books)

@app.route('/findip')
def findip():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        print ("Error : No id field provided")

    result =[]

    for book in books:
        if book['id'] == id:
            result.append(book)

    return jsonify(result)

# ------------------------------------------------------------------------
@app.route('/findtitle')
def findtitle():
    if 'title' in request.args:
        title = request.args['title']
    else:
        return "The title field is required"
    
    result =[]

    for book in books:
        if book['title'] == title:
            result.append(book)

    return jsonify(result)    

# ----------------------------------------------------------------
@app.route('/findauthor')
def findauthor():

    if 'author' in request.args:
        author = request.args['author']
    else:
        return "The author field is required"
    
    result = []

    for book in books:
        if book['author'] == author:
            result.append(book)

    return jsonify(result)

# ------------------------------------------------------------------
@app.route('/findpublished')
def findpublished():
    if 'published' in request.args:
        published = request.args['published']
    else:
        return "The published field is required"

    result = []

    for book in books:
        if book['published'] == published:
            result.append(book)
    
    return jsonify(result)


# ------------------------------ ------------------------------------
if __name__ == '__main__':
    app.run(debug=True)