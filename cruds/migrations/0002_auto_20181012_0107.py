from django.db import migrations
from cruds.models import Department, KnowledgeBase, Question

def create_data(apps, schema_editor):
    department = Department(name='HR', description='Human Resources')
    department.save()
    knowledge_base = KnowledgeBase(department=department, name='General Policies')
    knowledge_base.save()
    question1 = Question(knowledge_base=knowledge_base, text='This is question 1', answer='This is answer 1')
    question1.save()
    question2 = Question(knowledge_base=knowledge_base, text='This is question 2', answer='This is answer 2')
    question2.save()

class Migration(migrations.Migration):

    dependencies = [
        ('cruds', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data)
    ]
