# Using User-Based Activity Logging and Analysis to Prioritise Software Maintenance

Master of Engineering in Computer and Electronic Engineering — Cornelius Scheepers

Supervised by Dr Jaco Prinsloo

## About

This dissertation develops a methodology for capturing user-based activity logs from web-based software systems and analysing them to prioritise software maintenance efforts. Software maintenance consumes 60–80% of total development resources, yet decisions about where to focus those efforts are often ad hoc. This work provides a data-driven approach by:

1. Designing and implementing a logging mechanism that captures user-generated events (clicks, form inputs, navigation) with attributes such as timestamp, user ID, activity type, subsystem, and metadata.
2. Normalising and analysing the captured logs to calculate a **Maintenance Priority Factor** for each subsystem based on usage frequency and user count.
3. Evaluating the approach across three real-world case studies (Projects A, B, and C).

## Repository Structure

```
├── Chapters/              LaTeX chapter sources
│   ├── Chapter1.tex       Introduction
│   ├── Chapter2.tex       Methodology
│   ├── Chapter3.tex       Implementation & Results
│   ├── Chapter4.tex       Evaluation
│   └── Chapter5.tex       Discussion (draft)
├── src/
│   ├── Ch3/
│   │   ├── data/uat_raw/  Raw CSV datasets (~320K rows)
│   │   └── log_analysis/  Jupyter notebook & analysis output
│   ├── includes/          Title pages & chapter figures
│   └── lib/               BibTeX bibliography
├── img/                   Figures and generated charts
├── docs/                  Research papers & supporting documents
├── Document.tex           Main LaTeX document
└── .github/workflows/     CI/CD for LaTeX compilation
```

## Building the Dissertation

### Prerequisites

- A LaTeX distribution (TeX Live or MiKTeX) with `latexmk`
- Python 3.8+ (for the analysis notebook)

### Compile

```bash
latexmk -pdf Document.tex
```

### Run the Analysis Notebook

```bash
cd src/Ch3/log_analysis
pip install -r requirements.txt
jupyter notebook uat_analysis.ipynb
```

## CI/CD

The GitHub Actions workflow automatically compiles the LaTeX document on every push and pull request. The compiled PDF is uploaded as a build artifact.

## License

See [LICENSE](LICENSE) for details.
