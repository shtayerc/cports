pkgname = "taplo"
pkgver = "0.9.3"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "-p",
    "taplo-cli",
    "--no-default-features",
    "--features",
    "native-tls,lsp",
]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "openssl-devel",
    "rust-std",
]
pkgdesc = "CLI for TOML"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://taplo.tamasfe.dev"
source = f"https://github.com/tamasfe/taplo/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "65510664071252541e66f603dc9aa04016c38d62299061419c95d3bffaa73125"


def do_install(self):
    self.install_license("LICENSE.md")
    self.install_bin(f"target/{self.profile().triplet}/release/taplo")
