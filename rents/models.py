from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Rent(models.Model):

    AUTHORS = (
        ('JONI', 'joni'),
        ('JERMAN', 'jerman'),
        ('SUBMIT', 'submit'),
        ('KAZEHAYA', 'kazehaya'),
    )

    TITLES = (
        ('BUKU_JONI', 'bukuJoni'),
        ('BUKU_JERMAN', 'bukuJerman'),
        ('BUKU_SUBMIT', 'bukuSubmit'),
        ('BUKU_KAZEHAYA', 'bukuKazehaya'),
    )

    PHOTOS = (
        ('BUKU_JONI.png', 'bukuJoni.png'),
        ('BUKU_JERMAN.png', 'bukuJerman.png'),
        ('BUKU_SUBMIT.png', 'bukuSubmit.png'),
        ('BUKU_KAZEHAYA.png', 'bukuKazehaya.png'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=20, choices=TITLES, default=TITLES[0][0])
    photo = models.CharField(
        max_length=20, choices=PHOTOS, default=PHOTOS[0][0])
    author = models.CharField(
        max_length=20, choices=AUTHORS, default=AUTHORS[0][0])
    borrowed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Rent book {self.title} by {self.customer.username}>"
