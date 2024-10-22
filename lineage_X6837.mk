#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common EvolutionX stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)
TARGET_BOOT_ANIMATION_RES := 1080
TARGET_BUILD_APERTURE_CAMERA := true
-include vendor/lineage-priv/keys/keys.mk

# Inherit from X6837 device
$(call inherit-product, device/infinix/X6837/device.mk)

# Device identifier. This must come after all inclusions.
BOARD_VENDOR := Infinix
PRODUCT_NAME := lineage_X6837
PRODUCT_DEVICE := X6837
PRODUCT_MANUFACTURER := INFINIX
PRODUCT_BRAND := Infinix
PRODUCT_MODEL := Infinix X6837

PRODUCT_GMS_CLIENTID_BASE := android-transsion

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRIVATE_BUILD_DESC="sys_tssi_64_armv82_infinix-user 13 TP1A.220624.014 526124 release-keys" \
    PRODUCT_NAME=X6837-OP

BUILD_FINGERPRINT := Infinix/X6837-OP/Infinix-X6837:13/TP1A.220624.014/240313V1154:user/release-keys