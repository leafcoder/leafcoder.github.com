---
layout: main
title: ZoomCat 起点
---
{% for post in site.posts %}
<div class="box">
  <div class="row">
    <div class="col-lg-12 text-center">
      <hr>
      <h2 class="intro-text text-center">{{ page.title }} <strong>{{ site.name }}</strong></h2>
      <hr>
      <p>{{ post.content }}</p>
      <h2>作者：{{ post.author }}<br><small>{{ post.date | date_to_string }}</small></h2>
      <a href="{{ post.url }}" class="btn btn-default btn-lg">阅读更多</a>
      <hr>
    </div>
  </div>
</div>
{% endfor %}
