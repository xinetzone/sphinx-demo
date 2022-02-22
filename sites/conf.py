import sys
from pathlib import Path

DOC_ROOT = Path(__file__).parent.absolute()
sys.path.extend([str(DOC_ROOT), str(DOC_ROOT.parent)])

from shared_conf import *

extensions.append("sphinx_sitemap")

# -- 国际化输出 ----------------------------------------------------------------
gettext_compact = False  # optional.
locale_dirs = ['locales/']


def setup(app):
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')

