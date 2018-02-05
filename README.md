# Cookiecutter Landing Page

A template for [Cookiecutter](https://github.com/audreyr/cookiecutter) for
generating a landing page, ready to deploy to
[CloudFront](https://aws.amazon.com/cloudfront/).

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Usage](#usage)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Usage

Before getting started, it's easiest to already have a
CloudFront distribution set up. The general steps involved
are:

- Create an S3 bucket that will house the actual HTML files
- Create a CloudFront distribution that points to this S3 bucket as its source
  - Configure the distribution so that it allows caching based on query
    strings, where the whitelisted query string is `v`:

    ![cloudfront screenshot](https://raw.githubusercontent.com/b-ryan/cookiecutter-landing-page/master/cache-bust-screenshot.png)

If you don't have a domain, you can always do this later. But you'll have to
modify some files manually once you create the distribution (I can add notes
about this later).

Now generate the landing page:

```
$ pip install cookiecutter
$ cookiecutter https://github.com/b-ryan/cookiecutter-landing-page
```

Once you have generated your project, see the README within the project
directory for details on developing and deploying.

## Features

- Uses [Pelican](https://blog.getpelican.com/) as the static page generator.
  (Normally Pelican is used as / thought of as a blog generator, but it has
  been working well for my needs as a landing page generator.)
- Built-in cache busting
- Auto-generated development and deploy scripts.
- Bootstrap 4
