import csv
from contact.models import Roster, Team


team_dict = {
    'Football': 1,
    'Volleyball': 2,
    "Men's Soccer": 3,
    "Women's Soccer": 4,
    "Men's Golf": 5,
    "Women's Golf": 6,
    "Cross Country": 7,
    "Baseball": 8,
    "Men's Wrestling": 9,
    "Track and Field/Cross Country": 10,
    "Men's Basketball": 11,
    "Women's Basketball": 12,
    "Softball": 13,
    "Tennis": 14,
    "Women's Wrestling": 17,
    "Tiger Debs": 16,
    "Cheerleading": 18,
}

def roster_import(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            team_instance = Team.objects.get(id=team_dict[row['sport']])
            s = Roster(student_name=row['name'], team=team_instance)
            s.save()
