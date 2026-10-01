# SPDX-FileCopyrightText: Helmholtz-Zentrum Dresden-Rossendorf (HZDR)
#
# SPDX-License-Identifier: Apache-2.0

"""Nox configuration for the hifis.toolkit collection."""

import sys

import nox

try:
    import antsibull_nox
except ImportError:
    print("Install antsibull-nox in the same Python environment as nox.")
    sys.exit(1)

antsibull_nox.load_antsibull_nox_toml()

if __name__ == "__main__":
    nox.main()
