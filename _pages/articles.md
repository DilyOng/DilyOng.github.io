---
layout: page
title: Articles
permalink: /articles/
nav: true
nav_order: 6
horizontal: false
---

<!-- pages/articles.md -->
<div class="projects">
{% assign sorted_articles = site.articles | sort: "importance" %}

  <!-- Generate cards for each article item -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_articles %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_articles %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
</div>
