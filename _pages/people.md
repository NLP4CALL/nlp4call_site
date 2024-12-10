---
title: Organisers
permalink: /people/
alias: /current/people/
---
<h1>People</h1>

<ul>
  {% for author in site.people %}
    <li class="prettylistitem">
      <h2><a href="{{ author.url | relative_url}}">{{ author.name }}</a></h2>
      <h3>{{ author.position }}</h3>
      {% if author.picture != nil %} <img src={{ author.picture  | relative_url }} alt={{ author.name }} class="responsive"/>{% endif %}
      <p>{{ author.content | markdownify }}</p>
    </li>
  {% endfor %}
</ul>
