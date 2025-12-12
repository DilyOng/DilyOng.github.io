---
layout: page
permalink: /talks/
title: Talks & Conferences
description: Highlighted academic talks and conference presentations.
nav: true
nav_order: 5
---

<div class="talks">
  {% if site.data.talks %}
    <div class="card mt-3 p-3">
      <h3 class="card-title font-weight-medium">Highlighted Academic Talks & Conferences</h3>
      <ul class="card-text font-weight-light list-group list-group-flush">
        {% for talk in site.data.talks %}
          <li class="list-group-item">
            <div class="row">
              <div class="col-xs-2 cl-sm-2 col-md-2 text-center" style="width: 75px">
                <table class="table-cv">
                  <tbody>
                    <tr>
                      <td>
                        <span class="badge font-weight-bold danger-color-dark text-uppercase align-middle" style="min-width: 75px">
                          {{ talk.date }}
                        </span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="col-xs-10 cl-sm-10 col-md-10 mt-2 mt-md-0">
                <h6 class="title font-weight-bold ml-1 ml-md-4">{{ talk.type }}</h6>
                <table class="table-cv ml-1 ml-md-4 institution">
                  <tbody>
                    <tr>
                      <td style="vertical-align: top; text-align: center" class="institution">
                        <i class="fa-solid fa-building-columns iconinstitution"></i>
                      </td>
                      <td class="institution">{{ talk.event }}</td>
                    </tr>
                    {% if talk.location %}
                      <tr>
                        <td style="vertical-align: top; text-align: center" class="institution">
                          <i class="fa-solid fa-location-dot iconinstitution"></i>
                        </td>
                        <td class="institution">{{ talk.location }}</td>
                      </tr>
                    {% endif %}
                  </tbody>
                </table>
                {% if talk.video or talk.slides %}
                  <div class="container-links ml-1 ml-md-4">
                    {% if talk.video %}
                      <div class="container-link-button">
                        <a href="{{ talk.video }}" target="_blank" class="btncv z-depth-0">
                          <i class="fa-solid fa-video"></i> Watch Talk
                        </a>
                      </div>
                    {% endif %}
                    {% if talk.slides %}
                      <div class="container-link-button">
                        <a href="{{ talk.slides }}" target="_blank" class="btncv z-depth-0">
                          <i class="fa-solid fa-file-powerpoint"></i> Slides
                        </a>
                      </div>
                    {% endif %}
                  </div>
                {% endif %}
              </div>
            </div>
          </li>
        {% endfor %}
      </ul>
    </div>
  {% endif %}
</div>
