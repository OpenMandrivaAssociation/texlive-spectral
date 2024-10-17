Name:		texlive-spectral
Version:	64528
Release:	2
Summary:	Spectral fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/spectral
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spectral.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spectral.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Spectral family of fonts, designed by
Jean-Baptiste Levee at the Production Type digital type design
agency. Spectral is a new and versatile serif face available in
seven weights of roman and italic, with small caps.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/spectral
%{_texmfdistdir}/fonts/vf/production/spectral
%{_texmfdistdir}/fonts/type1/production/spectral
%{_texmfdistdir}/fonts/truetype/production/spectral
%{_texmfdistdir}/fonts/tfm/production/spectral
%{_texmfdistdir}/fonts/map/dvips/spectral
%{_texmfdistdir}/fonts/enc/dvips/spectral
%doc %{_texmfdistdir}/doc/fonts/spectral

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
