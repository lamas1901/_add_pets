from django.utils.text import slugify
from django.core.files.uploadedfile import UploadedFile
from django.contrib.auth.models import User

from pets.models import Pet, PetType
from pets.utils.consts import 
from json import loads
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

with open('json/dogs.json') as f:
	dogs = loads(f.read())
with open('json/cats.json') as f:
	cats = loads(f.read())

cat_pet_type = PetType.objects.get(slug='kedi')
dog_pet_type = PetType.objects.get(slug='kopek')

dog = dogs[0]

pet = Pet(
	name = dog['name'],
	slug = slugify(dog['name']),
	owner = User.objects.first(),
	price = 0,
	animal_type = dog_pet_type,
	age = dog['age'],
	sex = 'male' if dog['sex']=='Erkek' else 'female',
	breed= dog['breed'],
	city = slugify(dog['city']),
	content = dog['content'],
	special_phone = dog['owner_phone'],
	special_waphone = dog['owner_phone'],
	special_owner = dog['owner_name']
)
pet.save()
pet.photo.save(
	slugify(dog['name'])+str(pet.id)+'.jpg',
	UploadedFile(
		file=open(BASE_DIR/f'images/{slugify(dog['name'])}.jpg','rb')
	)
)
pet.save()