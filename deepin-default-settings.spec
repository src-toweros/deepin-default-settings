%bcond_with check
%global _unpackaged_files_terminate_build 0 
%global debug_package   %{nil}
%global common_description %{expand:default settings for deepin destkop environment
 This package does tweaking and to provide better experience of deepin desktop
 environment.}

Name:          deepin-default-settings
Version:       2020.03.25
Release:       2
Summary:       This library is designed to be exception-free and avoid Qt application developer do direct access to glib/glibmm
License:       GPLv3
URL:           https://uos-packages.deepin.com/uos/pool/main/d/deepin-default-settings/
Source0:       https://uos-packages.deepin.com/uos/pool/main/d/%{name}/%{name}_%{version}.orig.tar.xz
BuildRequires:	   dde-desktop

%description
%{common_description}

%prep
%setup

%build
make
%install
%make_install
install -d %{buildroot}%{_sysconfdir}/skel/{Desktop,Documents,Downloads,Pictures,Videos}
install -Dm644 %{_datadir}/applications/dde-computer.desktop %{buildroot}%{_sysconfdir}/skel/Desktop/dde-computer.desktop
install -Dm755 %{_datadir}/applications/dde-trash.desktop %{buildroot}%{_sysconfdir}/skel/Desktop/dde-trash.desktop

%post
for i in $(getent passwd | grep -v nologin | grep -v halt | grep -v shutdown | grep -v sync); do
  userid=$(echo "$i" | awk -F ':' '{print $3}')
  groupid=$(echo "$i" | awk -F ':' '{print $4}')
  userhome=$(echo "$i" | awk -F ':' '{print $6}')
  if [ ! -f /"${userhome}"/Desktop/dde-computer.desktop ] && [ ! -f /"${userhome}"/Desktop/dde-trash.desktop ]; then
    install -o "${userid}" -g "${groupid}" -Dm644 /etc/skel/.config/user-dirs.dirs /"${userhome}"/.config/user-dirs.dirs || true
    install -o "${userid}" -g "${groupid}" -d /"${userhome}"/{Desktop,Documents,Downloads,Pictures,Pictures/Wallpapers,Music,Videos,.Public,.Templates} || true
    install -o "${userid}" -g "${groupid}" -Dm644 /etc/skel/.config/autostart/dde-first-run.desktop /"${userhome}"/.config/autostart/dde-first-run.desktop || true
    chown -R "${userid}":"${groupid}" "${userhome}"
  fi
done

%files
%{_sysconfdir}/apt
%{_sysconfdir}/X11/xorg.conf.d/50-synaptics.conf
%{_sysconfdir}/X11/xorg.conf.d/75-wacom.conf
%{_sysconfdir}/binfmt.d/wine.conf
%{_sysconfdir}/fonts/conf.d/10-enhance-rending.conf
%{_sysconfdir}/fonts/conf.d/55-language-deepin-zh-cn.conf
%{_sysconfdir}/fonts/conf.d/55-language-deepin-zh-hk.conf
%{_sysconfdir}/fonts/conf.d/55-language-deepin-zh-tw.conf
%{_sysconfdir}/gimp/2.0/fonts.conf
%{_sysconfdir}/lscolor-256color
%{_sysconfdir}/modprobe.d/iwlwifi.conf
%{_sysconfdir}/skel/.config/SogouPY/sogouEnv.ini
%{_sysconfdir}/skel/.config/Trolltech.conf
%{_sysconfdir}/skel/.config/autostart/dde-first-run.desktop
%{_sysconfdir}/skel/.config/deepin/qt-theme.ini
%{_sysconfdir}/skel/.config/user-dirs.dirs
%{_sysconfdir}/skel/.icons/default/index.theme
%{_sysconfdir}/skel/Music/bensound-sunny.mp3
%{_sysconfdir}/skel/*
%{_sysconfdir}/sudoers.d/01_always_set_sudoers_home
/lib/udev/rules.d/99-deepin.rules
%{_bindir}/dde-first-run
/usr/lib/sysctl.d/deepin.conf
%{_datadir}/applications/deepin/dde-mimetype.list
%{_datadir}/deepin-default-settings/fontconfig.json
%{_datadir}/fontconfig/conf.avail/10-enhance-rending.conf
%{_datadir}/fontconfig/conf.avail/55-language-deepin-zh-cn.conf
%{_datadir}/fontconfig/conf.avail/55-language-deepin-zh-hk.conf
%{_datadir}/fontconfig/conf.avail/55-language-deepin-zh-tw.conf
%{_datadir}/mime/packages/deepin-workaround.xml
%{_datadir}/mime/wine-ini.xml
%{_datadir}/music/bensound-sunny.mp3
%license LICENSE

%changelog
* Wed Dec 16 2020 weidong <weidong@uniontech.com> - 2020.03.25-2
- Update user desktop

* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> - 2020.03.25-1
- Project init.
