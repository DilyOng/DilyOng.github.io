---
layout: page
title: Outreach
permalink: /outreach/
nav: true
nav_order: 5
horizontal: false
---

<!-- pages/outreach.md -->
<div class="projects">
{% assign sorted_outreach = site.outreach | sort: "importance" %}

  <!-- Generate cards for each outreach item -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_outreach %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_outreach %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
</div>
