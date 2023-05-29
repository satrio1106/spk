from django.db import models

# Create your models here.
class Alternatif(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Kriteria(models.Model):
    STATUS = (
        ('benefit', 'benefit'),
        ('cost', 'cost')
    )
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return self.name

class BobotKriteria(models.Model):
    kriteria = models.OneToOneField(Kriteria, on_delete=models.CASCADE)
    bobot = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.kriteria.name} - {self.bobot}'

class BobotNormalKriteria(models.Model):
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE)
    bobot = models.FloatField(default=0)

class Penilaian(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE)
    kelengkapan_fitur = models.IntegerField(default=0)
    kemudahan_penggunaan = models.IntegerField(default=0)
    keamanan = models.IntegerField(default=0)
    biaya = models.IntegerField(default=0)

    def __str__(self):
        return self.alternatif.name
