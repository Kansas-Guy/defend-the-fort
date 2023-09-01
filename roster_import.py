import csv
from contact.models import Roster


team_dict = {
    'Football': 1,
    'Volleyball': 2,
    "Men's Soccer": 3,
    "Women's Soccer": 4,
    "Men's Golf": 5,
    "Women's Golf": 6,
    "Cross Country": 7,
    "Baseball": 8,
    "Wrestling": 9,
    "Track and Field": 10,
    "Men's Basketball": 11,
    "Women's Basketball": 12,
    "Softball": 13,
    "Tennis": 14,
    "Women's Wrestling": 15,
    "Tiger Debs": 16,
    "Cheerleading": 18,
}

def roster_import(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            s = Roster(student_name=row['name'], team_id=team_dict[row['sport']])
            s.save()
