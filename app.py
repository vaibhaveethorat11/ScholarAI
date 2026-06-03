from flask import Flask, render_template, request
from services.gemini_service import get_scholarship_recommendations

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
        "state": request.form['state'],
        "income": request.form['income']
    }

    recommendations = get_scholarship_recommendations(student_data)

    return render_template(
        'recommendations.html',
        recommendations=recommendations,
        student=student_data
    )

if __name__ == '__main__':
    app.run(debug=True)