from invoke import Collection #, task, run
from _docs import docs


# @task
# def build(ctx):
#     # run('conda activate py38')
#     run('tvmc -h')


ns = Collection(
    docs
)
