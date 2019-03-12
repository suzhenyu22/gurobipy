# Help on class GurobiError in module gurobipy:

class GurobiError():
    """
    GurobiError(errno, argument)

    Gurobi exception class

    Method resolution order:
        GurobiError
        builtins.Exception
        builtins.BaseException
        builtins.object

    Methods defined here:

    __init__(self, errno, argument)

    __str__(self)

    ----------------------------------------------------------------------
    Data descriptors defined here:

    __weakref__
        list of weak references to the object (if defined)

    message

    ----------------------------------------------------------------------
    Static methods inherited from builtins.Exception:

    __new__(*args, **kwargs) from builtins.type
        Create and return a new object.  See help(type) for accurate signature.

    ----------------------------------------------------------------------
    Methods inherited from builtins.BaseException:

    __delattr__(self, name, /)
        Implement delattr(self, name).

    __getattribute__(self, name, /)
        Return getattr(self, name).

    __reduce__(...)
        Helper for pickle.

    __repr__(self, /)
        Return repr(self).

    __setattr__(self, name, value, /)
        Implement setattr(self, name, value).

    __setstate__(...)

    with_traceback(...)
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.

    ----------------------------------------------------------------------
    Data descriptors inherited from builtins.BaseException:

    __cause__
        exception cause

    __context__
        exception context

    __dict__

    __suppress_context__

    __traceback__

    args
    """
    def __init__(self, errno, argument):
        pass