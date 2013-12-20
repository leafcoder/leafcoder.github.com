<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>{{ page.title }}</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.css" rel="stylesheet">
    <!-- Font Awesome 3.0 CSS -->
    <link href="/css/font-awesome.css" rel="stylesheet">
    <!-- Add custom CSS here -->
    <link href="/css/custome.css" rel="stylesheet">
  </head>

  <body>

    <div class="container">
      <h2>{{ site.name }}</h2>
      <ul class="nav" id="nav">
        <li {% if page.nav == 'HOME' %} class="active" {% endif %}><a href="/index.html">人生起点</a></li>
        <li {% if page.nav == 'ABOUT' %} class="active" {% endif %}><a href="/about.html">关于 DigFlyBird</a></li>
      </ul>
    </div>

    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          {{ content }}
        </div>
      </div>
    </div>

    {% include foot.html %}

    <!-- JavaScript -->
    <script src="/js/jquery-1.10.2.js"></script>
    <script src="/js/bootstrap.js"></script>

  </body>
</html>
