def clean_sequence(sequence):
    sequence = sequence.upper()
    sequence = sequence.replace(" ", "").replace("\n", "")
    return sequence

def validate_sequence(sequence):
    invalid_bases = []

    for i, base in enumerate(sequence):
        if base not in "ATGC":
            invalid_bases.append((i, base))

    return invalid_bases
