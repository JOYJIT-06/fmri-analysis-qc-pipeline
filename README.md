# fMRI Analysis & Quality Control Pipeline

An end-to-end Python pipeline designed for production-level functional Magnetic Resonance Imaging (fMRI) quality control, preprocessing, first-level General Linear Model (GLM) task activation analysis, region-of-interest (ROI) functional connectivity, and multivariate pattern analysis (MVPA) classification.

## Project Architecture
```text
└── fmri-analysis-qc-pipeline/
    └── configs/               # Central pipeline parameters (YAML)
    └── src/                   # Core modular Python library files
    └── tests/                 # Unit test coverage
    └── figures/               # Automatically generated diagnostic plots
    └── results/
        └── reports/           # Standalone dynamic HTML executive dashboard
        └── qc/                # Computed metrics (FD, DVARS, tSNR)
```

## Pipeline Functional Blocks
1. **Automated Quality Control (Part 2)**: Computes Frame Displacement (FD), DVARS, and Temporal SNR maps.
2. **Preprocessing (Part 3)**: Performs 3D Gaussian spatial smoothing and high-pass Butterworth temporal filtering.
3. **General Linear Model (Part 4)**: Maps neural activation contrasts matching experimental paradigms.
4. **Functional Connectivity (Part 5)**: Computes spatial cross-correlations acrossDefault Mode Network coordinate seeds.
5. **Machine Learning / MVPA (Part 6)**: Decodes neurological task states with Support Vector Machines.

## Usage
To install dependencies and run tests locally:
```bash
pip install -r requirements.txt
python -m unittest discover -s tests
```