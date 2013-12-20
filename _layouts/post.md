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

<div id="disqus_thread"></div>
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
  
