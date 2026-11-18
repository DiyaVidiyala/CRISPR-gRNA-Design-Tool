
import streamlit as st
import pandas as pd

from sequence_processing import clean_sequence, validate_sequence
from pam_identification import find_pam_sites, generate_candidates
from candidate_ranking import rank_candidates
from grna_scoring import gc_content

st.title("CRISPR gRNA Design Tool")

st.write("This tool identifies and ranks potential gRNA candidates from a DNA sequence.")

dna = st.text_area("Enter DNA sequence")

if st.button("Analyze Sequence"):

    sequence = clean_sequence(dna)

    if len(sequence) == 0:
        st.warning("Please enter a DNA sequence.")

    elif len(validate_sequence(sequence)) != 0:
        st.error("Invalid DNA sequence. Enter only A, T, G and C.")

    else:
        st.success("Valid DNA sequence")

        pam_sites = find_pam_sites(sequence)
        candidates = generate_candidates(sequence, pam_sites)
        ranked = rank_candidates(candidates)

        st.write("Sequence length:", len(sequence))
        st.write("PAM sites found:", len(pam_sites))
        st.write("gRNA candidates generated:", len(candidates))

        if len(ranked) == 0:
            st.warning("No suitable gRNA candidates found.")

        else:
            results = []

            for i in range(len(ranked)):
                candidate = ranked[i]

                results.append({
                    "Rank": i + 1,
                    "gRNA": candidate["sequence"],
                    "PAM": candidate["pam"],
                    "PAM Position": candidate["pam_position"],
                    "GC Content": gc_content(candidate["sequence"]),
                    "Score": candidate["score"]
                })

            df = pd.DataFrame(results)

            st.subheader("Ranked gRNA Candidates")
            st.dataframe(df)

            st.subheader("Candidate Scores")
            st.bar_chart(df.set_index("Rank")["Score"])

st.caption("Scores are based on a simplified scoring method.")
