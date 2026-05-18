---
layout: page
title: Outreach
permalink: /outreach/
nav: true
nav_order: 6
horizontal: false
---

I actively take part in outreach, especially with young children, because I believe it provides inspiration to the next generation. I am who I am today — a cosmologist happily doing research at the University of Cambridge — because outreach reached me at a point in my life when I was younger.

Below are some of the outreach activities I have participated in.

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
