
%define realname   Image-Resize
%define version    0.5
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Simple image resizer using GD
Source:     http://www.cpan.org/modules/by-module/Image/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(GD)

BuildArch: noarch

%description
Despite its heavy weight, I've always used Image::Magick for creating image
thumbnails. I know it can be done using lighter-weight GD, I just never
liked its syntax. Really, who wants to remember the lengthy arguments list
of copyResized() or copyResampled() functions:

    $image->copyResampled($sourceImage,$dstX,$dstY,
                        $srcX,$srcY,$destW,$destH,$srcW,$srcH);

when Image::Magick lets me say:

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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


