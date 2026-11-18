
from grna_scoring import score_grna


def rank_candidates(candidates):
    results = []

    for candidate in candidates:
        guide = candidate[0]
        pam_position = candidate[1]
        pam = candidate[2]

        score = score_grna(guide)

        result = {
            "sequence": guide,
            "pam_position": pam_position,
            "pam": pam,
            "score": score
        }

        results.append(result)

    results.sort(key=lambda x: x["score"], reverse=True)

    return results
