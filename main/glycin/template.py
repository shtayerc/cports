pkgname = "glycin"
pkgver = "1.1.4"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX libexecdir
]
hostmakedepends = [
    "cargo-auditable",
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "cairo-devel",
    "gtk4-devel",
    "libheif-devel",
    "libjxl-devel",
    "librsvg-devel",
    "libseccomp-devel",
    "pango-devel",
    "rust-std",
]
depends = [self.with_pkgver("glycin-loaders")]
checkdepends = [*depends]
# transitional
provides = [self.with_pkgver("libglycin")]
pkgdesc = "Sandboxed and extendable image decoding"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/glycin"
source = f"$(GNOME_SITE)/glycin/{pkgver[:-2]}/glycin-{pkgver}.tar.xz"
sha256 = "d1b6d590b699b6681a67d01198a581a7f710d8ca7450934dd7f5db241fa12500"
# gobject-introspection
# check: for some divine reason, it always passes locally and never on the builders (??)
options = ["!cross", "!check"]


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
    # so target/release is not triple-prefixed for buildsystem integration
    del self.make_env["CARGO_BUILD_TARGET"]


@subpackage("glycin-devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libglycin-devel")]

    return self.default_devel()


@subpackage("glycin-gtk4")
def _(self):
    self.subdesc = "GTK4 bindings"
    self.depends = [self.with_pkgver("glycin-loaders")]
    # transitional
    self.provides = [self.with_pkgver("libglycin-gtk4")]
    return [
        "lib:libglycin-gtk4-1.so.*",
        "usr/lib/girepository-1.0/GlyGtk4-1.typelib",
    ]


@subpackage("glycin-loaders")
def _(self):
    self.subdesc = "loaders"
    self.depends = ["bubblewrap"]
    return [
        "usr/lib/glycin-loaders",
        "usr/share/glycin-loaders",
    ]
