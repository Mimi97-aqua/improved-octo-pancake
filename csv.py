# import csv
# from script import generate_question  # Import the generate_question function
#
# def export_questions(topic, nb_questions, filename="questions.csv"):
#   """
#   Exports generated questions to a CSV file.
#
#   Args:
#       topic (str): The topic for which questions were generated.
#       nb_questions (int): The number of questions generated.
#       filename (str, optional): The filename for the CSV file. Defaults to "questions.csv".
#   """
#
#   questions = generate_question(topic, nb_questions)  # Generate questions using the imported function
#
#   with open(filename, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Question"])  # Write header row
#
#     for question in questions:
#       writer.writerow([question])
#
# # Example usage (assuming trivia_exporter.py is in the same directory)
# if __name__ == "__main__":
#   export_questions("Python", 5)
