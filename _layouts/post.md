---
layout: default
---
<div class="row">
  <div class="col-md-12">
    <h1 class="page-header">{{ page.title }}</h1>
  </div>
</div>
<div class="row">
  <div class="col-md-12">
    <p>{{ content }}</p>
    <p>By <a href="/about.html">{{ page.author }}</a> on {{ page.date | date_to_string }}</p>
  </div>
</div>

<div class="panel panel-default">
  <div class="panel-heading">相关文章</div>
  <div class="panel-body">
    {% for post in site.related_posts %}
    <div class="row">
      <div class="col-lg-12">
        <i class="icon-angle-right"></i> <a href="{{ post.url }}">{{ post.title }}</a> By {{ post.author }} on {{ post.date | date_to_string }}
      </div>
    </div>
    {% endfor %}
  </div>
</div>

<div class="panel panel-default">
  <div class="panel-heading">评论</div>
  <div class="panel-body">
    <div id="disqus_thread"></div>
  </div>
</div>

<script type="text/javascript">
    /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
    var disqus_shortname = 'digflybird'; // required: replace example with your forum shortname

    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
<a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>

