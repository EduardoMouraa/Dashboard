# Arquivo de filtros

def datetimeformat(value, format='%Y/%m/%d'):
    return value.strftime(format)


def datetimeformatMessage(value, format='%Y/%m/%d %H:%M'):
    data = value.strftime(format).split()
    return "{} às {}".format(data[0], data[1])


def formatMessage(value):
    data = value

    if len(value) > 40:
        data = '{}...'.format(value[:40])

    return data

def formatSizeBoxMessage(value):
    if len(value) > 40:
        return 2
    return 1