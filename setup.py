# lint as: python3
# Copyright 2021 The Ivy Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License..
# ==============================================================================
from distutils.core import setup
import setuptools

setup(name='ivy-memory',
      version='1.1.3',
      description='End-to-end memory modules for deep learning developers, written in Ivy.\n'
                  'Tested with Ivy 1.1.3',
      author='Ivy Team',
      author_email='ivydl.team@gmail.com',
      packages=setuptools.find_packages(),
      install_requires=['ivy-core', 'ivy-mech', 'ivy-vision'],
      classifiers=['License :: OSI Approved :: Apache Software License'],
      license='Apache 2.0'
      )