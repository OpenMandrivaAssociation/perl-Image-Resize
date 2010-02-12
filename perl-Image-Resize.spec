%define upstream_name    Image-Resize
%define upstream_version 0.5

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Simple image resizer using GD
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Image/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(GD)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
