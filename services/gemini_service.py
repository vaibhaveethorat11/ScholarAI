from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_scholarship_recommendations(student_data):

    prompt = f"""
    You are an expert scholarship advisor.

    Student Profile:

    Name: {student_data['name']}
    Degree: {student_data['degree']}
    Year: {student_data['year']}
    State: {student_data['state']}
    Family Income: {student_data['income']}
    CGPA: {student_data['cgpa']}
    Gender: {student_data['gender']}
    Category: {student_data['category']}
    Preferred Language: {student_data['language']}

    Recommend exactly 5 scholarships.

Format each scholarship like this:

## Scholarship Name

Match Percentage: XX%

Why This Matches:
- Point 1
- Point 2

Benefits:
- Benefit

Required Documents:
- Document 1
- Document 2

Application Tips:
- Tip

    Use clear formatting.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text