from setuptools import setup, find_packages

import conductor
import os

setup(
    name='ansible-container-conductor',
    version=conductor.__version__,
    packages=['conductor', 'container.common'],
    package_dir={'container': os.path.normpath('../..')},
    include_package_data=True,
    url='https://github.com/ansible/ansible-container',
    license='LGPLv3 (See LICENSE file for terms)',
    author='Joshua "jag" Ginsberg, Chris Houseknecht, and others (See AUTHORS file for contributors)',
    author_email='jag@ansible.com',
    description=('Ansible Container empowers you to orchestrate, build, run, and ship '
                 'Docker images built from Ansible playbooks.'),
    entry_points={
        'console_scripts': ['conductor = conductor.cli:commandline']
    }
)
