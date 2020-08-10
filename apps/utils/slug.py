from apps.utils.dict import dic, alphabet
from django.utils.text import slugify

from apps.posts import models


def _get_unique_slug(title):
    name = str(title)
    result = str()

    name_len = len(name)
    for i in range(0, name_len):
        if name[i] in alphabet:
            simb = dic[name[i]]
        else:
            simb = name[i]
        result = result + simb

    slug = slugify(result)
    unique_slug = slug
    num = 1
    while models.Post.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    return unique_slug
