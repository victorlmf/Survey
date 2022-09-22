from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "survey secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['fav_language'] = request.form['fav_language']
    session['fav_food'] = request.form['fav_food']
    session['hobby'] = request.form.getlist('hobby')
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', name = session['name'], location = session['location'], fav_language = session['fav_language'], fav_food = session['fav_food'], hobbies = session['hobby'], comment = session['comment'])

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

