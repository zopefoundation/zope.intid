##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Unique id utility views.

$Id$
"""
from zope.security.proxy import removeSecurityProxy
from zope.traversing.api import traverse, getPath


class IntIdsView(object):

    def len(self):
        return len(removeSecurityProxy(self.context).refs)

    def populate(self):
        # TODO: I think this should be moved to the functional test.
        self.context.register(traverse(self.context, "/"))
        self.context.register(traverse(self.context, "/++etc++site"))
        self.request.response.redirect('index.html')

    def _items(self):
        """return all items and their path (for testing only!)"""
        return [(uid, getPath(ref())) for uid, ref in self.context.items()]
