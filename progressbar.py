import sys


def progress(count, total, status=''):
    bar_len = 80
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '#' * filled_len + ' ' * (bar_len - filled_len)

    sys.stdout.write('%s |%s| %s%s\r' % (status, bar, percents, '%'))
    sys.stdout.flush()
