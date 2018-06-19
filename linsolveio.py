'''Contains input output routines for the equation solver.'''
import sys
import numpy as np


def read_input(inputfile):
    '''Reads the input for the solver.

    Args:
        inputfile: Name of the input file.

    Returns:
        Tuple (a, b) with the coefficient matrix a and the right hand side
        vector b.
    '''
    try:
        with open(inputfile, 'r') as fp:
            inp = fp.read()
    except OSError as exc:
        print("Failed to read input file '{}'".format(inputfile))
        print("Execption raised: {}".format(exc))
        sys.exit(1)
    aa, bb = _parse_input(inp)
    return aa, bb


def read_result(resultfile):
    '''Reads the result written by the solver (used for testing).

    Args:
        resultfile: Result file to read.

    Returns:
        Result vector x.
    '''
    with open(resultfile, 'r') as fp:
        res = fp.read()
    if res.startswith('ERROR'):
        xx = None
    else:
        numbers = [float(word) for word in res.split()]
        xx = np.array(numbers)
    return xx


def _parse_input(inp):
    lines = [line.strip() for line in inp.split('\n')]
    nvar = int(lines[0])
    aa = np.empty((nvar, nvar), dtype=float)
    for ii in range(nvar):
        aa[ii] = [float(word) for word in lines[ii + 1].split()]
    bb = np.empty((nvar,), dtype=float)
    bb[:] = [float(word) for word in lines[nvar + 1].split()]
    return aa, bb


def write_result(filename, xx):
    '''Writes the result of the solver into a file.

    Args:
        filename: Name of the file where the results should be written to.
        xx: Solution vector or None if the solver could not solve it.
    '''
    if xx is not None:
        numbers = ['{:23.15E}'.format(num) for num in xx]
        line = ' '.join(numbers)
        content = line + '\n'
    else:
        content = 'ERROR: LINDEP\n'
    try:
        with open(filename, 'w') as fp:
            fp.write(content)
    except OSError as exc:
        print("Failed to write result file '{}'".format(filename))
        print("Execption raised: {}".format(exc))
        sys.exit(1)

