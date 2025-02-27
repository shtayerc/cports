pkgname = "sakura"
pkgver = "3.8.8"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "gettext", "ninja", "perl", "pkgconf"]
makedepends = ["vte-gtk3-devel"]
pkgdesc = "Libvte-based terminal emulator"
license = "GPL-2.0-only"
url = "https://launchpad.net/sakura"
source = f"{url}/trunk/{pkgver}/+download/sakura-{pkgver}.tar.gz"
sha256 = "9f7e6b4e00401279686ca3ff11bab988d817b2df37ddf42d16cd3c3090560c38"
hardening = ["cfi", "vis"]
