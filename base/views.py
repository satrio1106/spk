from django.shortcuts import render
from django.db.models import Sum, Max, Min

import numpy as np
from functools import reduce
from copy import deepcopy
from .models import Alternatif, Kriteria, BobotKriteria, Penilaian


# Create your views here.
def home(request):

    context = {

    }
    return render(request, 'base/index.html', context)


def alternatif(request):
    alternatifs = Alternatif.objects.all()
    context = {
        'alternatifs': alternatifs,
    }

    return render(request, 'base/alternatif.html', context)


def kriteria(request):
    kriteria = Kriteria.objects.all()
    sum_bobot = BobotKriteria.objects.aggregate(total_sum=Sum('bobot'))
    bobot_max = sum_bobot['total_sum']

    context = {
        'kriteria': kriteria,
        'bobot_max': bobot_max,
    }

    return render(request, 'base/kriteria.html', context)

def sub_kriteria(request):
    context = {

    }

    return render(request, 'base/sub-kriteria.html', context)

def metode_saw(request):

    alternatif = Alternatif.objects.all()
    penilaian = Penilaian.objects.all()
    bobotK = BobotKriteria.objects.all()

    kriteria = Kriteria.objects.all()
    sum_bobot = BobotKriteria.objects.aggregate(total_sum=Sum('bobot'))
    bobot_max = sum_bobot['total_sum']

    kf_max = Penilaian.objects.aggregate(max_value=Max('kelengkapan_fitur'))['max_value'] if kriteria[0].status == 'benefit' else Penilaian.objects.aggregate(min_value=Min('kelengkapan_fitur'))['min_value']
    kp_max = Penilaian.objects.aggregate(max_value=Max('kemudahan_penggunaan'))['max_value'] if kriteria[1].status == 'benefit' else Penilaian.objects.aggregate(min_value=Min('kemudahan_penggunaan'))['min_value']
    k_max = Penilaian.objects.aggregate(max_value=Max('keamanan'))['max_value'] if kriteria[2].status == 'benefit' else Penilaian.objects.aggregate(min_value=Min('keamanan'))['min_value']
    b_max = Penilaian.objects.aggregate(max_value=Max('biaya'))['max_value'] if kriteria[3].status == 'benefit' else Penilaian.objects.aggregate(min_value=Min('biaya'))['min_value']

    mats_saw = []   
    mats_bbt = []

    for i in penilaian:
        mats_saw.append([i.kelengkapan_fitur / kf_max, i.kemudahan_penggunaan / kp_max, i.keamanan / k_max, b_max / i.biaya])

    for i in bobotK:
        mats_bbt.append([i.bobot / bobot_max])


    normalisasi = np.array(mats_saw)
    bobot_normal = np.array(mats_bbt)

    normal_name = list(list(i) for i in normalisasi)

    alternatif_name = [i.name for i in alternatif]
    for i, j in enumerate(normal_name):
        j.insert(0, alternatif_name[i])


    preferensi = np.dot(normalisasi, bobot_normal)

    preferensi = [list(i) for i in preferensi]

    for i, j in enumerate(preferensi):
        j.insert(0, alternatif_name[i])

    preferensi = sorted(preferensi, reverse=True, key=lambda x:x[1])

    context = {
        'penilaian': penilaian,
        'kriteria': kriteria,
        'bobot_max': bobot_max,

        'kf_max': kf_max,
        'kp_max': kp_max,
        'k_max': k_max,
        'b_max': b_max,

        'normalisasi': normal_name,
        'bobot_normal': bobot_normal,
        'preferensi': preferensi,
    }

    return render(request, 'base/saw.html', context)

def metode_wp(request):

    alternatif = Alternatif.objects.all()
    penilaian = Penilaian.objects.all()
    bobotK = BobotKriteria.objects.all()

    kriteria = Kriteria.objects.all()
    sum_bobot = BobotKriteria.objects.aggregate(total_sum=Sum('bobot'))
    bobot_max = sum_bobot['total_sum']

    kf_max = Penilaian.objects.aggregate(max_value=Max('kelengkapan_fitur'))['max_value'] if kriteria[0].status == 'benefit' else Penilaian.objects.aggregate(min_value=Min('kelengkapan_fitur'))['min_value']
    kp_max = Penilaian.objects.aggregate(max_value=Max('kemudahan_penggunaan'))['max_value'] if kriteria[1].status == 'benefit' else Penilaian.objects.aggregate(min_value=Min('kemudahan_penggunaan'))['min_value']
    k_max = Penilaian.objects.aggregate(max_value=Max('keamanan'))['max_value'] if kriteria[2].status == 'benefit' else Penilaian.objects.aggregate(min_value=Min('keamanan'))['min_value']
    b_max = Penilaian.objects.aggregate(max_value=Max('biaya'))['max_value'] if kriteria[3].status == 'benefit' else Penilaian.objects.aggregate(min_value=Min('biaya'))['min_value']

    mats_wp = []   
    mats_bbt = []

    for i in bobotK:
        mats_bbt.append(i.bobot / bobot_max)

    for i in penilaian:
        mats_wp.append([pow(i.kelengkapan_fitur, mats_bbt[0]), pow(i.kemudahan_penggunaan, mats_bbt[1]), pow(i.keamanan, mats_bbt[2]), pow(b_max, (- mats_bbt[3]))])

    vektor_s = deepcopy(mats_wp)

    alternatif_name = [i.name for i in alternatif]
    for i, j in enumerate(vektor_s):
        j.append(reduce(lambda x, y: x*y, mats_wp[i]))
        j.insert(0, alternatif_name[i])

    
    vektor_v = list(map(lambda x: sum(x), mats_wp))
    vektor_v = list(map(lambda x,y:[x,y], alternatif_name, vektor_v))

    vektor_v = sorted(vektor_v, reverse=True, key=lambda x:x[1])

    context = {
        'penilaian': penilaian,
        'kriteria': kriteria,
        'bobot_max': bobot_max,

        'kf_max': kf_max,
        'kp_max': kp_max,
        'k_max': k_max,
        'b_max': b_max,

        'vektor_s': vektor_s,
        'vektor_v': vektor_v,
    }

    return render(request, 'base/wp.html', context)


def metode_ahp(request):
    context = {

    }

    return render(request, 'base/ahp.html', context)