---
layout: page
title: cosmulator
description: Accelerating cosmological inference with JAX machine-learning emulators on GPU
importance: 0.5
category: work
related_publications: false
---

I am the **principal investigator** of the **UKRI-funded DiRAC high-performance computing project** behind `cosmulator`, awarded **10,000 GPU hours** on the DiRAC Tursa supercomputer to train machine-learning emulators.

`cosmulator` trains JAX normalising-flow emulators of nested-sampling posteriors on GPU, so a distribution can be resampled instantly for fast marginalisation and Bayesian evidence, and manages the resulting emulators (training, validation, storage and serving) across a grid of cosmological models and surveys.

## Installation

```bash
pip install cosmulator            # inspect and use emulators (numpy only)
pip install "cosmulator[train]"   # adds the JAX training stack
```

Requires Python 3.11 or later.

## Resources

- **GitHub Repository:** [https://github.com/DilyOng/cosmulator](https://github.com/DilyOng/cosmulator)
- **PyPI:** [https://pypi.org/project/cosmulator/](https://pypi.org/project/cosmulator/)
