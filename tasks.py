from invoke import Collection, task
from _docs import docs


@task
def init(ctx):
    ctx.run('pip install .[doc]')


ns = Collection(docs, init)
