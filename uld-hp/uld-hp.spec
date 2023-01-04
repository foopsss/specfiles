Name:           uld-hp
Version:        1.00.39.12_00.15
Release:        1%{?dist}
Summary:        Driver for HP Laser 100 and HP Color Laser 150 printer series.
BuildArch:      noarch

License:        Propietary
URL:            https://support.hp.com/us-en/drivers/selfservice/swdetails/hp-laser-100-printer-series/24494339/model/24494371/swItemId/ly-227001-2
Source0:        https://ftp.hp.com/pub/softlib/software13/printers/CLP150/%{name}_V%{version}.tar.gz

%description
Driver for HP Laser 100 and HP Color Laser 150 printer series. It does not include ULD, which can be obtained elsewhere.

%prep
%setup -q -n uld

%install
# PPDs.
install -Dm644 noarch/share/ppd/*.ppd -t %{buildroot}%{_datadir}/cups/model/uld
install -Dm644 noarch/share/ppd/cms/*.cts -t %{buildroot}%{_datadir}/cups/model/uld/cms

%files
%license noarch/license/eula.txt
%{_datadir}/cups/model/uld/

%changelog
* Mon Jan 02 2023 Lucas <46837214+foopsss@users.noreply.github.com>
- Initial build.
