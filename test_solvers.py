#!/usr/bin/env python3
"""Contains routines to test the solvers module"""

import os.path
import pytest
import numpy as np
import solvers
import linsolveio as io


TOLERANCE = 1e-10
TESTDATADIR = 'testdata'

TESTS_SUCCESSFUL = ['simple', 'needs_pivot', 'linearly_dependant']


def _get_test_input(testname):
    "Reads the input for a given test."
    inputfile = os.path.join(TESTDATADIR, testname, 'linsolve.in')
    aa, bb = io.read_input(inputfile)
    return aa, bb


def _get_test_output(testname):
    "Reads the reference ouput for a given test."
    testoutfile = os.path.join(TESTDATADIR, testname, 'linsolve.out.ref')
    result = io.read_result(testoutfile)
    return result


@pytest.mark.parametrize("testname", TESTS_SUCCESSFUL)
def test_elimination(testname):
    "Tests successful elimination."
    aa, bb = _get_test_input(testname)
    xx_expected = _get_test_output(testname)
    xx_gauss = solvers.gaussian_eliminate(aa, bb)
    if xx_expected is None:
        assert xx_gauss is None
    else:
        assert np.all(np.abs(xx_gauss - xx_expected) < TOLERANCE)

