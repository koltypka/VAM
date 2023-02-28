import csv

def csv_open(filePath):
    result = []
    with open(filePath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row)

    return result

if __name__ == "__main__":
    print(csv_open('../Фильмы.csv'))