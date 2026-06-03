from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_scholarship_recommendations(student_data):

    prompt = f"""
    You are an expert scholarship advisor for Indian students.

    Student Profile:
    Name: {student_data['name']}
    Degree: {student_data['degree']}
    Year: {student_data['year']}
    State: {student_data['state']}
    Family Income: {student_data['income']}

    Recommend 5 scholarships.

    For each scholarship provide:
    1. Scholarship Name
    2. Why the student qualifies
    3. Benefits
    4. Required Documents

    Keep the language simple and student-friendly.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text