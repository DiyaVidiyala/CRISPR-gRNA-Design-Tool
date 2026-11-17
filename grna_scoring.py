def gc_content(seq):
seq = seq.upper()

    gc_count = 0

    for base in seq:
        if base == "G" or base == "C":
            gc_count += 1

    return (gc_count / len(seq)) * 100


def score_grna(seq):
seq = seq.upper()
    score = 0

    if len(seq) == 20:
        score += 40

    gc = gc_content(seq)

    if 40 <= gc <= 60:
        score += 40
    elif 30 <= gc <= 70:
        score += 20

    valid = True

    for base in seq:
        if base not in "ATGC":
            valid = False

    if valid:
        score += 20

    return score
