from gurobipy.Model import Model
from gurobipy.GRB import GRB
from gurobipy.Column import Column
from gurobipy.Constr import Constr

from gurobipy.tupledict import tupledict
from gurobipy.tuplelist import tuplelist
from gurobipy import izip
from gurobipy.gurobi import gurobi
# 下面这些都是系统自带，而不是gurobipy的接口
import dis
import fnmatch
import gc
import glob
import logging
import atexit
import types
import sys
import re
import operator
import numbers
import math
import itertools
import inspect
from collections.abc import Iterable
from io import StringIO  as GRBStringIO


# 下面这些是gurobipy定义的快捷计算函数
def abs_(*args):
    """Return the absolute value of x, or the absolute value general constraint"""
    pass

def all_(*args, **kwargs):
    """Return the general constraint of type all"""
    pass

def and_(*args, **kwargs):
    """Return the general constraint of type and"""
    pass

def any_(*args, **kwargs):
    """Return the general constraint of type or"""
    pass

def paramHelp(paramname):
    """Obtain help on a Gurobi parameter."""
    pass

def quicksum(list):
    """
    A quicker version of the Python built-in 'sum' function for building Gurobi expressions.
    return An expression that represents the sum of the input arguments.
    """
    pass

def disposeDefaultEnv():
    """Release default Gurobi environment."""
    pass

def exprfactory():
    pass

def exprfactory_iter():
    pass

def max_(*args, **kwargs):
    """Return the general constraint of type max"""
    pass

def min_(*args, **kwargs):
    """Return the general constraint of type min"""
    pass

def models():
    """Provide a list of currently loaded models."""
    pass

def multidict(data):
    """
    Split a single dictionary into multiple dictionaries.
    return A list of the shared keys, followed by individual tupledicts.
    EXAMPLE:
           (keys, dict1, dict2) = multidict( {
                    'key1': [1, 2],
                    'key2': [1, 3],
                    'key3': [1, 4] } )
    """
    pass

def or_(*args, **kwargs):
    """Help on cython_function_or_method in module gurobipy:"""
    pass

def read(filename):
    """Read an optimization model from a file. RETURN A Model object."""
    pass

def readParams(filename):
    """Read a set of parameter settings from a file."""
    pass

def writeParams(filename):
    """Write non-default parameter settings to a file."""
    pass

def resetParams():
    """Reset all parameters to their default values."""
    pass

def setParam(paramname, newvalue):
    """Set a parameter to a new value."""
    pass



def system(command):
    """Issue a system shell command."""
    pass


