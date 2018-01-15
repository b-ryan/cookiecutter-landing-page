from pelican import signals
import pickle
import subprocess
import os


class Plugin(object):
    def __init__(self):
        self.pelican = None

    def initialized(self, pelican):
        self.pelican = pelican

    def finalized(self, _):
        path = os.path.join(self.pelican.settings["OUTPUT_PATH"],
                            "theme/css-build")
        subprocess.check_call([
            "npx",
            "postcss",
            "theme/static/css/*.css",
            "--use", "autoprefixer",
            "-d", path,
        ])

    def generator_init(self, generator):
        settings = self.pelican.settings
        def css_link(filename):
            return (
                '<link href="{}/theme/css-build/{}?v={}" rel="stylesheet">'
                .format(settings["SITEURL"], filename, settings["CACHE_BUST"])
            )
        def img_url(filename):
            return (
                "/theme/img/{}?v={}"
                .format(filename, settings["CACHE_BUST"])
            )
        generator.context["css_link"] = css_link
        generator.context["img_url"] = img_url

plugin = Plugin()


def register():
    signals.initialized.connect(plugin.initialized)
    signals.finalized.connect(plugin.finalized)
    signals.generator_init.connect(plugin.generator_init)
