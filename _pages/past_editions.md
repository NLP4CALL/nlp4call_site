---
title: Past editions
permalink: /past_editions/
alias: /current/past_editions/
---

<h1>Past editions</h1>

<ul>
  {% for edition in site.editions reversed %}
    <li class="prettylistitem">
      <h2><a href="{{ edition.external_url }}">{{ edition.name }}</a></h2>
      <p>{{ edition.content | markdownify }}</p>
      <p><a href="{{ edition.proceedings_url }}">Proceedings available here</a></p>
    </li>
  {% endfor %}
</ul>