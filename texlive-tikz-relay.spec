Name:		texlive-tikz-relay
Version:	64072
Release:	2
Summary:	TikZ library for typesetting electrical diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tikz-relay
License:	lppl1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-relay.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-relay.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains a collection of symbols for typesetting
electrical wiring diagrams for relay control systems. The
symbols are meant to be in agreement with the international
standard IEC-60617 which has been adopted worldwide, with
perhaps the exception of the USA. It extends and modifies, when
needed, the TikZ-libray circuits.ee.IEC. A few non-standard
symbols are also included mainly to be used in presentations,
particularly with the beamer package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-relay
%doc %{_texmfdistdir}/doc/latex/tikz-relay

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
