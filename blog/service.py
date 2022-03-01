from portfolio_backend.service import get_client_ip
from users import models as users_models


def add_article_visitor(request, article):
    client_ip = get_client_ip(request)
    users_qs = users_models.AnonymousUser.objects.filter(ipAddress=client_ip)
    viewer = None
    if users_qs.exists():
        viewer = users_qs[0]
    else:
        viewer = users_models.AnonymousUser.objects.create(ipAddress=client_ip)
    article.viewers.add(viewer)
    article.save()
    return article