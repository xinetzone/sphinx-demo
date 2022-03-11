import sys
from pathlib import Path

# 载入自定义模块
def load_mod():
    DOC_ROOT = Path(__file__).parent.absolute()
    sys.path.extend([str(DOC_ROOT/'utils'),
                    str(DOC_ROOT.parent/'_sphinx'),
                    str(DOC_ROOT.parent/'src'),
                     ])
# =====================================================================================
# 下面的内容可以自行配置
# -- Project information -----------------------------------------------------
project = 'sphinx-demo'
copyright = '2021, xinetzone'
author = 'xinetzone'

# The full version, including alpha/beta/rc tags
release = '0.1'

comments_config = {
    "hypothesis": True,
    "dokieli": False,
    "utterances": {
        "repo": "xinetzone/sphinx-demo",
        "optional": "config",
    }
}

# Sitemap 配置
sitemap_locales = [None]
sitemap_url_scheme = "{link}"
html_context = {
    'test_versions': ['latest', 'translation'],
    'locale_versions': ['zh_CN'],
}

bibtex_bibfiles = ["references.bib"]

extlinks = {
    # 'duref': ('https://docutils.sourceforge.io/docs/ref/rst/'
    #           'restructuredtext.html#%s', ''),
    # 'durole': ('https://docutils.sourceforge.io/docs/ref/rst/'
    #            'roles.html#%s', ''),
    # 'dudir': ('https://docutils.sourceforge.io/docs/ref/rst/'
    #           'directives.html#%s', ''),
    # 'py-doc': ('https://daobook.github.io/cpython/%s', ''),
    # 'daobook': ('https://daobook.github.io/%s', ''),
}

intersphinx_mapping = {
    # 'python': ('https://daobook.github.io/cpython/', None),
    # 'sphinx': ('https://daobook.github.io/sphinx/', None),
    # 'peps': ('https://daobook.github.io/peps', None),
}

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

blog_baseurl = "https://xinetzone.github.io/sphinx-demo"
# 默认作者的名字
blog_default_author = "lxw"
# 默认语言的代码名称
blog_default_language = 'zh'
# 一个作者名字的字典，映射到作者的完整显示名称和链接。
# 字典的键值应该在 ``post`` 指令中使用，以指代作者。默认是 ``{}``。
blog_authors = {
    "lxw": ("刘新伟", None),
}

load_mod()
from shared_conf import *
# 替换 shared_conf.py 的配置
html_theme_options.update(
    {
        # 默认情况下，编辑按钮将指向版本库的根。
        # 如果你的文档被托管在一个子文件夹中，请使用以下配置：
        "path_to_docs": "docs/",  # 文档的路径，默认 `docs/``
        "repository_url": "https://github.com/xinetzone/sphinx-demo",
        "repository_branch": "main",  # 文档库的分支，默认 `master`
    }
)