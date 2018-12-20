# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.
from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <oqs/sig_qtesla.h>
"""

TYPES = """
static const int OQS_SIG_qTESLA_I_length_public_key;
static const int OQS_SIG_qTESLA_I_length_secret_key;
static const int OQS_SIG_qTESLA_I_length_signature;

static const int OQS_SIG_qTESLA_III_size_length_public_key;
static const int OQS_SIG_qTESLA_III_size_length_secret_key;
static const int OQS_SIG_qTESLA_III_size_length_signature;

static const int OQS_SIG_qTESLA_III_speed_length_public_key;
static const int OQS_SIG_qTESLA_III_speed_length_secret_key;
static const int OQS_SIG_qTESLA_III_speed_length_signature;
"""

FUNCTIONS = """
OQS_STATUS OQS_SIG_qTESLA_I_keypair(uint8_t *, uint8_t *);
OQS_STATUS OQS_SIG_qTESLA_I_sign(uint8_t *, size_t *, const uint8_t *, size_t, const uint8_t *);
OQS_STATUS OQS_SIG_qTESLA_I_verify(const uint8_t *, size_t, const uint8_t *, size_t, const uint8_t *);

OQS_STATUS OQS_SIG_qTESLA_III_size_keypair(uint8_t *, uint8_t *);
OQS_STATUS OQS_SIG_qTESLA_III_size_sign(uint8_t *, size_t *, const uint8_t *, size_t, const uint8_t *);
OQS_STATUS OQS_SIG_qTESLA_III_size_verify(const uint8_t *, size_t, const uint8_t *, size_t, const uint8_t *);

OQS_STATUS OQS_SIG_qTESLA_III_speed_keypair(uint8_t *, uint8_t *);
OQS_STATUS OQS_SIG_qTESLA_III_speed_sign(uint8_t *, size_t *, const uint8_t *, size_t, const uint8_t *);
OQS_STATUS OQS_SIG_qTESLA_III_speed_verify(const uint8_t *, size_t, const uint8_t *, size_t, const uint8_t *);

"""

CUSTOMIZATIONS = """
"""
