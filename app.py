
import streamlit as st
import pandas as pd

from sequence_processing import clean_sequence, validate_sequence
from pam_identification import find_pam_sites, generate_candidates
from candidate_ranking import rank_candidates
from grna_scoring import gc_content
from off_target_analysis import off_target_information, similarity_demo

st.set_page_config(
    page_title="CRISPR gRNA Design Tool",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #100e17;
    color: #e5e1ed;
}

[data-testid="stHeader"] {
    background-color: #100e17;
}

[data-testid="stSidebar"] {
    background-color: #191522;
    border-right: 1px solid #382b4d;
}

h1 {
    color: #c4a0ff !important;
    font-weight: 700;
    letter-spacing: -1px;
}

h2, h3 {
    color: #d8c5f5 !important;
}

p, label {
    color: #d0c8dc !important;
}

[data-testid="stMetric"] {
    background-color: #1c1727;
    border: 1px solid #403052;
    border-top: 3px solid #a78bfa;
    padding: 22px;
    border-radius: 8px;
}

[data-testid="stMetricValue"] {
    color: #c4a0ff !important;
    font-family: monospace;
}

.stButton > button {
    background-color: #7952b3;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 10px 25px;
    font-weight: 600;
}

.stButton > button p {
    color: white !important;
}

.stButton > button:hover {
    background-color: #9365d4;
    color: white;
}

.stTextArea textarea {
    background-color: #191522;
    color: #e0b3ff;
    font-family: monospace;
    font-size: 15px;
    border: 1px solid #49365e;
}

.stTextArea textarea::placeholder {
    color: #9488a7;
}

[data-testid="stDataFrame"] {
    border: 1px solid #403052;
    border-radius: 8px;
}

[data-testid="stExpander"] {
    background-color: #191522;
    border: 1px solid #403052;
    border-radius: 8px;
}

hr {
    border-color: #403052;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    "<p style='color:#a78bfa; font-family:monospace; letter-spacing:2px; font-size:12px;'>COMPUTATIONAL BIOLOGY / SEQUENCE ANALYSIS</p>",
    unsafe_allow_html=True
)

st.title("CRISPR gRNA Design Tool")

st.write("DNA sequence analysis, candidate ranking and visualization.")

st.divider()

st.sidebar.title("CRISPR / 01")
st.sidebar.caption("Python Course Project")

st.sidebar.divider()

st.sidebar.header("Design Parameters")

st.sidebar.write("**Cas Protein:** SpCas9")
st.sidebar.write("**PAM Motif:** NGG")
st.sidebar.write("**Guide Length:** 20 nucleotides")
st.sidebar.write("**Preferred GC Content:** 40-60%")

st.sidebar.divider()

st.sidebar.header("Developed By")
st.sidebar.write("Diya Vidiyala")
st.sidebar.write("Manaswini Yerramilli")

st.sidebar.divider()

st.sidebar.caption("Python • Pandas • Streamlit")

st.subheader("01 / Sequence Input")

dna = st.text_area(
    "Enter DNA sequence",
    height=150,
    placeholder="Enter DNA sequence containing A, T, G and C..."
)

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

        st.divider()

        st.subheader("02 / Sequence Analysis")

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
                    "GC Content": round(
                        gc_content(candidate["sequence"]), 2
                    ),
                    "Score": candidate["score"]
                })

            df = pd.DataFrame(results)

            st.divider()

            st.subheader("03 / Ranked gRNA Candidates")

            st.dataframe(df, hide_index=True)

            st.caption("PAM positions start from index 0.")

            st.divider()

            st.subheader("04 / Candidate Visualization")

            chart1, chart2 = st.columns(2)

            with chart1:
                st.markdown("#### Candidate Scores")
                st.bar_chart(
                    df.set_index("Rank")["Score"],
                    color="#a78bfa"
                )

            with chart2:
                st.markdown("#### GC Content Comparison")
                st.bar_chart(
                    df.set_index("Rank")["GC Content"],
                    color="#c084fc"
                )

            st.subheader("Scoring Criteria")

            score1, score2, score3 = st.columns(3)

            score1.metric("Guide Length", "40 pts")
            score2.metric("Maximum GC Score", "40 pts")
            score3.metric("Valid DNA Bases", "20 pts")

            st.caption("Maximum possible candidate score: 100")

st.divider()

st.subheader("05 / Off-Target Effects")

with st.expander("Understanding Off-Target Effects"):

    information = off_target_information()

    for heading in information:
        st.markdown(
            "**" + heading + ":** " + information[heading]
        )

    st.subheader("Sequence Similarity Demonstration")

    st.code("ABCDEF", language=None)

    demo = pd.DataFrame(similarity_demo())

    st.dataframe(demo, hide_index=True)

    st.bar_chart(
        demo.set_index("Example")["Differences"],
        color="#db8ab8"
    )

    st.caption(
        "This fictional example demonstrates sequence mismatches, "
        "not biological off-target prediction."
    )

st.divider()

st.caption(
    "This tool is intended for educational purposes. "
    "Candidate scores do not guarantee editing efficiency or specificity."
)

st.markdown(
    "<p style='text-align:center; font-family:monospace; "
    "font-size:11px; letter-spacing:2px;'>"
    "CRISPR / COMPUTATIONAL BIOLOGY / 2026"
    "</p>",
    unsafe_allow_html=True
)
