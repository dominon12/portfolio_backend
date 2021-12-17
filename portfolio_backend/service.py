


def build_absolute_uri(request, relative_url):
    uri = request.build_absolute_uri(relative_url)
    # return uri.replace('http', 'https')
    return uri