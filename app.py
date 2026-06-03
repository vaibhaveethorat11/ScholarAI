from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():

    student_data = {
        "name": request.form['name'],
        "degree": request.form['degree'],
        "year": request.form['year'],
        "income": request.form['income']
    }

    return render_template(
        'recommendations.html',
        student=student_data
    )


if __name__ == '__main__':
    app.run(debug=True)