import sys
from pathlib import Path


def load_mod():
    DOC_ROOT = Path(__file__).parent.absolute()
    sys.path.extend([str(DOC_ROOT/'utils'),
                    str(DOC_ROOT.parent/'_sphinx'),
                    str(DOC_ROOT.parent/'src'),
                     ])

load_mod()
from shared_conf import *

# Sitemap 配置
sitemap_locales = [None]
sitemap_url_scheme = "{link}"

bibtex_bibfiles = ['refs.bib']

# Napoleon 设置
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True