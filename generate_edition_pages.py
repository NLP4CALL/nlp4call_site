import yaml

content="""---
year: {}
layout: editions
title: NLP4CALL {}
permalink: /past_editions/{}
---"""


with open("./_data/editions.yml") as F:
    editions = yaml.safe_load(F)

for ed in editions:
    year = str(ed["year"])
    with open("./_pages/editions/{}.md".format(year),mode="w+") as F:
        F.write(content.format(year,year,year))