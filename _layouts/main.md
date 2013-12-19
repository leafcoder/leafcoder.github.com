---
layout: default
---
<div>
  <div class="container-fluid">
    {{ content }}

    {% if site.related_posts %}
    <div class="row">
      <h2>相关文章</h2>
      {% for post in site.related_posts %}
      <div class="row">
        <div class="col-lg-12">
          <a href="{{ post.url }}">{{ post.title }}</a>
        </div>
      </div>
      {% endfor %}
    </div>
    {% endif %}
  </div><!-- /.container -->
</div>
