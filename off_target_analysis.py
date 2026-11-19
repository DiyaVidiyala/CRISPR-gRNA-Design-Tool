

def off_target_information():
    information = {
        "Definition": "Off-target effects occur when Cas9 acts on unintended DNA regions.",
        "Cause": "Similarity between intended and unintended DNA targets.",
        "Impact": "Unintended changes in the DNA sequence.",
        "Requirement": "A reference genome is required for genome-wide off-target analysis.",
        "Status": "Educational similarity demonstration only. Biological off-target prediction is not implemented."
    }

    return information


def similarity_demo():
    original = "ABCDEF"
    examples = ["ABCDEF", "ABCXEF", "AXCXEF", "XXXXXX"]

    results = []

    for example in examples:
        matches = 0

        for i in range(len(original)):
            if original[i] == example[i]:
                matches += 1

        results.append({
            "Example": example,
            "Matches": matches,
            "Differences": len(original) - matches
        })

    return results
