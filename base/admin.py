from django.contrib import admin
from .models import Alternatif, Kriteria, BobotKriteria, BobotNormalKriteria, Penilaian

# Register your models here.
admin.site.register(Alternatif)
admin.site.register(Kriteria)
admin.site.register(BobotKriteria)
admin.site.register(BobotNormalKriteria)
admin.site.register(Penilaian)