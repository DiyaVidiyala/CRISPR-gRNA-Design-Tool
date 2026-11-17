def find_pam_sites(seq):
pam_sites = []

    for i in range(len(seq) - 2):
        pam = seq[i:i+3]

        if pam[1:] == "GG":
            pam_sites.append((i, pam))

    return pam_sites


def generate_candidates(seq, pam_sites):
candidates = []

    for position, pam in pam_sites:
        start = position - 20

        if start >= 0:
            guide = seq[start:position]

            if len(guide) == 20:
                candidates.append((guide, position, pam))

    return candidates
