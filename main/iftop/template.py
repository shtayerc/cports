pkgname = "iftop"
pkgver = "1.0_p4"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake"]
makedepends = ["libpcap-devel", "linux-headers", "ncurses-devel"]
pkgdesc = "Display bandwidth usage on an interface by host"
license = "GPL-2.0-or-later"
url = "https://pdw.ex-parrot.com/iftop"
source = f"{url}/download/iftop-1.0pre4.tar.gz"
sha256 = "f733eeea371a7577f8fe353d86dd88d16f5b2a2e702bd96f5ffb2c197d9b4f97"
