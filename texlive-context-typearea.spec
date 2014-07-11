# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-typearea
# catalog-date 2008-08-18 23:54:09 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-typearea
Version:	20080818
Release:	8
Summary:	Something like Koma-Script typearea
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-typearea
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-typearea.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-typearea.doc.tar.xz
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
%{_texmfdistdir}/tex/context/third/typearea/t-typearea.tex
%doc %{_texmfdistdir}/doc/context/third/typearea/typearea-demo.pdf
%doc %{_texmfdistdir}/doc/context/third/typearea/typearea-doc.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080818-2
+ Revision: 750530
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080818-1
+ Revision: 718144
- texlive-context-typearea
- texlive-context-typearea
- texlive-context-typearea
- texlive-context-typearea

