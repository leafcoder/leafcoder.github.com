---
layout: default
---
{% include nav.html %}

<div class="container">
  {{ content }}

  {% if site.related_posts %}
  <div class="row">
    <div class="box">
      <div class="row">
        <div class="col-lg-12">
          <h2>相关文章</h2>
        </div>
      </div>
      {% for post in site.related_posts %}
      <div class="row">
        <div class="col-lg-12">
          <a href="{{ post.url }}">{{ post.title }}</a>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
  {% endif %}
</div><!-- /.container -->

{% include foot.html %}
