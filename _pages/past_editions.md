---
title: Past editions
permalink: /past_editions/
alias: /current/past_editions/
---

# Past editions


<ul>
  {% for edition in site.data.editions %}
    <li class="prettylistitem">
      <h2><a href="/past_editions/{{ edition.year }}">NLP4CALL {{ edition.year }}</a></h2>
      <p>{{edition.long_name}}<br>{{edition.co_located}}, {{edition.place}}, {{edition.date}}, {{edition.year}}</p>
      {% if edition.proceedings_url == "None" %}
        <p>Proceedings coming soon...</p>
      {% else %}
        <p><a href="{{ edition.proceedings_url }}">Proceedings available here</a></p>
      {% endif %}
      
    </li>
  {% endfor %}
</ul>