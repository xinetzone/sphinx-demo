from invoke import Collection, task
from _docs import docs


@task
def init(ctx):
    ctx.run('pip install .[doc] --use-feature=in-tree-build')


ns = Collection(docs, init)
