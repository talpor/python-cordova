# -*- coding: utf-8 -*-
from __future__ import absolute_import
__version__ = '0.1'

import os
import subprocess

from .decorators import for_all_methods, chdir_context


BUILD_LOCATION = {
    'android': {
        'debug': 'platforms/android/ant-build/%s-debug.apk',
        'release': 'platforms/android/ant-build/%s-release-unsigned.apk'
    },
    'ios': {
        'debug': 'platforms/ios/build/emulator/%s.app',
        'release': 'platforms/ios/build/emulator/%s.app',
    }
}


@for_all_methods(chdir_context)
class App(object):
    path = None
    name = None

    # We need to initialize the application with the path of the root
    # of the project
    def __init__(self, path, name, *args, **kwargs):
        self.path = path
        self.name = name
        super(App, self).__init__(*args, **kwargs)

    def __platform_list(self):
        platform_ls_output = subprocess.check_output([
            'cordova', 'platform', 'ls'
        ]).splitlines()

        installed = re.findall(r'[,:]\s(\w+)\s\d+', platform_ls_output[0])
        available = re.findall(r'[,:]\s(\w+)\s', platform_ls_output[1])

        return (installed, available)

    def installed_platform_list(self):
        return self.__platform_list()[0]

    def available_platform_list(self):
        return self.__platform_list()[1]

    def add_platform(self, platform):
        return_code = subprocess.call([
            'cordova', 'platform', 'add', platform
        ])

        if return_code == 0:
            return True
        else:
            return False

    def remove_platform(self, platform):
        return_code = subprocess.call([
            'cordova', 'platform', 'remove', platform
        ])

        if return_code == 0:
            return True
        else:
            return False

    def archive(self, platform):
        os.chdir('platforms')
        return_code = subprocess.call([
            'tar', '-czf',
            '%s-%s.zip' % (
                self.name, platform
            ), platform
        ])

        if return_code == 0:
            return '%s/%s-%s.zip' % (
                os.getcwd(), self.name, platform
            )
        else:
            return False

    def build(self, platform=None, release=False):
        release_flag = ''
        platform_flag = platform or ''
        if release:
            release_flag = '--release'

        return_code = subprocess.call([
            'cordova', 'build', platform_flag, release_flag
        ])

        if return_code == 0:
            if platform:
                return os.path.join(
                    path,
                    BUILD_LOCATION[platform]
                    ['release' if release else 'debug'] % (
                        self.name
                    )
                )
            else:
                return True
        else:
            return False

    def prepare(self, platform):
        return_code = subprocess.call([
            'cordova', 'prepare', platform
        ])

        if return_code == 0:
            return True
        else:
            return False

    def compile(self, platform):
        return_code = subprocess.call([
            'cordova', 'compile', platform
        ])

        if return_code == 0:
            return True
        else:
            return False
