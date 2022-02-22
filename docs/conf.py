# Obtain shared config values
import sys
from pathlib import Path

DOC_ROOT = Path(__file__).parent.absolute()
sys.path.extend([str(DOC_ROOT), str(DOC_ROOT.parent)])

from shared_conf import *

# Sitemap configuration
sitemap_locales = [None]
sitemap_url_scheme = "{link}"

# -- 国际化输出 ----------------------------------------------------------------
gettext_compact = False  # optional.
locale_dirs = ['./locales/']