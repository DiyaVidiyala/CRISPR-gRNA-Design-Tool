
import streamlit as st
import pandas as pd

from sequence_processing import clean_sequence, validate_sequence
from pam_identification import find_pam_sites, generate_candidates
from candidate_ranking import rank_candidates
from grna_scoring import gc_content

st.set_page_config(page_title="CRISPR gRNA Design Tool", page_icon="🧬")

st.title("🧬 CRISPR gRNA Design Tool")

st.sidebar.title("About the Tool")
st.sidebar.write("Python Course Project")
st.sidebar.write("Cas Protein: SpCas9")
st.sidebar.write("PAM Motif: NGG")
st.sidebar.write("Guide Length: 20 nucleotides")
st.sidebar.write("Preferred GC Content: 40-60%")

st.sidebar.header("Developed By")
st.sidebar.write("Diya Vidiyala")
st.sidebar.write("Manaswini Yerramilli")

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

        st.subheader("Sequence Analysis")

        col1, col2, col3 = st.columns(3)

        col1.metric("Sequence Length", len(sequence))
        col2.metric("PAM Sites", len(pam_sites))
        col3.metric("gRNA Candidates", len(candidates))

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
                    "GC Content": round(gc_content(candidate["sequence"]), 2),
                    "Score": candidate["score"]
                })

            df = pd.DataFrame(results)

            st.subheader("Ranked gRNA Candidates")
            st.dataframe(df, hide_index=True)
            st.caption("PAM positions start from index 0.")

            st.subheader("Candidate Scores")
            st.bar_chart(df.set_index("Rank")["Score"])

            st.subheader("GC Content Comparison")
            st.bar_chart(df.set_index("Rank")["GC Content"])

            st.subheader("Scoring Criteria")
            st.write("Guide length: 40 points")
            st.write("GC content: Up to 40 points")
            st.write("Valid DNA bases: 20 points")

st.caption("Scores are based on a simplified scoring method and do not guarantee editing efficiency. Off-target analysis is not currently included.")

