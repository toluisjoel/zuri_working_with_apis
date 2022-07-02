from django.db import models
from . import utils
from django.contrib.auth import get_user_model

# Create your models here.


class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.identifier:
            # Generate a random ID
            random_id = utils.generate_random_id()

            while Link.objects.filter(identifier=random_id).exists():
                random_id = utils.generate_random_id()

            self.identifier = random_id

        # Complete the save operation
        super().save(*args, **kwargs)
