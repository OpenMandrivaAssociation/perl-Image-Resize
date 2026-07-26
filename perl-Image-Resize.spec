%define upstream_name    Image-Resize
Name:		perl-%{upstream_name}
Version:	0.5
Release:	7

Summary:	Simple image resizer using GD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Image-Resize
Source0:	https://cpan.metacpan.org/authors/id/S/SH/SHERZODR/Image-Resize-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(GD)

BuildArch:	noarch

%description
Despite its heavy weight, I've always used Image::Magick for creating image
thumbnails. I know it can be done using lighter-weight GD, I just never
liked its syntax. Really, who wants to remember the lengthy arguments list
of copyResized() or copyResampled() functions:

    $image->copyResampled($sourceImage,$dstX,$dstY,
                        $srcX,$srcY,$destW,$destH,$srcW,$srcH);

when Image::Magick lets me say:

    $image->Scale(-geometry=>'250x250');

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.500.0-2mdv2011.0
+ Revision: 655035
- rebuild for updated spec-helper

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-1mdv2011.0
+ Revision: 504933
- rebuild using %0.5 Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.5-2mdv2010.0
+ Revision: 430470
- rebuild

* Wed Sep 10 2008 Jérôme Quelin <jquelin@mandriva.org> 0.5-1mdv2009.0
+ Revision: 283532
- import perl-Image-Resize


* Wed Sep 10 2008 cpan2dist 0.5-1mdv
- initial mdv release, generated with cpan2dist

