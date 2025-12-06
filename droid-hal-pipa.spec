%define device pipa
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Pad 6

%define droid_target_aarch64 1

%define installable_zip 1

%define enable_kernel_update 1
%define enable_dtbo_update 1
%define enable_vendor_boot_update 1

%define makefstab_skip_entries / /product /system /system_ext /vendor /odm

%define straggler_files \
/bugreports\
/cache\
/d\
/sdcard\
%{nil}

%include rpm/dhd/droid-hal-device.inc

