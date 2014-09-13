# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from rcon import RCON, NoResponseError

SERVER_ADDR = ('54.207.65.230', 28016)
SERVER_PASSWD = '3840'
COMMANDS = {'airdrop.drop': 'chamou o aviaozinho',
            'kick': 'chutou {0}'}


def rust(command, user, target_name=''):
    key = command
    if command in COMMANDS.keys():
        with RCON(SERVER_ADDR, SERVER_PASSWD, timeout=2) as rcon:
            if target_name:
                command = '{0} {1}'.format(command, target_name)

            try:
                rcon(command)
            except NoResponseError:
                pass

            message = 'Moderador {0} {1}'.format(
                user, COMMANDS[key].format(target_name))
            try:
                rcon('notice.popupall "{0}"'.format(message))
            except NoResponseError:
                pass
