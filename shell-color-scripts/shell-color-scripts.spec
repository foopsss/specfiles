Name:           shell-color-scripts
Version:        1.1.r96.da2e3c5
Release:        1%{?dist}
Summary:        A CLI for the collection of terminal color scripts. Includes 50+ beautiful terminal color scripts
BuildArch:      noarch

License:        MIT
URL:            https://gitlab.com/dwt1/shell-color-scripts
Source0:        https://gitlab.com/dwt1/shell-color-scripts/-/archive/master/%{name}-master.tar.gz
Patch0:         shell-color-scripts.patch

%description
The following package provides a program, colorscript, that can display a colorscript from a collection of 50+ colorscripts. Includes completions for the Fish and Zsh shells.

%prep
%setup -q -n shell-color-scripts-master

# Fixes for the colorscripts.sh, _colorscript, colorscript.fish and Makefile files.
%patch0 -p2

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_datadir}/zsh/_colorscript
%{_datadir}/fish/vendor_completions.d/colorscript.fish
%{_libexecdir}/%{name}/colorscripts/
%{_bindir}/colorscript
%{_mandir}/man1/colorscript.1*

%changelog
* Wed Dec 21 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
- Added sed fixes to change the colorscripts' location and a reworked Makefile in a patch.
- Changed the Source0 parameter to use the downloaded source from upstream instead of using a local file.

* Thu Dec 15 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
- First version being packaged.
