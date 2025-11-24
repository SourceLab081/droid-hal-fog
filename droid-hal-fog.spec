# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device fog
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi 10C
%define rpm_device fog

%define enable_kernel_update 1
%define enable_dtbo_update 1

%define installable_zip 1

%define droid_target_aarch64 1

%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define straggler_files \
  /acct \
  /bugreports \
  /cache \
  /d \
  /odm \
  /oem \
  /product \
  /sdcard \
  /storage \
%{nil}

# On Android 8 the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl

# Using droid-system instead of mounting
#%define makefstab_skip_entries /product /system /system_ext /vendor /dev/binderfs /metadata
# Requires: droid-system

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

