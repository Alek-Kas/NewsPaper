from django import template

register = template.Library()

BAD_WORDS = (
    'редиск',
    'хрен'
)


@register.filter()
def censor(value):
    text = value.replace('.', ' ')
    text = text.replace(',', ' ')
    text = text.replace('-', ' ')
    text = text.split()
    # print(text)
    text_out = ''
    for i in text:
        j = i.lower()
        # print(i, j)
        for k in BAD_WORDS:
            if j.find(k) != -1:
                first = i[0]
                last = (len(i) - 1) * '*'
                # print(first, last)
                i = first + last
                # print(i)
        '''
        if j in BAD_WORDS:
            print(i[0])
            first = i[0]
            last = len(i) * '*'
            print(first, last)
            i = first + last
            print(i)
        '''
        text_out = text_out + ' ' + i
        # print(text_out)
    return f'{text_out}'

