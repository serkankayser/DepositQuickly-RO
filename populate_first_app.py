import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django

django.setup()

## FAKE POP SCRIPT

import random
from first_app.models import Witdrawal_Form
from faker import Faker


fakegen = Faker()
wd_form = [
    'name',
    'bank_name',
    'iban',
    'amount',
    'status',
    'created_date',
    'modified_date',
]

def add_wd():
    wd = Witdrawal_Form.objects.get_or_create(top_name= random.choice(wd_form))[0]
    wd.save()
    return wd

def populate(N=5):

    for entry in range(N):
        top = add_wd()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('Populating Complete!')
