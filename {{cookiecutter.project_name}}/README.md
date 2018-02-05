# {{cookiecutter.project_name}}

## Installation

You must have npm and Python 3 available. npm is used for some
CSS processing to help with browser compatibility.

To install, run:

```
npm install
pip install -r requirements.txt
```

## Development

Once you have the dependencies installed, developing is easy:

```
bin/develop.sh
```

Your page is now available
[here](http://localhost:{{cookiecutter.port}}).

You can now modify `theme/templates/index.html`.

## Deployment

There is a script for you that will deploying your code to S3 and invalidate
the CloudFront cache for the `index.html` page. Note that the code does a
destructive rsync to S3. So if there are files you need in your bucket that
might be deleted, you should back them up.

To deploy, run:

```
bin/deploy.sh
```
