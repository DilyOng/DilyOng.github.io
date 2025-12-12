---
layout: page
title: unimpeded
description: A public nested sampling database for Bayesian cosmology
img: assets/img/unimpeded/flowchart.png
importance: 1
category: work
related_publications: true
---

`unimpeded` is a public Python library and data repository created to accelerate and democratize research in Bayesian cosmology. It addresses the significant computational expense of calculating Bayesian evidence by providing a massive, pre-computed database of nested sampling results for dozens of cosmological model and dataset combinations. This allows any researcher to perform sophisticated model comparison and tension analysis without requiring access to high-performance computing resources.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/unimpeded/flowchart.png" title="Unimpeded workflow" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Figure 1: The unimpeded workflow showing the automated pipeline for nested sampling analysis and archival.
</div>

## Key Features

- **Public Data Grid:** Provides open access to thousands of pre-computed nested sampling and MCMC chains for 8 cosmological models tested against 39 modern datasets.
- **Automated Archival & Reproducibility:** Seamlessly archives all analysis products on Zenodo, generating permanent, citable Digital Object Identifiers (DOIs) to ensure results are transparent and reproducible.
- **Built-in Tension Calculator:** Includes a tool for the rapid calculation of six distinct statistical metrics to quantify the agreement or "tension" between different experimental datasets.
- **User-Friendly Analysis:** Offers a high-level interface to easily download, analyze, and visualize cosmological data products like posterior distributions and corner plots.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/unimpeded/tension_stats.png" title="Tension statistics" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Figure 2: Statistical tension metrics showing the agreement between different cosmological datasets, sorted by p-value.
</div>

## Significance

This project significantly lowers the barrier to entry for advanced cosmological analysis and establishes a new standard for open, reproducible science in the field. It provides the community with a powerful, common baseline to systematically investigate cosmological tensions and explore physics beyond the standard model.

## Resources

- **GitHub Repository:** [https://github.com/handley-lab/unimpeded](https://github.com/handley-lab/unimpeded)

## References

- Ong, D. D. Y., & Handley, W. (2025). **unimpeded: A Public Nested Sampling Database for Bayesian Cosmology.** [arXiv:2511.05470](https://arxiv.org/abs/2511.05470)
