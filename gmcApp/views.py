
from datetime import datetime
from flask import Flask, render_template,request,send_file
import latex.backtracking.backtracking_1step_booklet_maker as backtrack

app = Flask(__name__)


# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

ops={'Addition':1,'Subtraction':2,'Multiplication':3,'Division':4, 'Random':5}

@app.route('/')
def index():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home Page',

    ) 

@app.route('/btonestep')
def btonestep():
    return render_template(
        'btonestep.html',
        ops=ops.keys(),
    )

@app.route('/btonestepcreate')
def btonestepcreate():
    operation = ops[request.args.get('operation')]
    num_q=int(request.args.get('num_q'))
    file=backtrack.create_booklet(num_q,operation)
    return send_file(file, as_attachment=True)
    # return render_template(
    #     'btonestep.html',
    #     ops=ops.keys(),)
    #return str(file)



# @app.route('/viewYearSelect')
# def viewYearSelect():
#     """Renders the home page."""
#     years = bl.getYears()
#     return render_template(
#         'viewYearSelect.html',
#         title='View By Year',
#         years=years,
#     )


# @app.route('/viewByYear',methods=['POST'])
# def viewByYear():
#     in_year = int(request.form['optionYear'])
#     years = bl.getYears()
#     books = bl.getBooks(year=in_year)
#     return render_template(
#         'viewByYear.html',
#         title='View By Year',
#         year=in_year,
#         years=years,
#         books=books,
#     )
    


# @app.route('/viewSubjectSelect')
# def viewSubjectSelect():
#     """Renders the home page."""
#     subjects = bl.getSubjects()
#     return render_template(
#         'viewSubjectSelect.html',
#         title='View By Subject',
#         subjects=subjects,
#     )


# @app.route('/viewBySubject',methods=['POST'])
# def viewBySubject():
#     subject = (request.form['optionSubject'])
#     subjects = bl.getSubjects()
#     books = bl.getBooks(subject=subject)
#     return render_template(
#         'viewBySubject.html',
#         title='View By Subject',
#         subject=subject,
#         subjects=subjects,
#         books=books,
#     )
    
# @app.route('/editBook')
# def editBook():
#     isbn = request.args.get('isbn')
#     book = bl.getBookbyISBN(isbn)
#     subjects = bl.getSubjects()
#     years = bl.getYears()
#     return render_template(
#         'editBook.html',
#         title='Edit Book',
#         book=book,
#         subjects=subjects,
#         years=years,
#     )

# @app.route('/updateBook')
# def updateBook():
#     isbn = request.args.get('isbn')
#     year = request.args.get('year')
#     title = request.args.get('title')
#     subject = request.args.get('subject')
#     pcode = request.args.get('pcode')
#     rrp = request.args.get('rrp')
#     supplier = request.args.get('supplier')
#     book = bl.updateBook(year,subject,title,rrp,pcode,isbn,supplier)
#     bl.updateBookCSV()
#     return render_template(
#         'successUpdate.html',
#         title='Booked Updated',
#         book=book,
#     )


# @app.route('/addBookView')
# def addBookView():
#     subjects = bl.getSubjects()
#     years = bl.getYears()
#     return render_template(
#         'addBook.html',
#         title='Add Book',
#         subjects=subjects,
#         years=years,
#     )

# @app.route('/addBook')
# def addBook():
#     isbn = request.args.get('isbn')
#     year = request.args.get('year')
#     title = request.args.get('title')
#     subject = request.args.get('subject')
#     pcode = request.args.get('pcode')
#     rrp = request.args.get('rrp')
#     supplier = request.args.get('supplier')
#     bl.addBook(year,subject,title,rrp,pcode,isbn,supplier)
#     book =bl.book(year,subject,title,rrp,pcode,isbn,supplier)
#     return render_template(
#         'successUpdate.html',
#         title='Booked Updated',
#         book=book,
#     )


# @app.route('/createOrder')
# def createOrder():
#     result = bl.createOrder()
#     books = bl.orderBooks
#     return render_template(
#         'createOrder.html',
#         title='Book Order',
#         books=books,
#         totalCost = str(format(result[1],".2f")),
#         totalQty = result[0]
#     )

if __name__ == '__main__':
    # import os


    # HOST = os.environ.get('SERVER_HOST', 'localhost')
    # try:
    #     PORT = int(os.environ.get('SERVER_PORT', '5555'))
    # except ValueError:
    #     PORT = 5555
    app.run()
