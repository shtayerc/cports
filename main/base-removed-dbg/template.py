pkgname = "base-removed-dbg"
pkgver = "1.0"
pkgrel = 0
build_style = "meta"
provides = []
pkgdesc = "Removed debug packages"
license = "custom:meta"
url = "https://chimera-linux.org"
options = ["empty"]

for _pkg in [
    "alsa-pipewire",
    "bsatool",
    "bsdtar",
    "debuginfod",
    "debuginfod-libs",
    "device-mapper",
    "dmesg",
    "esmtool",
    "fcitx5-gtk3",
    "fcitx5-gtk4",
    "fdisk",
    "fstrim",
    "fuse2fs",
    "gmpxx",
    "gstreamer-libcamera",
    "gstreamer-pipewire",
    "heif-thumbnailer",
    "irqtop",
    "lidb-progs",
    "libasn1",
    "libavcodec",
    "libavdevice",
    "libavformat",
    "libavutil",
    "libavfilter",
    "libblkid",
    "libbluetooth",
    "libbtrfs",
    "libbtrfsutil",
    "libbzip3",
    "libcdparanoia",
    "libcolord",
    "libcrypto3",
    "libcryptsetup",
    "libcurl",
    "libdjvulibre",
    "libecpg",
    "libefivar",
    "libegl",
    "libelogind",
    "libfdisk",
    "libflac",
    "libgbm",
    "libgdm",
    "libgirepository",
    "libgl",
    "libglapi",
    "libgles1",
    "libgles2",
    "libglycin",
    "libglycin-gtk4",
    "libgs",
    "libgssapi",
    "libhcrypto",
    "libhdb",
    "libheimbase",
    "libheimntlm",
    "libhx509",
    "libibus",
    "libiptc",
    "libkadm5clnt",
    "libkadm5srv",
    "libkafs",
    "libkdc",
    "libkmod",
    "libkrb5",
    "libldns",
    "libltdl",
    "libmagic",
    "libmagick",
    "libmagick-perl",
    "libmount",
    "libnftables",
    "libnm",
    "libnss_winbind",
    "libntfs-3g",
    "libnuma",
    "libosmesa",
    "libpcre2",
    "libpkgconf",
    "libplist++",
    "libpoppler-cpp",
    "libpoppler-glib",
    "libpoppler-qt6",
    "libpostproc",
    "libpq",
    "libpytalloc-util",
    "libqpdf-libs",
    "libroken",
    "librtmp",
    "libsane",
    "libsensors",
    "libsl",
    "libsmartcols",
    "libsmbclient",
    "libspirv-tools-shared",
    "libsquashfs",
    "libssl3",
    "libswscale",
    "libswresample",
    "libsysfs",
    "libtotem-plparser-mini",
    "libtspi",
    "libunbound",
    "libuuid",
    "libuuid-progs",
    "libvala",
    "libvaladoc",
    "libwbclient",
    "libwget",
    "libwind",
    "libwoff2common",
    "libwoff2dec",
    "libwoff2enc",
    "libxatracker",
    "libxkbregistry",
    "libxtables",
    "lscpu",
    "mkfs",
    "mount",
    "nautilus-gnome-terminal-extension",
    "nfs-server",
    "pam_cgroup",
    "pam_elogind",
    "pam_winbind",
    "projucer",
    "python-mlt",
    "python-opencolorio",
    "python-opencv",
    "python-openimageio",
    "python-openshadinglanguage",
    "python-openvdb",
    "rename",
    "runuser",
    "qalc",
    "rfkill",
    "sdl",
    "tzutils",
    "valadoc",
    "xmlwf",
    "xsltproc",
    "zlib",
    "zramctl",
]:
    provides += [f"{_pkg}-dbg=9999"]
