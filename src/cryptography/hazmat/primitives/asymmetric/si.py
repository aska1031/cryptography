# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

import abc

import six


@six.add_metaclass(abc.ABCMeta)
class SIDH(object):
    @abc.abstractmethod
    def keypair(self, pub, pri):
        """
        Generate public and private keys
        """

    @abc.abstractmethod
    def encap(self, cipher_text, shared_secret, public_key):
        """
        Sign the data
        """

    @abc.abstractmethod
    def decap(self, shared_secret, cipher_text, secret_key):
        """
        Verify the signature
        """
