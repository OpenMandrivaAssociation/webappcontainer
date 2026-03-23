Name:           webappcontainer
Release:        1
Version:        1.4.2
Summary:        Open any web app in a single, lightweight, portable application with a tray icon
Group:          Internet
License:        GPL-2.0
URL:            https://github.com/josephcrowell/webappcontainer

Source0:        %url/archive/%version/%name-%version.tar.gz

BuildSystem:    cmake

BuildOption:    -DENABLE_WIDEVINE=OFF

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(VulkanHeaders)
BuildRequires:  pkgconfig(libpsl)

Suggests:       widevine-installer

%description
A lightweight, persistent web container built with C++20 and Qt 6.9+. 
This application allows you to run web applications as standalone 
desktop apps with isolated profiles, custom icons, and system tray 
integration. It's a nice alternative to Electron or running web apps 
from Chrome/Chromium/Brave/Edge.

%files
%license LICENSE
%doc README.md
%{_bindir}/%name

