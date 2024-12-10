---
title: News
permalink: /news/
alias: /current/news/
---
<h1>{{ page.title }}</h1>

<ul>
  {% for post in site.posts %}
    <li class="prettylistitem">
      <h3>{{ post.date | date_to_string }} -- <a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p>{{ post.excerpt }}</p>
    </li>
  {% endfor %}
</ul>