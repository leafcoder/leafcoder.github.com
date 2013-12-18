---
layout: default
---
{% include nav.html %}

<div class="container">
  <div class="row">
    <div class="box">
      <div class="col-lg-12">
        <hr>
        <h2 class="intro-text text-center">{{ page.title }} <strong>{{ site.name }}</strong></h2>
        <hr>
      </div>
      {{ content }}
    </div>
  </div>

  {% if site.related_posts %}
    <div class="row">
      <div class="box">
        {% for post in site.related_posts %}
        <div class="col-lg-12">
          <a href="{{ post.url }}">{{ post.title }}</a>
        </div>
        {% endfor %}
      </div>
    </div>
  {% endif %}
</div><!-- /.container -->

{% include foot.html %}
