# SNA-Project: Network Analysis of ASCAIDA and Astrophysics Collaboration Networks

## Overview
This repository contains tools and analyses for studying scientific collaboration networks in astrophysics, with a particular focus on the ASCAIDA (Astrophysics Scientific Collaboration and Institution Data Analysis) dataset. The project aims to uncover collaboration patterns, identify key research communities, and analyze the evolution of scientific partnerships in the field of astrophysics.

## Features
- Analysis of co-authorship networks from astrophysics publications
- Visualization of scientific collaboration patterns
- Identification of influential researchers and institutions
- Community detection in research networks
- Temporal analysis of collaboration evolution
- Network metrics calculation (centrality measures, clustering coefficients, etc.)
- Interactive network visualizations

## Prerequisites
- Python 3.8+
- Required Python packages:
  - networkx
  - pandas
  - numpy
  - matplotlib
  - plotly
  - scipy
  - scikit-learn
  - community (python-louvain)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/SNA-Project.git
cd SNA-Project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Data Sources
- ASCAIDA dataset: Collaboration networks from astrophysics publications
- ArXiv astrophysics paper metadata
- Additional astrophysics collaboration data from relevant journals and databases

## Analysis Capabilities
- **Network Construction**
  - Co-authorship network generation
  - Institution collaboration networks
  - Topic-based subnetworks

- **Network Metrics**
  - Author centrality measures
  - Institution influence analysis
  - Research community detection
  - Collaboration strength metrics
  - Geographic distribution of collaborations

- **Temporal Analysis**
  - Evolution of collaboration patterns
  - Growth of research communities
  - Changes in network structure over time


## Acknowledgments
- ASCAIDA dataset providers and contributors
- ArXiv for providing access to astrophysics paper metadata
- The astrophysics research community for their valuable input and feedback
- Network analysis tools and libraries used in this project