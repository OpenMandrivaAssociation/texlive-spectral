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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Spectral family of fonts, designed by Jean-Baptiste Levee at the
Production Type digital type design agency. Spectral is a new and
versatile serif face available in seven weights of roman and italic,
with small caps.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from spectral:
Map spectral.map
TL_DROPIN_EOF
