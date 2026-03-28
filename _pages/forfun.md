---
layout: page
title: For Fun
permalink: /forfun/
nav: true
nav_order: 6
horizontal: false
---

<!-- pages/forfun.md -->
<div class="projects">
{% assign sorted_forfun = site.forfun | sort: "importance" %}

  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_forfun %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_forfun %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
</div>
