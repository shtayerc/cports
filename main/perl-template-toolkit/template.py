pkgname = "perl-template-toolkit"
pkgver = "3.102"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl templating module"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/Template"
source = f"$(CPAN_SITE)/Template/Template-Toolkit-{pkgver}.tar.gz"
sha256 = "d161c89dee9b213a7c55709ea782e2dd5923dbd1215b9576612889e6e74a2e06"
