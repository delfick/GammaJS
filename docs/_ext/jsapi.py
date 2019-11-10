from APIgen.main import main as genApi

import subprocess
import tempfile
import os

this_dir = os.path.dirname(__file__)
gma_src = os.path.join(this_dir, "..", "..", "gma")


def createAPI(app):
    buildir = app.env.srcdir

    with tempfile.TemporaryDirectory() as roottemp:
        tempdir = os.path.join(roottemp, "temp")
        outdir = os.path.join(roottemp, "docs")
        resultdir = os.path.join(buildir, "docs", "api")
        templatedir = os.path.join(buildir, "_templates")

        for path in outdir, resultdir, tempdir, templatedir:
            if not os.path.exists(path):
                os.makedirs(path)

        try:
            information = genApi(
                gma_src, outDir=outdir, tempDir=tempdir, templateDirs=[templatedir]
            )
        except:
            import sys, traceback

            _, _, tb = sys.exc_info()
            traceback.print_tb(tb)
            raise

        app.jsapi = information

        subprocess.check_call(["rsync", outdir, resultdir, "-r", "--delete", "-c"])


def removeInfo(app, doctree):
    app.env.jsapi = None


def addInfo(app, env, docname):
    app.env.jsapi = app.jsapi


def setup(app):
    app.connect("builder-inited", createAPI)
    app.connect("doctree-read", removeInfo)
    app.connect("env-purge-doc", addInfo)
