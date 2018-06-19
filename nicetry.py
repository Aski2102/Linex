#!/usr/bin/env python3

import solvers
import linsolveio as lio

(aa, bb) = lio.read_input('testdata/linearly_dependant/linsolve.in')

xx = solvers.gaussian_eliminate(aa, bb)

lio.write_result('Result/result.out', xx)

xx = lio.read_result('Result/result.out')

print(xx)