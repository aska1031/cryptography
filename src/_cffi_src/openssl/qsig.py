# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <oqs/sig.h>
"""

TYPES = """
static const char *OQS_SIG_alg_default;
static const char *OQS_SIG_alg_picnic_L1_FS;
static const char *OQS_SIG_alg_picnic_L1_UR;
static const char *OQS_SIG_alg_picnic_L3_FS;
static const char *OQS_SIG_alg_picnic_L3_UR;
static const char *OQS_SIG_alg_picnic_L5_FS;
static const char *OQS_SIG_alg_picnic_L5_UR;
static const char *OQS_SIG_alg_qTESLA_I;
static const char *OQS_SIG_alg_qTESLA_III_size;
static const char *OQS_SIG_alg_qTESLA_III_speed;
static const int OQS_SIG_algs_length;

typedef enum {
    OQS_ERROR = -1,
    OQS_SUCCESS = 0,
    OQS_EXTERNAL_LIB_ERROR_OPENSSL = 50
} OQS_STATUS;

typedef struct{
    const char *method_name;
    const char *alg_version;
    uint8_t claimed_nist_level;
    bool euf_cma;
    size_t length_public_key;
    size_t length_secret_key;
    size_t length_signature;
    OQS_STATUS (*keypair)(uint8_t *, uint8_t *);
    OQS_STATUS (*sign)(uint8_t *, size_t *, const uint8_t *, size_t, const uint8_t *);
    OQS_STATUS (*verify)(const uint8_t *, size_t, const uint8_t *, size_t, const uint8_t *);
} OQS_SIG;

"""

FUNCTIONS = """
const char *OQS_SIG_alg_identifier(size_t);
OQS_STATUS OQS_SIG_keypair(const OQS_SIG *sig, uint8_t *public_key, uint8_t *secret_key);
OQS_STATUS OQS_SIG_sign(const OQS_SIG *sig, uint8_t *signature, size_t *signature_len, const uint8_t *message, size_t message_len, const uint8_t *secret_key);
OQS_STATUS OQS_SIG_verify(const OQS_SIG *sig, const uint8_t *message, size_t message_len, const uint8_t *signature, size_t signature_len, const uint8_t *public_key);
void OQS_SIG_free(OQS_SIG *sig);
"""

CUSTOMIZATIONS = """
"""
