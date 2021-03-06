"""
test02_interface_errors_job.py

Verify that no errors have been reported on network interfaces in the testbed.

"""
# see https://pubhub.devnetcloud.com/media/pyats/docs/easypy/jobfile.html
# for how job files work

__author__ = "Hank Preston"
__copyright__ = "Copyright (c) 2019, Cisco Systems Inc."
__contact__ = ["hapresto@cisco.com"]
__credits__ = []
__version__ = 1.0

import os
from pyats.easypy import run

# compute the script path from this location
SCRIPT_PATH = os.path.dirname(__file__)


def main(runtime):
    """job file entrypoint"""

    # run script
    run(
        testscript=os.path.join(SCRIPT_PATH, "test02_interface_errors.py"),
        runtime=runtime,
    )
