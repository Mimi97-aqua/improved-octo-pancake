from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are an excellent assistant skilled in Python programming"},
        {"role": "user", "content": "How would I solve the Tower of Hanoi problem using Python."},
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(completion.choices[0].message)

# TEST SECTION
def generate_question(topic, nb_questions):
  """
  Generates questions on a given topic and stores them in a dictionary.
  :param topic: str - The topic to generate questions for.
  :param nb_questions: int - The number of questions to generate.
  :return: A dictionary containing questions as keys and answers as values.
  """

  questions_and_answers = {}
  for _ in range(nb_questions):
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

    # Extract questions and answers from the response, handle potential formatting issues
    response = completion.choices[0].message.content
    split_lines = response.split("\n")  # Split by newlines

    # Check if there are at least 2 lines before accessing elements
    if len(split_lines) >= 2:
      question = split_lines[0].split(":")[1].strip()
      answer = split_lines[1].strip()
      questions_and_answers[question] = answer
    else:
      print(f"Warning: Unexpected response format for question {_+1}. Skipping.")

    # Print the generated question-answer dictionary
    print(questions_and_answers)

generate_question("Python", 5)
