from django.core.management.base import BaseCommand
import csv
from contact.models import Project, Members

class Command(BaseCommand):
    help = 'Import roster from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                project_instance, created = Project.objects.get_or_create(project_name=row['project'])
                if created:
                    print(f"Created new project: {row['project']}")

                s = Members(student_name=row['name'], student_email=row['email'], project=project_instance)
                s.save()
                self.stdout.write(self.style.SUCCESS(f"Imported {row['name']} into {project_instance.project_name}"))
