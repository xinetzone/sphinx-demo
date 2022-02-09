"""
Tasks for managing Sphinx documentation trees.
"""

from os.path import join, isdir
from tempfile import mkdtemp
from shutil import rmtree
import sys

from invoke import task, Collection


# Underscored func name to avoid shadowing kwargs in build()
@task(name="clean")
def _clean(c):
    """
    Nuke docs build target directory so next build is clean.
    """
    if isdir(c.sphinx.target):
        rmtree(c.sphinx.target)


# Ditto
@task(name="browse")
def _browse(c):
    """
    Open build target's index.html in a browser (using 'open').
    """
    index = join(c.sphinx.target, c.sphinx.target_file)
    c.run("open {0}".format(index))


@task(
    default=True,
    help={
        "opts": "Extra sphinx-build options/args",
        "clean": "Remove build tree before building",
        "browse": "Open docs index in browser after building",
        "nitpick": "Build with stricter warnings/errors enabled",
        "source": "Source directory; overrides config setting",
        "target": "Output directory; overrides config setting",
    },
)
def build(
    c,
    clean=False,
    browse=False,
    nitpick=False,
    opts=None,
    source=None,
    target=None,
):
    """
    Build the project's Sphinx docs.
    """
    if clean:
        _clean(c)
    if opts is None:
        opts = ""
    if nitpick:
        opts += " -n -W -T"
    cmd = "sphinx-build{0} {1} {2}".format(
        (" " + opts) if opts else "",
        source or c.sphinx.source,
        target or c.sphinx.target,
    )
    c.run(cmd)
    if browse:
        _browse(c)


@task
def doctest(c):
    """
    Run Sphinx' doctest builder.

    This will act like a test run, displaying test results & exiting nonzero if
    all tests did not pass.

    A temporary directory is used for the build target, as the only output is
    the text file which is automatically printed.
    """
    tmpdir = mkdtemp()
    try:
        opts = "-b doctest"
        target = tmpdir
        build(c, clean=True, target=target, opts=opts)
    finally:
        rmtree(tmpdir)


@task
def tree(c):
    """
    Display documentation contents with the 'tree' program.
    """
    ignore = ".git|*.pyc|*.swp|dist|*.egg-info|_static|_build|_templates"
    c.run('tree -Ca -I "{0}" {1}'.format(ignore, c.sphinx.source))


# Vanilla/default/parameterized collection for normal use
ns = Collection(_clean, _browse, build, tree, doctest)
ns.configure(
    {
        "sphinx": {
            "source": "docs",
            # TODO: allow lazy eval so one attr can refer to another?
            "target": join("docs", "_build/html"),
            "target_file": "index.html",
        }
    }
)


# Multi-site variants, used by various projects (fabric, invoke, paramiko)
# Expects a tree like sites/www/<sphinx> + sites/docs/<sphinx>,
# and that you want 'inline' html build dirs, e.g. sites/www/_build/index.html.


def _site(name, help_part):
    _path = join(".", name)
    # TODO: turn part of from_module into .clone(), heh.
    self = sys.modules[__name__]
    coll = Collection.from_module(
        self,
        name=name,
        config={"sphinx": {"source": _path, "target": join(_path, "_build/html")}},
    )
    coll.__doc__ = "Tasks for building {}".format(help_part)
    coll["build"].__doc__ = "Build {}".format(help_part)
    return coll


# Usage doc/API site (published as e.g. docs.myproject.org)
docs = _site("docs", "the API docs subsite.")
