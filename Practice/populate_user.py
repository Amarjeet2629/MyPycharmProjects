import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Practice.settings')


import django
django.setup()


import random
from User.models import user
from faker import Faker



fakgen = Faker()


def populate(N = 5):
    for i in range(N):
        name = fakgen.name()
        l = name.split(' ')
        first = l[0]
        last = l[1]
        email = fakgen.email()

        t = user.objects.get_or_create(first_name=first, last_name=last, email=email)[0]
        t.save()


if __name__ == '__main__':
    print("Populate Script Running")
    populate(20)
    print("Population Completed")
