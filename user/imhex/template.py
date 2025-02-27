pkgname = "imhex"
pkgver = "1.37.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DIMHEX_BUNDLE_DOTNET=OFF",
    "-DIMHEX_DISABLE_STACKTRACE=ON",
    "-DIMHEX_ENABLE_UNIT_TESTS=ON",
    "-DIMHEX_IGNORE_BAD_CLONE=ON",
    "-DIMHEX_OFFLINE_BUILD=ON",
    "-DIMHEX_STRICT_WARNINGS=OFF",
    "-DIMHEX_STRIP_RELEASE=OFF",
    "-DUSE_SYSTEM_CAPSTONE=ON",
    "-DUSE_SYSTEM_FMT=ON",
    "-DUSE_SYSTEM_LLVM=ON",
    "-DUSE_SYSTEM_NLOHMANN_JSON=ON",
    "-DUSE_SYSTEM_YARA=ON",
]
make_build_args = ["--target", "all", "unit_tests"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "capstone-devel",
    # for llvm cmake detection to work
    "clang-tools-extra",
    "curl-devel",
    "dbus-devel",
    "file-devel",
    "fmt-devel",
    "freetype-devel",
    "glfw-devel",
    "libarchive-devel",
    "libedit-devel",
    "llvm-devel",
    # LLVMdemangle is static only
    "llvm-devel-static",
    "mbedtls-devel",
    "nlohmann-json",
    "xz-devel",
    "yara-devel",
]
pkgdesc = "Hex editor for reverse engineers"
license = "GPL-2.0-or-later"
url = "https://imhex.werwolv.net"
source = [
    f"https://github.com/WerWolv/ImHex/releases/download/v{pkgver}/Full.Sources.tar.gz>src-{pkgver}.tar.gz",
    f"https://github.com/WerWolv/ImHex-Patterns/archive/refs/tags/ImHex-v{pkgver}.tar.gz",
]
source_paths = [
    ".",
    "ImHex-Patterns",
]
sha256 = [
    "38f670293fcc1e5a06fccf7d35dd8c23a4be8c6ab4a5e3b2900f730d2a8ad2f5",
    "dc009ad616e73209f8eed1a1a36ebea70e1288a038e756d4ad0c341991fcbfb3",
]
# FIXME: drop with LLVM 20 where std::jthread & std::stop_token are deemed stable
tool_flags = {"CXXFLAGS": ["-fexperimental-library"]}

if self.profile().wordsize == 32:
    broken = "uses int128"


def post_install(self):
    self.uninstall("usr/bin/imhex-updater")


@subpackage("imhex-devel")
def _(self):
    return self.default_devel(extra=["usr/share/imhex/sdk"])
