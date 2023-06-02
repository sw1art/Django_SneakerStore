from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model

from .models import Sneaker, Brand, Size, Review


class SneakerTets(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'review_user',
            email = 'review_user@email.com',
            password = '23password32'
            )
        self.brand = Brand.objects.create(
            name='Nike', 
            description='Nike brand'
            )
        self.size = Size.objects.create(
            size_us = 0.5, 
            size_ru = 43, 
            size_eu = 44, 
            size_uk = 9.5, 
            size_cm = 27
            )
        self.sneaker = Sneaker.objects.create(
            title = 'Мужские Nike Air Max 90',
            brand = self.brand,
            description = 'Nike Air Max 90 sneakers',
            feature = 'color: white',
            price = 15000,
            release_date = '2023-06-02',
            )
        self.review = Review.objects.create(
            sneaker = self.sneaker, 
            author = self.user,
            review = 'Review. five stars'
            )
        self.url = reverse('sneaker_detail', 
                           kwargs={
                               'slug': self.sneaker.slug,
                               'uuid': self.sneaker.id,
                               }
            )

    # Databases test
    def test_sneaker_creation(self):
        self.assertEqual(Sneaker.objects.count(), 1)
        self.assertEqual(self.sneaker.title, 'Мужские Nike Air Max 90')
        self.assertEqual(self.sneaker.brand, self.brand)
        self.assertEqual(self.sneaker.description, 'Nike Air Max 90 sneakers')
        self.assertEqual(self.sneaker.feature, 'color: white')
        self.assertEqual(self.sneaker.price, 15000)
        self.assertEqual(self.sneaker.release_date, '2023-06-02')
        self.assertEqual(self.sneaker.sizes.count(), 0)
        self.sneaker.sizes.add(self.size)
        self.assertEqual(self.sneaker.sizes.count(), 1)
        self.assertEqual(self.sneaker.sizes.first(), self.size)

    def test_brand_creation(self):
        brand = Brand.objects.create(
            name='Adidas', 
            description='Adidas brand'
            )
        self.assertEqual(Brand.objects.count(), 2)
        self.assertEqual(brand.name, 'Adidas')
        self.assertEqual(brand.description, 'Adidas brand')

    def test_size_creation(self):
        size = Size.objects.create(
            size_us=9.0, 
            size_ru=42, 
            size_eu=43, 
            size_uk=8.0, 
            size_cm=26
            )
        self.assertEqual(Size.objects.count(), 2)
        self.assertEqual(size.size_us, 9.0)
        self.assertEqual(size.size_ru, 42)
        self.assertEqual(size.size_eu, 43)
        self.assertEqual(size.size_uk, 8.0)
        self.assertEqual(size.size_cm, 26)

    def test_review_creation(self):
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(self.review.sneaker.title, 'Мужские Nike Air Max 90')
        self.assertEqual(self.review.author.username, 'review_user')
        self.assertEqual(self.review.review, 'Review. five stars')

    # Views test
    def test_sneaker_list_view(self):
        response = self.client.get(reverse('sneaker_list'))
        no_response = self.client.get('/no_sneaker')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'sneakers/sneaker_list.html')
        self.assertContains(response, 15000)
        self.assertContains(response, 'Мужские Nike Air Max 90')

    def test_sneaker_detail_view(self):
        response = self.client.get(self.url)
        no_response = self.client.get('/sneakers/nike-23232323232232sdasd')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'sneakers/sneaker_detail.html')
        self.assertContains(response, 15000)
        self.assertContains(response, 'Мужские Nike Air Max 90')
        self.assertContains(response, 'color: white')
        self.assertContains(response, '2 июня 2023')
