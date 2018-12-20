# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.
from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <oqs/common.h>
"""

TYPES = """
"""

FUNCTIONS = """
void OQS_MEM_cleanse(void *, size_t);
void OQS_MEM_secure_free(void *, size_t);
void OQS_MEM_insecure_free(void *ptr);
"""

CUSTOMIZATIONS = """
"""
