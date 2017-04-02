#!/usr/bin/env python3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2017 Fabian Ritzmann
#

import logging
import sleekxmpp
from testfixtures import LogCapture
import unittest

from xmppbot import MucBot


class ClientXmppMock(sleekxmpp.ClientXMPP):
    pass 

class TestMucBot(unittest.TestCase):

    def test_muc_message(self):
        with LogCapture('xmppMessages') as logCapture:
            muc_bot = MucBot(ClientXmppMock('testjid', 'testpassword'), 'testroom', 'testnick')
            test_message = {'mucnick': 'testnick', 'body': 'testbody'}
            presence = {'muc': {'nick': 'testnick', 'jid': 'testjid'}}
            muc_bot.muc_presence(presence)
    
            muc_bot.muc_message(test_message)

            logCapture.check(('xmppMessages', 'INFO', '<testjid> testbody'))