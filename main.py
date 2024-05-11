from flask import Flask,render_template

app=Flask(__name__)
title="Book List"
books= [
    {
        "id":1,
        "title": "Aladin",
        "author":"Abdullah Al-sharif",
        "year":1925,
        "description":"how can people see some carpets ?"
    },
    {
        "id":2,
        "title":"Avatar",
        "author":"Mohammed Al-Sharif",
        "year":1962,
        "description":"what are avatars used for?"
    }
]
@app.route("/")
def book_list():
    return  render_template("book_list.html",title=title,books=books)


@app.route("/book/<int:book_id>")
def book_detail(book_id):
    book= next((book for book in books if book['id']==book_id),None)
    if book:
        return render_template("book_detail.html",book=book)
    else:
        return "book not found", 404


if __name__ == '__main__':
    app.run(debug=True)