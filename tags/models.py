from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    recipes = models.ForeignKey(
        "recipes.Recipe", related_name="tags", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


# Create your models here.
