Name:		texlive-context-typearea
Version:	47085
Release:	2
Summary:	Something like Koma-Script typearea
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-typearea
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-typearea.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-typearea.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The module provides a command that calculates the page layout
as the LaTeX package typearea does.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/typearea
%doc %{_texmfdistdir}/doc/context/third/typearea

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
