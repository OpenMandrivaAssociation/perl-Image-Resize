%define upstream_name    Image-Resize
%define upstream_version 0.5

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Simple image resizer using GD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Image/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.5-2mdv2010.0
+ Revision: 430470
- rebuild

* Wed Sep 10 2008 Jérôme Quelin <jquelin@mandriva.org> 0.5-1mdv2009.0
+ Revision: 283532
- import perl-Image-Resize


* Wed Sep 10 2008 cpan2dist 0.5-1mdv
- initial mdv release, generated with cpan2dist

