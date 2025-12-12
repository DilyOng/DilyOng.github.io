---
layout: page
title: anesthetic
description: A Python package for processing nested sampling and MCMC chains
img: assets/img/anesthetic/prior_posterior.png
importance: 1.5
category: work
related_publications: true
---

`anesthetic` is a Python package for processing nested sampling and MCMC chains, providing powerful tools for visualising and analysing high-dimensional astronomical data.

## Visualising High-Dimensional Data

Astronomical datasets are inherently high-dimensional, presenting a significant challenge for visualisation and interpretation. When characterising a celestial object like a star or a galaxy, we are not simply measuring its position on the sky, but a host of interdependent physical properties. For example, a single star might be described by its mass, age, temperature, luminosity, distance, and the abundances of a dozen different chemical elements. This creates a parameter space with many dimensions, far beyond the two or three that we can intuitively perceive or plot on a simple graph. Understanding the complex relationships and covariances between these parameters is crucial for testing astrophysical models, but traditional plots that show only two variables at a time can be misleading, as they hide the influence of all other unplotted dimensions.

To navigate this high-dimensional landscape, astronomers frequently rely on a powerful visualisation tool known as a corner plot (also called a triangle plot). A corner plot elegantly displays a series of two-dimensional and one-dimensional projections of the parameter space in a single, compact figure. The diagonal of the plot consists of one-dimensional histograms for each parameter, showing its individual probability distribution. This allows a researcher to see the most likely value and the uncertainty for each variable independently. The off-diagonal panels contain two-dimensional scatter plots or density contours for every possible pair of parameters in the dataset.

The true utility of the corner plot lies in these off-diagonal panels, which reveal the correlations and degeneracies between variables. For instance, an elongated, slanted contour between stellar mass and age would immediately indicate that the data cannot easily distinguish a younger, more massive star from an older, less massive one—a critical insight for model fitting. By systematically laying out all pairwise relationships, the corner plot provides a comprehensive overview of the entire multi-dimensional structure of the data. This allows scientists to assess the results of complex statistical analyses, such as Markov Chain Monte Carlo (MCMC) simulations, at a glance, making it an indispensable tool for understanding the constraints and limitations of their astronomical measurements.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/anesthetic/prior_posterior.png" title="Corner plot" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption" style="text-align: left;">
    Corner plot showing posterior distributions for the Ω<sub>k</sub>ΛCDM cosmological model constrained by Planck with CMB lensing + SDSS data. The diagonal panels show the one-dimensional marginalised prior (blue) and Planck with CMB lensing + SDSS posterior (orange) distributions, demonstrating the constraining power of the observational data. The lower triangular panels display the two-dimensional joint posterior and prior, where the inner (darker blue and darker orange) and outer (lighter blue and lighter orange) contours correspond to the 68% (1σ) and 95% (2σ) credible regions, respectively. The upper triangular panels show scatter plots of samples drawn from the posterior, visually representing parameter correlations. The posterior volume (orange) is much smaller than the prior volume (blue). This corner plot was created using anesthetic.
</div>

## Resources

- **GitHub Repository:** [https://github.com/handley-lab/anesthetic](https://github.com/handley-lab/anesthetic)
