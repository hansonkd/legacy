from django.db import models


class FidoModel(models.Model):

    class Meta:
        abstract = True

    @property
    def f(self):
        return self.functions(self)
    

class ShortTextField(models.TextField):
    def formfield(self, **kwargs):
        return super(models.CharField, self).formfield(**kwargs)

def choices(it):
    return [(i, i) for i in it]