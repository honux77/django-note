from django.db import models

class Note(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}: {}".format(self.name, self.text)