# End-to-End fMRI Quality Control & Task Analysis Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/JOYJIT-06/fmri-analysis-qc-pipeline/issues)

An automated, modular, production-ready quality control and analysis pipeline for 4D functional Magnetic Resonance Imaging (fMRI) data. This repository features robust calculations of standard motion-realignment artifacts, spatio-temporal noise reduction filters, General Linear Model (GLM) task activation mappings, seed-to-voxel Pearson connectivity metrics, and multivariate brain state decoding using Machine Learning.

---

## 1. Key Project Highlights & Features
- **Production Code Architecture**: Implements clean, modular Python packages (`src/`) separated from configuration variables (`configs/`).
- **Rigorous Motion & Noise Analysis (Part 2)**: Computes Framewise Displacement (FD, Power 2012) and root-mean-square temporal variance changes (DVARS).
- **Signal Conditioning (Part 3)**: Uses 3D Gaussian spatial smoothing kernels and voxel-wise temporal high-pass filtering (Butterworth) to remove physiological drifts.
- **First-Level Task Mapping (Part 4)**: Maps neural activations using Ordinary Least Squares (OLS) General Linear Models.
- **Seed-Based DMN Connectivity (Part 5)**: Computes Pearson cross-correlation matrices across spatial coordinates representing key nodes in the Default Mode Network (DMN).
- **Multivariate Decoding (Part 6)**: Trains a linear Support Vector Machine (SVM) classifier inside a 5-fold cross-validation scheme to decode task-active vs rest neurological states.
- **Interactive Report Delivery (Part 7)**: Automatically generates an elegant, standalone, single-file HTML executive diagnostic dashboard summarizing quantitative metadata and visualizations.


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



## 3. Installation Guide

### Step 1: Clone the Repository
Clone this project repository on your local machine using standard terminal commands:
```bash
git clone https://github.com/JOYJIT-06/fmri-analysis-qc-pipeline.git
cd fmri-analysis-qc-pipeline
```

### Step 2: Set Up Virtual Environment
It is highly recommended to isolate your dependencies using a Python virtual environment:
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Required Dependencies
Install the required third-party python libraries utilizing the compiled `requirements.txt` manifest:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. How to Execute the Project Locally

### Running the Automated Unit Tests
Verify the library modules perform successfully inside your local environment:
```bash
python -m unittest discover -s tests
```

### Executing the Entire fMRI Pipeline
You can run the pipeline directly inside your Jupyter notebook environment, or run the pipeline orchestrator via command-line shell script wrappers. 

Upon a successful run, the pipeline will:
1. Construct the workspace environment files.
2. Generate a simulated 4D task-rest fMRI NIfTI scan dataset.
3. Preprocess and calculate motion realignment parameters (FD, DVARS, tSNR).
4. Run statistical General Linear Models and spherical connectivity.
5. Save evaluation plots under `figures/`.
6. Compile and output `results/reports/qc_and_analysis_report.html`.

---

## 5. Licensing & Research Disclaimer
This software is distributed under the open-source **MIT License**.

**Academic Disclaimer**: This software pipeline is developed for academic research, technical demonstration, and portfolio verification. It is not clinically validated or certified for actual medical diagnostics, patient care, or hospital environments.
