from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        courses = request.form.getlist('AmCourse') + request.form.getlist('PmCourse')
        data = {'name': request.form['name'], 'address': request.form['address'],
                'email': request.form['email'], 'phone': request.form['phone'],
                'courses': courses, 'lunch': request.form['lunch'],
                'price': len(courses) * 3000, 'priceVAT': len(courses) * 3750}
        return render_template('results.html', results=data)
    else:
        return redirect('/')


@app.errorhandler(405)
def method_not_allowed_handler(e):
    return redirect('/')


@app.errorhandler(404)
def method_not_allowed_handler(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run()