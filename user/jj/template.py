pkgname = "jj"
pkgver = "0.21.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "libgit2-devel",
    "libssh2-devel",
    "openssl-devel",
    "rust-std",
    "zstd-devel",
]
checkdepends = ["openssh"]
pkgdesc = "Git-compatible VCS frontend"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://martinvonz.github.io/jj"
source = f"https://github.com/martinvonz/jj/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c38d98d7db42f08b799f5c51f33cd8454867bc4862a15aa0897b72f2d32eea0a"
# generates completions with host binary
options = ["!cross"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "serde_bser")


def post_build(self):
    for shell in ["bash", "fish", "nushell", "zsh"]:
        with open(f"{self.cwd}/jj.{shell}", "w") as o:
            self.do(
                f"target/{self.profile().triplet}/release/jj",
                "util",
                "completion",
                shell,
                stdout=o,
            )
    with open(f"{self.cwd}/jj.1", "w") as o:
        self.do(
            f"target/{self.profile().triplet}/release/jj",
            "util",
            "mangen",
            stdout=o,
        )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/jj")
    for shell in ["bash", "fish", "nushell", "zsh"]:
        self.install_completion(f"jj.{shell}", shell)
    self.install_man("jj.1")
