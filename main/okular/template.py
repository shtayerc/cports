pkgname = "okular"
pkgver = "24.12.2"
pkgrel = 0
build_style = "cmake"
# FIXME segfaults/weird failures
make_check_args = [
    "-E",
    "(parttest|visibilitytest|signunsignedfieldtest|documenttest|mainshelltest|annotationtoolbartest|epubgeneratortest)",
]
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "discount-devel",
    "djvulibre-devel",
    "ebook-tools-devel",
    "karchive-devel",
    "kbookmarks-devel",
    "kcompletion-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdegraphics-mobipocket-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kparts-devel",
    "kpty-devel",
    "ktextwidgets-devel",
    "kwallet-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libkexiv2-devel",
    "libspectre-devel",
    "libzip-devel",
    "phonon-devel",
    "plasma-activities-devel",
    "poppler-devel",
    "purpose-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtspeech-devel",
    "qt6-qtsvg-devel",
    "threadweaver-devel",
]
checkdepends = ["dbus", "xwayland-run"]
pkgdesc = "KDE document viewer"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/okular"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/okular-{pkgver}.tar.xz"
sha256 = "036cc27dea900a3eae27de9e2fb540d9568a1995d843669baa2a36c2e41556de"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("okular-devel")
def _(self):
    self.depends += [
        "kconfig-devel",
        "kcoreaddons-devel",
        "kxmlgui-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
