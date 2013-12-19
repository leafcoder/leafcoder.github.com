---
layout: main
title: ZoomCat 起点
nav: HOME
---
{% for post in site.posts %}
<div class="row">
  <div class="col-lg-12">
    <h3><em><a href="{{ post.url }}">{{ post.title }}</a></em></h3>
    <p>{{ post.content | truncatewords: 200}}</p>
    <p><em>By {{ post.author }} on <small>{{ post.date | date_to_string }}</small></em></p>
    <a href="{{ post.url }}">Read More...</a>
  </div>
</div>
{% endfor %}
