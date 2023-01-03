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
%{_libexecdir}/%{name}/colorscripts/00default.sh
%{_libexecdir}/%{name}/colorscripts/alpha
%{_libexecdir}/%{name}/colorscripts/arch
%{_libexecdir}/%{name}/colorscripts/awk-rgb-test
%{_libexecdir}/%{name}/colorscripts/bars
%{_libexecdir}/%{name}/colorscripts/blocks1
%{_libexecdir}/%{name}/colorscripts/blocks2
%{_libexecdir}/%{name}/colorscripts/bloks
%{_libexecdir}/%{name}/colorscripts/colorbars
%{_libexecdir}/%{name}/colorscripts/colortest
%{_libexecdir}/%{name}/colorscripts/colortest-slim
%{_libexecdir}/%{name}/colorscripts/colorview
%{_libexecdir}/%{name}/colorscripts/colorwheel
%{_libexecdir}/%{name}/colorscripts/crowns
%{_libexecdir}/%{name}/colorscripts/crunch
%{_libexecdir}/%{name}/colorscripts/crunchbang
%{_libexecdir}/%{name}/colorscripts/crunchbang-mini
%{_libexecdir}/%{name}/colorscripts/darthvader
%{_libexecdir}/%{name}/colorscripts/debian
%{_libexecdir}/%{name}/colorscripts/dna
%{_libexecdir}/%{name}/colorscripts/doom-original
%{_libexecdir}/%{name}/colorscripts/doom-outlined
%{_libexecdir}/%{name}/colorscripts/elfman
%{_libexecdir}/%{name}/colorscripts/faces
%{_libexecdir}/%{name}/colorscripts/fade
%{_libexecdir}/%{name}/colorscripts/ghosts
%{_libexecdir}/%{name}/colorscripts/guns
%{_libexecdir}/%{name}/colorscripts/hex
%{_libexecdir}/%{name}/colorscripts/illumina
%{_libexecdir}/%{name}/colorscripts/jangofett
%{_libexecdir}/%{name}/colorscripts/kaisen
%{_libexecdir}/%{name}/colorscripts/manjaro
%{_libexecdir}/%{name}/colorscripts/monster
%{_libexecdir}/%{name}/colorscripts/mouseface
%{_libexecdir}/%{name}/colorscripts/mouseface2
%{_libexecdir}/%{name}/colorscripts/pacman
%{_libexecdir}/%{name}/colorscripts/panes
%{_libexecdir}/%{name}/colorscripts/pinguco
%{_libexecdir}/%{name}/colorscripts/print256
%{_libexecdir}/%{name}/colorscripts/pukeskull
%{_libexecdir}/%{name}/colorscripts/rails
%{_libexecdir}/%{name}/colorscripts/rally-x
%{_libexecdir}/%{name}/colorscripts/rupees
%{_libexecdir}/%{name}/colorscripts/six
%{_libexecdir}/%{name}/colorscripts/space-invaders
%{_libexecdir}/%{name}/colorscripts/spectrum
%{_libexecdir}/%{name}/colorscripts/square
%{_libexecdir}/%{name}/colorscripts/suckless
%{_libexecdir}/%{name}/colorscripts/tanks
%{_libexecdir}/%{name}/colorscripts/thebat
%{_libexecdir}/%{name}/colorscripts/thebat2
%{_libexecdir}/%{name}/colorscripts/tiefighter1
%{_libexecdir}/%{name}/colorscripts/tiefighter1-no-invo
%{_libexecdir}/%{name}/colorscripts/tiefighter1row
%{_libexecdir}/%{name}/colorscripts/tiefighter2
%{_libexecdir}/%{name}/colorscripts/tux
%{_libexecdir}/%{name}/colorscripts/xmonad
%{_libexecdir}/%{name}/colorscripts/zwaves
%{_bindir}/colorscript
%{_mandir}/man1/colorscript.1*

%changelog
* Tue Jan 03 2023 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
- Changed the install section to use the reworked makefile.

* Sat Dec 31 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
- Changed the Source0 parameter to download the source from upstream instead of using a local file.

* Mon Dec 26 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
- Moved the sed fixes to a patch file. Also added a reworked makefile, but it still needs a prefix.

* Sat Dec 24 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
- Reduced the number of comments in the %prep section of the specfile.

* Thu Dec 22 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
- Changes made to the specfile to suit the Fedora Packaging Guidelines.

* Wed Dec 21 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
- Changes made to the specfile to suit the Fedora Packaging Guidelines.

* Thu Dec 15 2022 Lucas <46837214+foopsss@users.noreply.github.com> - 1.1.r96.da2e3c5
- First version being packaged.
