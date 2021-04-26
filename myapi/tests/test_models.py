from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


from django.test import TestCase
from ..models import Hero
from .. import views
from ..serializers import HeroSerializer


# initialize the APIClient app
client = Client()

class HeroTest(TestCase):
    """ Test module for Hero model """
    
    def setUp(self):
        Hero.objects.create(
            name="Casper", alias="BLACK")
        Hero.objects.create(
            name="MUFFIN", alias="BROEN")

    def test_hero(self):
        hero_casper=Hero.objects.get(name="Casper")
        hero_casper=Hero.objects.get(name="MUFFIN")
        
    def test_get_all_heros(self):
        #get API response
        response = client.get(reverse('get_post_hero'))
        heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
