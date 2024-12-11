from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page_one():
    return render_template('page_one.html')

@app.route('/page-two')
def page_two():
    return render_template('page_two.html')

if __name__ == '__main__':
    app.run(debug=True)
