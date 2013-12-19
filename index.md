---
layout: main
title: ZoomCat 起点
---
{% for post in site.posts %}
<div class="box">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <hr>
        <h2 class="intro-text text-center"><strong>{{ post.title }}</strong></h2>
        <hr>
        <p>{{ post.content | truncatewords: 200}}</p>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-12 text-center">
        <h2>作者：{{ post.author }}<br><small>{{ post.date | date_to_string }}</small></h2>
        <a href="{{ post.url }}" class="btn btn-default btn-lg">阅读更多</a>
        <hr>
      </div>
    </div>
  </div>
</div>
{% endfor %}
