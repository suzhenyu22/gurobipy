# Help on class Env in module gurobipy:

class Env():
    """
	Env(logfilename='', empty=False, cenv=None, isDefault=False)

    Gurobi environment object.  Methods on this object are:
      readParams(paramname): Read a set of parameter settings from a file.
      resetParams(): Reset all parameters to their default values.
      setParam(paramname, newval): Set a parameter to a new value.
      writeParams(paramname): Write the current parameter settings to a file.

    Additional help can be obtained on any of these methods (e.g.,
    help(Env.setParam)).  A list of all available parameters can be
    obtained by typing 'help(GRB.param)'.

    Methods defined here:
    """

    def __init__(self, logfilename='', empty=False, cenv=None, isDefault=False):
        pass

    def __repr__(self):
        pass

    def __del__(self):
        pass

    def dispose(self):
        pass

    def readParams(self, filename):
        """
        ROUTINE:
          readParams(filename)

        PURPOSE:
          Read a set of parameter settings from a file.

        ARGUMENTS:
          filename (string): A path to a file containing a list of parameter
                             settings.

        RETURN VALUE:
          None.

        EXAMPLE:
          env.readParams('gurobi.prm')

        NOTES:
          This routine should normally be called on the default environment or on
          a model object.

          The parameter file should contain "name value" pairs, each on its own
          line.  A hash symbol at the beginning of a line indicates that the line
          should be ignored.  Here is an example of a valid parameter file:

            # List of changed parameters
            TimeLimit      100
            IterationLimit 1000
        """
        pass

    def resetParams(self):
        """
        ROUTINE:
          resetParams()

        PURPOSE:
          Reset all parameters to their default values.

        ARGUMENTS:
          None.

        RETURN VALUE:
          None.

        EXAMPLE:
          env.resetParams()

        NOTES:
          This routine should normally be called on the default environment or on
          a model object.
        """
        pass

    def setParam(self, paramname, newval, verbose=True):
        """
        ROUTINE:
          setParam(paramname, newvalue)

        PURPOSE:
          Set a parameter to a new value.

        ARGUMENTS:
          paramname (string): The name of the parameter.
          newvalue: The desired new value.  The type of the value should be
                    compatible with the parameter type (e.g., an integer parameter
                    will take an integer value).  One important exception: the
                    string "default" will return the specified parameter to its
                    default value.

        RETURN VALUE:
          None.

        EXAMPLE:
          env.setParam("NodeLimit", 100)
          env.setParam("TimeLimit", "default")

        NOTES:
          Use this routine to change parameter values in the default environment.
          The default environment is used to initialize parameter values when a
          new model is created.  Once the model exists, changes to the default
          environment will no longer affect that model.  Use Model.setParam()
          to change parameter settings for an existing model.

          Routine paramHelp() provides additional information on the available
          parameters.
        """
        pass

    def start(self):
        pass

    def writeParams(self, filename):
        """
        ROUTINE:
          writeParams(filename)

        PURPOSE:
          Write non-default parameter settings to a file.

        ARGUMENTS:
          filename (string): The name of the file to which non-default parameter
                             settings should be written.

        RETURN VALUE:
          None.

        EXAMPLE:
          env.writeParams('changed.prm')

        NOTES:
          This routine should normally be called on the default environment or on
          a model object.

          Upon completion, the specified file will contain a set of "name value"
          pairs, one per line, that indicates the set of parameters that current
          have non-default values in the specified model.
        """
        pass

    # ----------------------------------------------------------------------
    # Class methods defined here:

    # ClientEnv(logfilename, computeServer, router='', password='', group='', tlsInsecure=0, priority=0, timeout=1e+100) from builtins.type

    # CloudEnv(logfilename, accessID, secretKey, pool='', priority=0) from builtins.type

    # OtherEnv(logfilename, i, a, e, k) from builtins.type

    # ----------------------------------------------------------------------
    # Data descriptors defined here:

    # __dict__
    # dictionary for instance variables (if defined)

    # __weakref__
    # list of weak references to the object (if defined)
