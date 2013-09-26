from django import template

register = template.Library()

@register.filter(name="article_shorten")
def article_shorten(bodytext,length):
    if len(bodytext) > length:
        text = "%s ..." % (bodytext[:length])
    else:
        text = bodytext
    return text