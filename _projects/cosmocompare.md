---
layout: page
title: cosmocompare
description: Bayesian model comparison by importance sampling of existing nested-sampling chains
importance: 0.75
category: work
related_publications: false
---

I am the **principal investigator** of the **UKRI-funded DiRAC high-performance computing project** behind `cosmocompare`, awarded **100,000 CPU hours** on the Cambridge CSD3 supercomputer to map the prior-sensitivity of cosmological Bayesian evidence via importance sampling.

`cosmocompare` performs Bayesian model comparison without rerunning nested sampling. It takes the posterior samples a survey already produced under one model and prior, reweights them onto a narrowed or changed prior and onto extended models, and recomputes the Bayesian evidence with an uncertainty, so that a model-comparison verdict and its sensitivity to the prior can be obtained in seconds on a laptop.

## Installation

```bash
pip install cosmocompare                  # reweighting, evidence, diagnostics
pip install "cosmocompare[likelihood]"    # adds the Cobaya likelihood stack
```

Requires Python 3.11 or later.

## Resources

- **GitHub Repository:** [https://github.com/DilyOng/cosmocompare](https://github.com/DilyOng/cosmocompare)
- **PyPI:** [https://pypi.org/project/cosmocompare/](https://pypi.org/project/cosmocompare/)
