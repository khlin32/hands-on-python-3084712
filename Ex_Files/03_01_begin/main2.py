import csv
from pprint import pprint

EINSTEIN_CSV_22 = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN_22 = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

with open("laureates.csv","r") as james_file:
  james_reader = csv.DictReader(james_file)
  james_list = list(james_reader)

pprint(james_reader)

for james_single in james_list:
  if james_single["surname"] == "Lippmann":
    pprint(james_single)
    break

