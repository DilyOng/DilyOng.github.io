---
layout: page
title: cosmulator
description: Accelerating cosmological inference with JAX machine-learning emulators on GPU
img: assets/img/cosmulator/emulator_desy1.jpg
importance: 0.5
category: work
related_publications: false
---

I am the **principal investigator** of the **UKRI-funded DiRAC high-performance computing project** behind `cosmulator`, awarded **10,000 GPU hours** on the DiRAC Tursa supercomputer to train machine-learning emulators.

`cosmulator` trains JAX normalising-flow emulators of nested-sampling posteriors on GPU, so a distribution can be resampled instantly for fast marginalisation and Bayesian evidence, and manages the resulting emulators (training, validation, storage and serving) across a grid of cosmological models and surveys.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/cosmulator/emulator_desy1.jpg" title="Emulator corner plot" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption" style="text-align: left;">
    An emulator at work. A posterior emulator (orange), trained on the DiRAC Tursa supercomputer, reproduces the Dark Energy Survey Year 1 constraints on the cosmological parameters of the Ω<sub>k</sub>ΛCDM model from its full analysis (blue). The diagonal panels show the one-dimensional marginalised posteriors, and the inner and outer contours in the lower triangular panels correspond to the 68% (1σ) and 95% (2σ) credible regions.
</div>

## Installation

```bash
pip install cosmulator            # inspect and use emulators (numpy only)
pip install "cosmulator[train]"   # adds the JAX training stack
```

Requires Python 3.11 or later.

## Resources

- **GitHub Repository:** [https://github.com/DilyOng/cosmulator](https://github.com/DilyOng/cosmulator)
- **PyPI:** [https://pypi.org/project/cosmulator/](https://pypi.org/project/cosmulator/)
