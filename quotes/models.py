from django.db import models

class Individual(models.Model):
    name = models.CharField(max_length=200,unique=True, verbose_name="Author ")

    def __str__(self) -> str:
        return str(self.name)


class Quote(models.Model):
    quote = models.TextField(unique=True)
    individual = models.ForeignKey(Individual,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.quote)