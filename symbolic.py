def symbolic_notation(mask):
    """
    to convert the Mask into symbolic notation
    :param mask:
    :return:
    """
    r = 4
    w = 2
    x = 1
    end_rwx = ''
    for p in str(mask):
        rwx = ''
        p = int(p)
        if r <= p:
            p -= r
            rwx += 'r'

            if w <= p:
                p -= w
                rwx += 'w'
                if x <= p:
                    p -= x
                    rwx += 'x'
                else:
                    rwx += '-'

            elif x <= p:
                p -= x
                rwx += '-x'

            else:
                rwx += '--'

        elif w < p:
            p -= w
            rwx += '-w'
            if x <= p:
                p -= x
                rwx += 'x'
            else:
                rwx += '-'

        elif x <= p:
            p -= x
            rwx += '--x'

        end_rwx += rwx

    return end_rwx