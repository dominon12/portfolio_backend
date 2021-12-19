from django.db.models import Q



def filter_projects(qs, getParams):
    filterBy = getParams.get("filterBy")
    if filterBy:
        qs = qs.filter(Q(type__icontains=filterBy) | Q(technologies__name__in=[filterBy]))


    sortBy = getParams.get("sortBy")
    if sortBy:
        qs = qs.order_by(sortBy)

    qs.distinct()

    return qs
