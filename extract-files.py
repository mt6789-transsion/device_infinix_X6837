#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/infinix/X6837',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/transsion',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    ('vendor.mediatek.hardware.videotelephony@1.0',): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),
    ('vendor/bin/hw/mt6789/camerahalserver', 'vendor/lib64/hw/mt6789/android.hardware.camera.provider@2.6-impl-mediatek.so',
     'vendor/lib/hw/mt6789/vendor.mediatek.hardware.pq@2.15-impl.so','vendor/lib64/hw/mt6789/vendor.mediatek.hardware.pq@2.15-impl.so', 'vendor/lib64/hw/mt6789/vendor.mediatek.hardware.camera.isphal@1.0-impl.so', 'vendor/lib64/hw/mt6789/vendor.mediatek.hardware.camera.isphal@1.1-impl.so', 'vendor/bin/hw/vendor.mediatek.hardware.pq@2.2-service'): blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so')
        .replace_needed('libbinder.so', 'libbinder-v32.so')
        .replace_needed('libutils.so', 'libutils-v32.transsion.so'),
    'vendor/lib64/hw/mt6789/android.hardware.camera.provider@2.6-impl-mediatek.so': blob_fixup()
        .add_needed('libshim_camera_metadata.so'),
    ('vendor/lib/libwvhidl.so', 'vendor/lib/mediadrm/libwvdrmengine.so','vendor/lib64/libwvhidl.so', 'vendor/lib64/mediadrm/libwvdrmengine.so'): blob_fixup()
        .replace_needed('libprotobuf-cpp-lite-3.9.1.so', 'libprotobuf-cpp-full-3.9.1.so'),
    'vendor/etc/init/android.hardware.media.c2@1.2-mediatek.rc': blob_fixup()
        .regex_replace('@1.2-mediatek', '@1.2-mediatek-64b'),
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so'),
    ('vendor/bin/mnld', 'vendor/lib64/hw/android.hardware.sensors@2.X-subhal-mediatek.so',
     'vendor/lib64/hw/mt6789/vendor.mediatek.hardware.pq@2.15-impl.so', 'vendor/lib64/mt6789/libaalservice.so',
     'vendor/lib64/mt6789/libcam.utils.sensorprovider.so'): blob_fixup()
        .add_needed('libshim_sensors.so'),
    ('vendor/lib/hw/audio.primary.mediatek.so', 'vendor/lib64/hw/audio.primary.mediatek.so'): blob_fixup()
        .replace_needed('libalsautils.so', 'libalsautils-v32.so')
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so')
        .replace_needed('libbinder.so', 'libbinder-v32.so')
        .add_needed('libstagefright_foundation-v33.so'),
    'vendor/bin/hw/android.hardware.security.keymint-service.trustonic': blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V1-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
        .add_needed('android.hardware.security.rkp-V3-ndk.so'),
    ('system_ext/bin/vtservice', 'system_ext/lib64/libsource.so'): blob_fixup()
        .add_needed('libshim_ui.so'),
    ('system_ext/bin/vtservice', 'system_ext/lib64/libsink.so'): blob_fixup()
        .add_needed('libshim_sink.so'),
    'vendor/etc/init/android.hardware.neuralnetworks-shim-service-mtk.rc': blob_fixup()
        .regex_replace('start', 'enable'),
    ('vendor/lib/libspeech_enh_lib.so', 'vendor/lib/libalsautils-v32.so', 'vendor/lib64/libspeech_enh_lib.so', 'vendor/lib64/libalsautils-v32.so', 'vendor/lib64/libwifi-hal-mtk.so',
     'vendor/lib64/hw/sound_trigger.primary.mt6789.so', 'vendor/lib64/libnir_neon_driver_ndk.mtk.vndk.so'): blob_fixup()
        .fix_soname(),
    'vendor/etc/init/init.thermal_core.rc': blob_fixup()
        .regex_replace('ro.vendor.mtk_thermal_2_0', 'vendor.thermal.link_ready'),
    'vendor/etc/vintf/manifest/manifest_media_c2_V1_2_default.xml': blob_fixup()
        .regex_replace('1.1', '1.2'),
    ('vendor/lib64/mt6789/libneuralnetworks_sl_driver_mtk_prebuilt.so', 'vendor/lib64/ese_spi_nxp.so', 'vendor/lib64/libstfactory-vendor.so',
     'vendor/lib/libnvram.so', 'vendor/lib64/libnvram.so', 'vendor/lib/libsysenv.so', 'vendor/lib64/libsysenv.so',
     'vendor/lib/libtflite_mtk.so', 'vendor/lib64/nfc_nci_nxp.so', 'vendor/lib64/libtflite_mtk.so'): blob_fixup()
        .add_needed('libbase_shim.so'),
    'vendor/lib64/hw/hwcomposer.mtk_common.so': blob_fixup()
        .patchelf_version('0_17_2')
        .add_needed('libprocessgroup_shim.so'),
    ('vendor/lib64/mt6789/lib3a.flash.so', 'vendor/lib64/mt6789/lib3a.ae.stat.so', 'vendor/lib64/mt6789/lib3a.sensors.flicker.so',
     'vendor/lib64/mt6789/lib3a.sensors.color.so', 'vendor/lib64/mt6789/libaaa_ltm.so', 'vendor/lib64/lib3a.ae.pipe.so',
     'vendor/lib64/libSQLiteModule_VER_ALL.so'): blob_fixup()
        .add_needed('liblog.so'),
    'vendor/lib64/mt6789/libmnl.so': blob_fixup()
        .add_needed('libcutils.so'),
    ('vendor/lib64/hw/mt6789/android.hardware.camera.provider@2.6-impl-mediatek.so', 'vendor/lib64/hw/mt6789/vendor.mediatek.hardware.camera.isphal@1.0-impl.so', 'vendor/lib64/hw/mt6789/vendor.mediatek.hardware.camera.isphal@1.1-impl.so'): blob_fixup()
        .add_needed('libutils-shim.so'),
    'vendor/etc/init/android.hardware.graphics.allocator@4.0-service-mediatek.rc': blob_fixup()
        .regex_replace('android.hardware.graphics.allocator@4.0-service-mediatek', 'android.hardware.graphics.allocator@4.0-service-mediatek.mt6789'),
}  # fmt: skip

module = ExtractUtilsModule(
    'X6837',
    'infinix',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()