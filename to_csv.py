import csv

def store_as_csv(data, filename="questions.csv"):
    '''
    Saves the generated questions and answers to a csv file
    :param data:
    :param filename: str
    :return:
    '''

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()  # Get fieldnames from the first dictionary
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Questions and answers have been successfully saved to {filename}")