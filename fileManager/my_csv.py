import csv

def run(filePath):
    result = []
    with open(filePath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row)

    return result

if __name__ == "__main__":
    print(run('../Фильмы.csv'))