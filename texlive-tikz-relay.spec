%global tl_name tikz-relay
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	TikZ library for typesetting electrical diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-relay
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-relay.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-relay.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains a collection of symbols for typesetting electrical
wiring diagrams for relay control systems. The symbols are meant to be
in agreement with the international standard IEC-60617 which has been
adopted worldwide, with perhaps the exception of the USA. It extends and
modifies, when needed, the TikZ-library circuits.ee.IEC. A few non-
standard symbols are also included mainly to be used in presentations,
particularly with the beamer package.

