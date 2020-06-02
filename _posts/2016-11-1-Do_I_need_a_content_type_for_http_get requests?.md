---
layout: post
title: Do I need a content type for http get requests?
description: "Do I need a content type for http get requests?"
category: articles
tags: [QA]
image:
  feature:
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: false
share: true
---

Any HTTP/1.1 message containing an entity-body SHOULD include a Content-Type header field defining the media type of that body. If and only if the media type is not given by a Content-Type field, the recipient MAY attempt to guess the media type via inspection of its content and/or the name extension(s) of the URI used to identify the resource. If the media type remains unknown, the recipient SHOULD treat it as type "application/octet-stream".

http://stackoverflow.com/questions/5661596/do-i-need-a-content-type-for-http-get-requests
