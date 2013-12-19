---
layout: default
---
{% include nav.html %}

<div class="container-fluid">
  <div class="box">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <hr>
          <h2 class="intro-text text-center">{{ page.title }}</h2>
          <hr>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-12">
          {{ content }}
        </div>
      </div>
      <div class="row">
        <div class="col-lg-12">
          <h2>作者：{{ page.author }}<br><small>{{ page.date | date_to_string }}</small></h2>
        </div>
      </div>
    </div>
  </div>

  {% if site.related_posts.length > 0 %}
  <div class="box">
    <div class="container">
      <div class="row">
        {% for post in site.related_posts %}
        <div class="col-lg-12">
          <a href="{{ post.url }}">{{ post.title }}</a>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
  {% endif %}
</div><!-- /.container -->

{% include foot.html %}
