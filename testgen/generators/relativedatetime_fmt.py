# -*- coding: utf-8 -*-
import os
import json
import re
import logging
import subprocess
from generators.base import DataGenerator

reblankline = re.compile("^\s*$")

class RelativeDateTimeFmtGenerator(DataGenerator):
    json_test = {"test_type": "rdt_fmt"}
    json_verify = {"test_type": "rdt_fmt"}

    def process_test_data(self):
        # Use NOde JS to create the .json files
        icu_nvm_versions = {
            'icu75': '22.1.0',
            'icu74': '21.6.0',
            'icu73': '20.1.0',
            'icu72': '18.14.2',
            'icu71': '18.7.0',
        }

        exec_list = ['node generators/rdt_fmt_gen.js']
        if self.run_limit:
            exec_list.append('-run_limit')
            exec_list.append(str(self.run_limit))
            print("RDTF generator: ", exec_list)

        run_list = [
            ['source ~/.nvm/nvm.sh; nvm install 21.6.0; nvm use 21.6.0 --silent'],
            exec_list,
            ['mv rdt_fmt*.json icu74']
        ]

        if self.icu_version not in icu_nvm_versions:
            logging.warning('Generating relative date/time data not configured for icu version %s', self.icu_version)
            return False

        # Set up Node version and call the generator
        nvm_version = icu_nvm_versions[self.icu_version]
        generate_command = 'source ~/.nvm/nvm.sh; nvm install %s; nvm use %s --silent; %s' %\
                           (nvm_version, nvm_version, ' '.join(exec_list))

        logging.debug('Running this command: %s', generate_command)
        result = subprocess.run(generate_command, shell=True)

        # Move results to the right directory
        mv_command = 'mv rdt_fmt*.json %s' % self.icu_version
        result = subprocess.run(mv_command, shell=True)

        return result
