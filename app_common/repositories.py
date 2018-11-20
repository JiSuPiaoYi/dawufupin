from app_common import models as common_models
from operator import itemgetter

def get_annunciate():
    annunciates = list(common_models.Annunciate.objects.all().values())
    governmentdecrees = list(common_models.GovernmentDecree.objects.all().values())
    for key, value in enumerate(annunciates):
        annunciates[key]['type'] = 1
        annunciates[key]['short_content'] = value['content'][:50]
    for key, value in enumerate(governmentdecrees):
        governmentdecrees[key]['type'] = 2
        governmentdecrees[key]['short_content'] = value['content'][:50]

    data = annunciates + governmentdecrees
    data.sort(key=itemgetter('create_time'), reverse=True)

    return data