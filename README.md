
# CRISPR gRNA Design Tool

### A Python-Based Approach to Computational Guide RNA Design

## Project Overview

The CRISPR gRNA Design Tool is a computational biology project developed using Python to identify, evaluate, and rank potential guide RNA (gRNA) candidates from a given DNA sequence.

The project integrates biological principles of CRISPR-Cas9 with computational sequence analysis to automate the preliminary identification of potential guide RNA candidates.

## Objectives

- Process and validate DNA sequences.
- Identify Protospacer Adjacent Motif (PAM) sites.
- Generate 20-nucleotide guide candidates.
- Calculate GC content and candidate scores.
- Rank candidates based on predefined scoring criteria.

## Biological Background

CRISPR-Cas9 is a genome-editing technology that uses guide RNA to direct the Cas9 enzyme towards a specific DNA target.

The commonly used SpCas9 enzyme recognizes an NGG PAM motif, where N represents any nucleotide. This project identifies NGG motifs and extracts the corresponding 20-nucleotide sequences preceding them.

## Key Features

- DNA sequence cleaning and validation
- Automated NGG PAM identification
- Guide RNA candidate generation
- GC content calculation
- Rule-based candidate scoring
- Descending score-based ranking
- Modular Python implementation


## Project Workflow

```text
Input DNA Sequence
        |
        v
Sequence Cleaning
        |
        v
Sequence Validation
        |
        v
PAM Site Identification
        |
        v
gRNA Candidate Generation
        |
        v
GC Content and Scoring
        |
        v
Candidate Ranking
        |
        v
Display Results
```


## Repository Structure

| File | Description |
|---|---|
| main.py | Executes the complete pipeline |
| sequence_processing.py | DNA cleaning and validation |
| pam_identification.py | PAM detection and candidate generation |
| grna_scoring.py | GC content calculation and scoring |
| candidate_ranking.py | Candidate sorting and ranking |

## Scoring Methodology

Each candidate is evaluated using a rule-based scoring system with a maximum score of 100.

| Parameter | Condition | Score |
|---|---|---:|
| Guide length | Exactly 20 nucleotides | 40 |
| GC content | 40–60% | 40 |
| GC content | 30–70%, outside the preferred range | 20 |
| GC content | Outside 30–70% | 0 |
| Sequence validity | Contains only A, T, G and C | 20 |

Candidates are sorted in descending order of their total scores.

The scoring system is heuristic and does not represent experimentally validated editing efficiency.

## Technologies Used

- Python 3
- Google Colab
- GitHub
- Computational sequence analysis
- String manipulation and sorting algorithms

## How to Run

1. Download or clone this repository.
2. Ensure Python 3 is installed.
3. Open the project directory.
4. Execute the following command:

```bash
python main.py
```

No external Python libraries are required for the current implementation.

## Sample Results

The current implementation was successfully tested using the DNA sequence included in main.py.

| Parameter | Result |
|---|---|
| Input sequence length | 83 nucleotides |
| Sequence validation | Valid |
| PAM sites identified | 7 |
| gRNA candidates generated | 6 |
| Maximum candidate score | 100 |

Six candidates were generated from seven PAM sites because one PAM site lacked sufficient upstream nucleotides.

## Current Limitations

- Uses a predefined input DNA sequence.
- Searches only the supplied DNA strand.
- Uses a simplified rule-based scoring model.
- Candidates with equal scores are not further differentiated.
- Off-target effects are not currently evaluated.
- Experimental validation has not been performed.

## Future Scope

- Interactive web application
- Custom DNA sequence input
- Reverse-complement strand analysis
- Off-target analysis
- Advanced scoring algorithms
- Interactive results visualization
- Exportable candidate reports

## Team Members and Responsibilities

### Diya Vidiyala

**Roll Number:** SE25UCAB028

- DNA sequence processing
- Sequence validation
- PAM site identification
- gRNA candidate generation

### Manaswini Yerramilli

**Roll Number:** SE25UCAB018

- gRNA scoring
- Candidate ranking
- Off-target analysis (planned)
- Results visualization (planned)

Both team members will collaborate on web application development and deployment.

## Project Status

- [x] DNA sequence processing
- [x] PAM site identification
- [x] gRNA candidate generation
- [x] Candidate scoring
- [x] Candidate ranking
- [x] Initial pipeline execution and testing
- [ ] Web application development
- [ ] Off-target analysis
- [ ] Results visualization
- [ ] Web application deployment

## Academic Disclaimer

This project is developed for academic and educational purposes. The generated candidates and scores require further computational and experimental validation before biological application.
