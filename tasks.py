from invoke import Collection, task
from _docs import docs, sites


@task
def init(ctx):
    ctx.run('pip install .[dev] --use-feature=in-tree-build')


ns = Collection(docs, sites, init)
