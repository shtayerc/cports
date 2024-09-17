pkgname = "gmic"
pkgver = "3.4.2"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "QMAKE=qmake6",
    "OPT_CFLAGS=",
]
make_use_env = True
hostmakedepends = [
    "bash",
    "gimp",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "fftw-devel",
    "libcurl-devel",
    "libomp-devel",
    "libpng-devel",
    "libtiff-devel",
    "libx11-devel",
    "openexr-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Full-featured Open-Source Framework for Image Processing"
maintainer = "psykose <alice@ayaya.dev>"
license = "CECILL-2.1"
url = "https://gmic.eu"
source = f"https://gmic.eu/files/source/gmic_{pkgver}.tar.gz"
sha256 = "9abd8377693715f87104bdbe077d45ecb00cf19f57c29f425eacda07c745fe8a"
# vis broken
# FIXME int: gmic_qt PreviewWidget::updateOriginalImagePosition
hardening = ["!int"]
# no tests
options = ["!check"]


def build(self):
    # lib has to come first to not be built multiple times for all subsequent
    # targets, rest can be parallel (and so this is faster than -j1)
    self.make.build(["lib"])
    self.make.build(["cli_shared", "gmic_qt_shared"])


@subpackage("gmic-devel")
def _(self):
    return self.default_devel()


@subpackage("gmic-qt")
def _(self):
    self.pkgdesc = "Qt GUI for GMIC"
    return [
        "usr/bin/gmic_qt",
        "usr/share/applications",
        "usr/share/icons",
    ]