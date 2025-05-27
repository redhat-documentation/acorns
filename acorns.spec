Name: acorns
Summary: Generate an AsciiDoc release notes document from tracking tickets.
Version: 1.0.1
Release: 1%{?dist}
License: GPLv3+
URL: https://github.com/redhat-documentation/acorns
Group: Applications/Text
Obsoletes: cizrna
#Source0: https://static.crates.io/crates/%{name}/%{name}-%{version}.crate
Source0: https://github.com/redhat-documentation/%{name}/archive/refs/tags/v%{version}.tar.gz

# This works fine with Fedora and RHEL, but breaks the SUSE build:
ExclusiveArch: %{rust_arches}

# Build dependencies of acorns:
BuildRequires: openssl-devel
# Dependencies of the Rust compiler:
BuildRequires: make
BuildRequires: gcc
BuildRequires: llvm

Requires: openssl-libs

%description
%{summary}

# Disable debugging packages. RPM looks for them even though none are created,
# and that breaks the build if you don't set this option.
%global debug_package %{nil}

%prep
# Unpack the sources.
%setup -q

%build
# Install the latest Rust compiler.
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain stable --component cargo

# Build the binary.
~/.cargo/bin/cargo build --release

%install
# Clean up previous artifacts.
rm -rf %{buildroot}
# Prepare the target directories.
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
# Install the binary into the chroot environment.
install -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
# An alternative way to install the binary using cargo.
# cargo install --path . --root %{buildroot}/usr
# Compress the man page.
gzip -c target/release/build/%{name}-*/out/%{name}.1 > %{name}.1.gz
# Install the man page into the chroot environment.
install -m 0644 %{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
# Pick documentation and license files from the source directory.
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%{_mandir}/man1/%{name}.1.gz
# Pick the binary from the virtual, chroot system.
%{_bindir}/%{name}
