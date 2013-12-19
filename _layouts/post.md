---
layout: default
---
<div class="row">
  <div class="col-lg-12">
    <h3><em><a href="{{ post.url }}">{{ page.title }}</a></em></h3>
    <p>{{ content }}</p>
    <p><em>By {{ page.author }} on <small>{{ page.date | date_to_string }}</small></em></p>
  </div>
</div>
<div class="row">
  <div class="col-lg-12">
    <p><em>相关文章</em><p>
  </div>
</div>
{% for post in site.related_posts %}
<div class="row">
  <div class="col-lg-12">
    <i class="icon-angle-right"></i> <a href="{{ post.url }}">{{ post.title }}</a> By <em>{{ post.author }}</em> on <em>{{ post.date | date_to_string }}</em>
  </div>
</div>
{% endfor %}
