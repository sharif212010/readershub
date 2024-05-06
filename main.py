from flask import Flask,render_template

app=Flask(__name__)
title="Book List"
@app.route("/")
def book_list():
    return  render_template("book_list.html",title=title)

if __name__ == '__main__':
    app.run(debug=True)