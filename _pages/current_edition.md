---
title: This year's edition of the Workshop
permalink: /current_edition/
alias: /current/current_edition/
---

{% capture current %}{{site.data.editions.first.year}}{% endcapture %}
{% capture title %}{{site.data.editions.first.long_name}}{% endcapture %}
# {{title}}
{% include_relative editions/content/{{current | append:".md"}} %}
{{current}}
