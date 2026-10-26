---
layout: page
title: cosmocompare
description: Bayesian model comparison by importance sampling of existing nested-sampling chains
img: assets/img/cosmocompare/prior_sensitivity.png
importance: 0.75
category: work
related_publications: false
---

I am the **principal investigator** of the **UKRI-funded DiRAC high-performance computing project** behind `cosmocompare`, awarded **100,000 CPU hours** on the Cambridge CSD3 supercomputer to map the prior-sensitivity of cosmological Bayesian evidence via importance sampling.

`cosmocompare` performs Bayesian model comparison without rerunning nested sampling. It takes the posterior samples a survey already produced under one model and prior, reweights them onto a narrowed or changed prior and onto extended models, and recomputes the Bayesian evidence with an uncertainty, so that a model-comparison verdict and its sensitivity to the prior can be obtained in seconds on a laptop.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/cosmocompare/prior_sensitivity.png" title="Prior sensitivity of the Bayesian evidence" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption" style="text-align: left;">
    Prior sensitivity of the evidence for evolving dark energy. The log Bayes factor ln <i>B</i> of w<sub>0</sub>w<sub>a</sub>CDM against ΛCDM is shown as the prior width is narrowed to a fraction <i>f</i> of its original width about the ΛCDM point (w<sub>0</sub>, w<sub>a</sub>) = (−1, 0), for DESI DR2 + CMB alone and combined with the DES-SN5YR, DES-Dovekie and Union3 supernova samples. Each point is obtained by reweighting existing nested-sampling chains rather than rerunning them, and the shaded bands show the uncertainty on ln <i>B</i>. Positive values favour w<sub>0</sub>w<sub>a</sub>CDM and negative values favour ΛCDM. Open markers indicate unreliable reweighting (effective sample size below 1000 or Pareto <i>k̂</i> ≥ 0.7).
</div>

## Installation

```bash
pip install cosmocompare                  # reweighting, evidence, diagnostics
pip install "cosmocompare[likelihood]"    # adds the Cobaya likelihood stack
```

Requires Python 3.11 or later.

## Resources

- **GitHub Repository:** [https://github.com/DilyOng/cosmocompare](https://github.com/DilyOng/cosmocompare)
- **PyPI:** [https://pypi.org/project/cosmocompare/](https://pypi.org/project/cosmocompare/)
