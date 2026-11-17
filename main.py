from sequence_processing import clean_sequence, validate_sequence
from pam_identification import find_pam_sites, generate_candidates
from candidate_ranking import rank_candidates


dna_sequence = (
    "ATGCGTACGTTACCGGATCGATCGGCTAGCTAGGCTAACCGGTAC"
    "GATCGGATCCGATCGTACGATCGGATCGATCGTACCGG"
)

sequence = clean_sequence(dna_sequence)

print("CRISPR gRNA Design Tool - Update 2")
print("-----------------------------------")
print("Sequence length:", len(sequence))
print()

invalid_bases = validate_sequence(sequence)

if len(invalid_bases) == 0:
    print("Sequence validation: Valid")
else:
    print("Sequence validation: Invalid")
    print("Invalid bases:", invalid_bases)

print()

pam_sites = find_pam_sites(sequence)

print("PAM sites found:", len(pam_sites))
print()

candidates = generate_candidates(sequence, pam_sites)

print("gRNA candidates generated:", len(candidates))
print()

ranked_candidates = rank_candidates(candidates)

print("Ranked gRNA candidates")
print("----------------------")

for i in range(len(ranked_candidates)):
    candidate = ranked_candidates[i]

    print("Rank:", i + 1)
    print("gRNA:", candidate["sequence"])
    print("PAM:", candidate["pam"])
    print("PAM position:", candidate["pam_position"])
    print("Score:", candidate["score"])
    print()
