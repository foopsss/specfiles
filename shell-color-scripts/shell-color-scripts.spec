Name:           shell-color-scripts
Version:        1.1.r96.da2e3c5
Release:        1%{?dist}
Summary:        A CLI for the collection of terminal color scripts. Includes 50+ beautiful terminal color scripts
BuildArch:      noarch

License:        MIT
URL:            https://gitlab.com/dwt1/shell-color-scripts.git
Source0:        %{name}-%{version}.tar.gz

%description
The following package provides a program, colorscript, that can display a colorscript from a collection of 50+ colorscripts.

%prep
%setup -q -n shell-color-scripts

# Fixes for the colorscripts.sh, _colorscript and colorscript.fish files.
sed -i 's!/opt/shell-color-scripts/colorscripts!/usr/lib64/shell-color-scripts/colorscripts!' colorscript.sh
sed -i 's!/opt/shell-color-scripts/colorscripts!/usr/lib64/shell-color-scripts/colorscripts!' completions/_colorscript
sed -i 's!/opt/shell-color-scripts/colorscripts!/usr/lib64/shell-color-scripts/colorscripts!' completions/colorscript.fish

%install
install -Dm755 completions/_colorscript %{buildroot}%{_datadir}/zsh/_colorscript
install -Dm755 completions/colorscript.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/colorscript.fish
install -Dm755 colorscripts/* -t %{buildroot}%{_libdir}/%{name}/colorscripts
install -Dm755 colorscript.sh %{buildroot}%{_bindir}/colorscript
install -Dm644 colorscript.1 %{buildroot}%{_mandir}/man1/colorscript.1

%files
%license LICENSE
%doc README.md
%{_datadir}/zsh/_colorscript
%{_datadir}/fish/vendor_completions.d/colorscript.fish
%{_libdir}/%{name}/colorscripts/00default.sh
%{_libdir}/%{name}/colorscripts/alpha
%{_libdir}/%{name}/colorscripts/arch
%{_libdir}/%{name}/colorscripts/awk-rgb-test
%{_libdir}/%{name}/colorscripts/bars
%{_libdir}/%{name}/colorscripts/blocks1
%{_libdir}/%{name}/colorscripts/blocks2
%{_libdir}/%{name}/colorscripts/bloks
%{_libdir}/%{name}/colorscripts/colorbars
%{_libdir}/%{name}/colorscripts/colortest
%{_libdir}/%{name}/colorscripts/colortest-slim
%{_libdir}/%{name}/colorscripts/colorview
%{_libdir}/%{name}/colorscripts/colorwheel
%{_libdir}/%{name}/colorscripts/crowns
%{_libdir}/%{name}/colorscripts/crunch
%{_libdir}/%{name}/colorscripts/crunchbang
%{_libdir}/%{name}/colorscripts/crunchbang-mini
%{_libdir}/%{name}/colorscripts/darthvader
%{_libdir}/%{name}/colorscripts/debian
%{_libdir}/%{name}/colorscripts/dna
%{_libdir}/%{name}/colorscripts/doom-original
%{_libdir}/%{name}/colorscripts/doom-outlined
%{_libdir}/%{name}/colorscripts/elfman
%{_libdir}/%{name}/colorscripts/faces
%{_libdir}/%{name}/colorscripts/fade
%{_libdir}/%{name}/colorscripts/ghosts
%{_libdir}/%{name}/colorscripts/guns
%{_libdir}/%{name}/colorscripts/hex
%{_libdir}/%{name}/colorscripts/illumina
%{_libdir}/%{name}/colorscripts/jangofett
%{_libdir}/%{name}/colorscripts/kaisen
%{_libdir}/%{name}/colorscripts/manjaro
%{_libdir}/%{name}/colorscripts/monster
%{_libdir}/%{name}/colorscripts/mouseface
%{_libdir}/%{name}/colorscripts/mouseface2
%{_libdir}/%{name}/colorscripts/pacman
%{_libdir}/%{name}/colorscripts/panes
%{_libdir}/%{name}/colorscripts/pinguco
%{_libdir}/%{name}/colorscripts/print256
%{_libdir}/%{name}/colorscripts/pukeskull
%{_libdir}/%{name}/colorscripts/rails
%{_libdir}/%{name}/colorscripts/rally-x
%{_libdir}/%{name}/colorscripts/rupees
%{_libdir}/%{name}/colorscripts/six
%{_libdir}/%{name}/colorscripts/space-invaders
%{_libdir}/%{name}/colorscripts/spectrum
%{_libdir}/%{name}/colorscripts/square
%{_libdir}/%{name}/colorscripts/suckless
%{_libdir}/%{name}/colorscripts/tanks
%{_libdir}/%{name}/colorscripts/thebat
%{_libdir}/%{name}/colorscripts/thebat2
%{_libdir}/%{name}/colorscripts/tiefighter1
%{_libdir}/%{name}/colorscripts/tiefighter1-no-invo
%{_libdir}/%{name}/colorscripts/tiefighter1row
%{_libdir}/%{name}/colorscripts/tiefighter2
%{_libdir}/%{name}/colorscripts/tux
%{_libdir}/%{name}/colorscripts/xmonad
%{_libdir}/%{name}/colorscripts/zwaves
%{_bindir}/colorscript
%{_mandir}/man1/colorscript.1*

%changelog
* Sat Dec 24 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
* Reduced the number of comments in the %prep section of the specfile.

* Thu Dec 22 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
* Changes made to the specfile to suit the Fedora Packaging Guidelines.

* Wed Dec 21 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
* Changes made to the specfile to suit the Fedora Packaging Guidelines.

* Thu Dec 15 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
- First version being packaged.
