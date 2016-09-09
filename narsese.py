# Simple conversions
def compound(seq, op = '*'):
    seq = ', '.join(seq)
    return '({}, {})'.format(op, seq)