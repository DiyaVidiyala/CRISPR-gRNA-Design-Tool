def clean_sequence(seq):
seq = seq.strip().upper()
    seq = seq.replace(" ", "")
    return seq


def validate_sequence(seq):
invalid_bases = []

    for i in range(len(seq)):
        if seq[i] not in "ATGC":
            invalid_bases.append((i, seq[i]))

    return invalid_bases
