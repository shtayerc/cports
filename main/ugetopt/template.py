pkgname = "ugetopt"
pkgver = "2.38.99"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
pkgdesc = "Standalone util-linux getopt"
license = "GPL-2.0-or-later"
url = "https://github.com/chimera-linux/ugetopt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "19c15c87bc3573fbbf8bdb7dda567c74b233d3fac8c6eb16af7d544f0bf470e4"
hardening = ["vis", "cfi"]
options = ["bootstrap"]
