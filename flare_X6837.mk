#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Flare stuff.
$(call inherit-product, vendor/flare/config/common_full_phone.mk)
$(call inherit-product, vendor/lineage-priv/keys/keys.mk)
FLARE_BUILD_TYPE := UNOFFICIAL
FLARE_MAINTAINER := gabutuniverse!
TARGET_ENABLE_BLUR := true
TARGET_FACE_UNLOCK_SUPPORTED := true
WITH_GAPPS := true

# Inherit from X6837 device
$(call inherit-product, device/infinix/X6837/device.mk)

BOARD_VENDOR := Infinix
PRODUCT_NAME := flare_X6837
PRODUCT_DEVICE := X6837
PRODUCT_MANUFACTURER := INFINIX
PRODUCT_BRAND := Infinix
PRODUCT_MODEL := Infinix X6837

PRODUCT_GMS_CLIENTID_BASE := android-transsion
PRODUCT_SYSTEM_NAME := X6837-OP
PRODUCT_SYSTEM_DEVICE := X6837
    
BUILD_FINGERPRINT := Infinix/X6837-OP/Infinix-X6837:13/TP1A.220624.014/240929V1624:user/release-keys