#!/usr/bin/env python

# Copyright (C) 2012, 2013 Jonathan Vasquez <jvasquez1011@gmail.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from subprocess import check_output
from os import getcwd

# Application Info
name = "Bliss Initramfs Creator"
author = "Jonathan Vasquez"
email = "jvasquez1011@gmail.com"
contact = author + " <" + email + ">"
version = "3.0.0"
license = "MPL 2.0"

# Locations
home = getcwd()
temp = home + "/temp"

# Plugins Directory
plugins = home + "/plugins"

# System Directories
bin = "/bin"
sbin = "/sbin"
lib = "/lib"
lib64 = "/lib64"
man = "/usr/share/man"
udev = lib64 + "/udev"
etc = "/etc"

# Directories in /usr
ubin = "/usr/bin"
usbin = "/usr/sbin"
ulib = "/usr/lib"
ushare = "/usr/share"
uexec = "/usr/libexec"

# Paths in Temp (Local)
lbin = temp + bin
lsbin = temp + sbin
llib = temp + lib
llib64 = temp + lib64
lman = temp + man
ludev = temp + udev
letc = temp + etc
lushare = temp + ushare

# CPU Architecture
arch = check_output(["uname", "-m"], universal_newlines=True).strip()

# Preliminary binaries needed for the success of creating the initrd
# but that are not needed to be placed inside the initrd
prel_bin = ["/bin/cpio"]

# Directories to create when generating the initramfs structure
cdirs = [
	lbin, 
	lsbin, 
        temp + "/usr/bin",
        temp + "/proc",
        temp + "/sys",
        temp + "/dev",
        letc,
        temp + "/mnt/root",
        temp + "/lib"]