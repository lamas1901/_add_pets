from django.utils.text import slugify

from pets.models import Pet, PetType
from json import loads

with open('json/dogs.json') as f:
	dogs = loads(f.read())
with open('json/cats.json') as f:
	cats = loads(f.read())