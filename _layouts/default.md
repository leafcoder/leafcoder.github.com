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

<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
  <div class="container">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="/index.html">{{ site.name }}</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li {% if page.nav == 'HOME' %} class="active" {% endif %}><a href="/index.html">{{ site.name }}</a></li>
        <li {% if page.nav == 'ABOUT' %} class="active" {% endif %}><a href="/about.html">关于</a></li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div>
</nav>

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
