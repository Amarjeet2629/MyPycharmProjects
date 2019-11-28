import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Practice1.settings')


import django
django.setup()


import random
from Login.models import user
from faker import Faker


fake = Faker()

def populate(N = 5):
    for i in range(N):
        name = fake.name()
        l = name.split(' ')
        first = l[0]
        last = l[1]
        email = fake.email()
        
        t = user.objects.get_or_create(first = first,last = last,email=email)[0]
        t.save()

    return 0


if __name__ == "__main__":
    print('running Script')
    populate(20)
    print('script success')