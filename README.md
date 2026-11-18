# 🧬 CRISPR gRNA Design Tool

A Python-based bioinformatics application developed to identify, evaluate, rank and visualize potential guide RNA (gRNA) candidates from an input DNA sequence using basic SpCas9 design principles.

## Live Web Application

[Launch CRISPR gRNA Design Tool](https://crispr-grna-design-tool-bmstt6zyagme6ckou8hhcc.streamlit.app/)

## 1. Project Objective

The objective of this project is to develop a user-friendly computational tool that demonstrates the fundamental principles of CRISPR-Cas9 guide RNA design through Python programming and an interactive web interface.

## 2. Key Features

- DNA sequence cleaning and validation
- Identification of NGG PAM motifs
- Generation of potential 20-nucleotide gRNA candidates
- GC content calculation
- Rule-based candidate scoring
- Candidate ranking
- Interactive results table
- Score and GC content visualization
- Educational information on off-target effects
- Web interface developed using Streamlit

## 3. Project Workflow

```text
Input DNA Sequence
        |
Sequence Cleaning and Validation
        |
PAM Site Identification
        |
gRNA Candidate Generation
        |
GC Content Calculation
        |
Candidate Scoring
        |
Ranking of Candidates
        |
Results and Visualization
```

## 4. Project Structure

| File | Description |
|---|---|
| sequence_processing.py | Cleans and validates DNA sequences |
| pam_identification.py | Identifies PAM sites and generates candidates |
| grna_scoring.py | Calculates GC content and candidate scores |
| candidate_ranking.py | Ranks candidates based on their scores |
| off_target_analysis.py | Provides educational information on off-target effects |
| main.py | Executes the core computational workflow |
| app.py | Implements the interactive Streamlit interface |
| requirements.txt | Lists required Python libraries |
| README.md | Contains project documentation |

## 5. Scoring Methodology

Each candidate is evaluated using a rule-based scoring system with a maximum score of 100.

| Criterion | Condition | Points |
|---|---|---:|
| Guide length | 20 nucleotides | 40 |
| GC content | 40–60% | 40 |
| GC content | 30–70%, outside preferred range | 20 |
| Sequence validity | Valid DNA bases | 20 |

Candidates are arranged in descending order of their total scores.

These scores represent a simplified educational evaluation and are not experimentally validated predictions of CRISPR editing efficiency.

## 6. Results and Testing

The application was tested with different categories of input sequences.

| Test Case | Observed Result |
|---|---|
| Valid DNA sequence | Successfully processed |
| Invalid DNA sequence | Error message displayed |
| Empty input | Warning message displayed |
| Sequence without PAM motifs | No candidates reported |

### Sample Analysis

- Input sequence length: 83 nucleotides
- PAM sites identified: 7
- Potential gRNA candidates generated: 6
- Maximum candidate score: 100

The application displays ranked candidates along with their PAM motifs, positions, GC content and scores.

## 7. Off-Target Effects

Off-target effects occur when CRISPR-Cas9 interacts with unintended DNA regions.

The application includes an educational module explaining the causes, consequences and importance of off-target effects.

Genome-wide computational off-target prediction is not implemented in the current version.

## 8. Technologies Used

- Python
- Streamlit
- Pandas
- GitHub
- Streamlit Community Cloud

## 9. Running the Project Locally

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the command-line version:

```bash
python main.py
```

Launch the web application:

```bash
streamlit run app.py
```

## 10. Limitations

- The current implementation focuses on the SpCas9 NGG PAM motif.
- Candidate identification is limited to the supplied DNA strand.
- Candidate scoring is based on simplified rules.
- Genome-wide off-target prediction is not implemented.
- Candidate scores do not guarantee biological editing efficiency or specificity.

## 11. Future Scope

- Reverse-strand analysis
- Reference genome integration
- Computational off-target analysis
- Advanced scoring models
- Support for additional Cas proteins
- Further improvements to visualization and reporting

## 12. Team Members

| Name | Enrollment Number |
|---|---|
| Diya Vidiyala | SE25UCAB028 |
| Manaswini Yerramilli | SE25UCAB018 |

### Project Responsibilities

**Diya Vidiyala**

- DNA sequence processing
- Sequence validation
- PAM identification
- Candidate generation

**Manaswini Yerramilli**

- gRNA scoring
- Candidate ranking
- Results visualization
- Off-target concept documentation

**Joint Responsibilities**

- Module integration
- Web application development
- Testing and deployment
- Project documentation

---

*Developed as part of an undergraduate Python course project, demonstrating the integration of programming and computational biology.*
