%global tl_name spectral
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Spectral fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/spectral
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spectral.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spectral.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Spectral family of fonts, designed by Jean-Baptiste Levee at the
Production Type digital type design agency. Spectral is a new and
versatile serif face available in seven weights of roman and italic,
with small caps.

