# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function
from cryptography.exceptions import UnsupportedAlgorithm, _Reasons
from cryptography.hazmat.backends.interfaces import QTESLABackend

import abc

import six


@six.add_metaclass(abc.ABCMeta)
class QTESLA(object):
    @abc.abstractmethod
    def keypair(self):
        """
        Generate public and private keys
        """

    @abc.abstractmethod
    def sign(self, signature, signature_len, message, message_len, private_key):
        """
        Sign the data
        """

    @abc.abstractmethod
    def verify(self, message, message_len, signature, signature_len, public_key):
        """
        Verify the signature
        """


def generate_keypair(backend):
    if not isinstance(backend, QTESLABackend):
        raise UnsupportedAlgorithm(
            "Backend object does not implement QTESLABackend.",
            _Reasons.BACKEND_MISSING_INTERFACE
        )

    return backend.generate_qtesla_keypair()
