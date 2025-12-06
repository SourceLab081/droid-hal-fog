%define device fog
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi 10C

%define droid_target_aarch64 1

%define rpm_vendor qualcomm

%define installable_zip 1

%define enable_kernel_update 1
%define enable_dtbo_update 1
%define enable_vendor_boot_update 1

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define makefstab_skip_entries / /product /system /system_ext /vendor /odm

%define straggler_files \
/bugreports\
/cache\
/d\
/sdcard\
%{nil}

BuildRequires:  python3-base

%include rpm/dhd/droid-hal-device.inc

