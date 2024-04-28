from flask import Flask, jsonify
import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to the QA API"


@app.route("/question")
def generate_question(topic=str, nb_questions=int):
    """
    Generates questions on a given topic using OpenAI's API.
    :param topic: str - The topic to generate questions for.
    :param nb_questions: int - The number of questions to generate.
    :return: A list of generates questions
    """

    questions_and_answers = {}

    for i in range(nb_questions):
        prompt = (f"Generate a question on {topic} alongside its answer in the format:"
                  f"Question: "
                  f"Answer: ")
        completion = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are a guru in programming languages and spoken languages."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=50,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extract questions and answers from the generated response
        response = completion.choices[0].message.content
        split_lines = response.split("\n")

        # Checks if there are at least 2 lines before accessing the elements
        if len(split_lines) >= 2:
            questions = split_lines[0].strip()
            answers = split_lines[1].strip()
            questions_and_answers[questions] = answers
        else:
            print("Unexpected/Invalid response format!")

    response = questions_and_answers
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

