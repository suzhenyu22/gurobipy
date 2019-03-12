# Help on class GRB in module gurobipy:
from .ParamConstClass import ParamConstClass
from .AttrConstClass import AttrConstClass
from .CallbackClass import CallbackClass
from .StatusConstClass import StatusConstClass
from .ErrorConstClass import ErrorConstClass


class GRB():
    """
    Gurobi constants.  Constants defined in this class are as follows:

      Basis status (e.g., var.vBasis == GRB.BASIC):

        BASIC: Variable is basic
        NONBASIC_LOWER: Variable is non-basic at lower bound
        NONBASIC_UPPER: Variable is non-basic at upper bound
        SUPERBASIC: Variable is superbasic

      Constraint sense (e.g., constr.sense = GRB.LESS_EQUAL):

        LESS_EQUAL, GREATER_EQUAL, EQUAL

      Variable types (e.g., var.vType = GRB.INTEGER):

        CONTINUOUS, BINARY, INTEGER, SEMICONT, SEMIINT

      SOS types:

        SOS_TYPE1, SOS_TYPE2

      General constraint types:

        GENCONSTR_MAX, GENCONSTR_MIN, GENCONSTR_ABS, GENCONSTR_AND, GENCONSTR_OR, GENCONSTR_INDICATOR

    The GRB class also includes definitions for attributes (GRB.attr),
    errors (GRB.error), parameters (GRB.param), status codes (GRB.status),
    and callbacks (GRB.callback).  You can ask for help on any of these
    (e.g., "help(GRB.attr)").

    Data descriptors defined here:

    __dict__
        dictionary for instance variables (if defined)

    __weakref__
        list of weak references to the object (if defined)

    ----------------------------------------------------------------------
    """

    # Data and other attributes defined here:

    Attr = AttrConstClass()
    BASIC = 0

    BINARY = 'B'

    CONTINUOUS = 'C'

    CUTOFF = 6

    # Callback = <gurobipy.Callback object>
    Callback = CallbackClass()

    DEFAULT_CS_PORT = 61000

    EQUAL = '='

    ERROR_CALLBACK = 10011

    ERROR_CLOUD = 10028

    ERROR_CSWORKER = 10030

    ERROR_DATA_NOT_AVAILABLE = 10005

    ERROR_DUPLICATES = 10018

    ERROR_EXCEED_2B_NONZEROS = 10025

    ERROR_FAILED_TO_CREATE_MODEL = 20002

    ERROR_FILE_READ = 10012

    ERROR_FILE_WRITE = 10013

    ERROR_IIS_NOT_INFEASIBLE = 10015

    ERROR_INDEX_OUT_OF_RANGE = 10006

    ERROR_INTERNAL = 20003

    ERROR_INVALID_ARGUMENT = 10003

    ERROR_INVALID_PIECEWISE_OBJ = 10026

    ERROR_JOB_REJECTED = 10023

    ERROR_MODEL_MODIFICATION = 10029

    ERROR_NETWORK = 10022

    ERROR_NODEFILE = 10019

    ERROR_NOT_FOR_MIP = 10016

    ERROR_NOT_IN_MODEL = 20001

    ERROR_NOT_SUPPORTED = 10024

    ERROR_NO_LICENSE = 10009

    ERROR_NULL_ARGUMENT = 10002

    ERROR_NUMERIC = 10014

    ERROR_OPTIMIZATION_IN_PROGRESS = 10017

    ERROR_OUT_OF_MEMORY = 10001

    ERROR_QCP_EQUALITY_CONSTRAINT = 10021

    ERROR_Q_NOT_PSD = 10020

    ERROR_SIZE_LIMIT_EXCEEDED = 10010

    ERROR_TUNE_MODEL_TYPES = 10031

    ERROR_UNKNOWN_ATTRIBUTE = 10004

    ERROR_UNKNOWN_PARAMETER = 10007

    ERROR_UPDATEMODE_CHANGE = 10027

    ERROR_VALUE_OUT_OF_RANGE = 10008

    # Error = <gurobipy.ErrorConstClass object>
    Error = ErrorConstClass()

    GENCONSTR_ABS = 2

    GENCONSTR_AND = 3

    GENCONSTR_INDICATOR = 5

    GENCONSTR_MAX = 0

    GENCONSTR_MIN = 1

    GENCONSTR_OR = 4

    GREATER_EQUAL = '>'

    INFEASIBLE = 3

    INFINITY = 1e+100

    INF_OR_UNBD = 4

    INPROGRESS = 14

    INTEGER = 'I'

    INTERRUPTED = 11

    ITERATION_LIMIT = 7

    LESS_EQUAL = '<'

    LOADED = 1

    MAXIMIZE = -1

    MINIMIZE = 1

    NODE_LIMIT = 8

    NONBASIC_LOWER = -1

    NONBASIC_UPPER = -2

    NUMERIC = 12

    OPTIMAL = 2

    # Param = <gurobipy.ParamConstClass object>
    Param = ParamConstClass()

    SEMICONT = 'S'

    SEMIINT = 'N'

    SOLUTION_LIMIT = 10

    SOS_TYPE1 = 1

    SOS_TYPE2 = 2

    SUBOPTIMAL = 13

    SUPERBASIC = -3

    # Status = <gurobipy.StatusConstClass object>
    Status = StatusConstClass()

    TIME_LIMIT = 9

    UNBOUNDED = 5

    UNDEFINED = 1e+101

    USER_OBJ_LIMIT = 15

    VERSION_MAJOR = 8

    VERSION_MINOR = 1

    VERSION_TECHNICAL = 0

    # attr = <gurobipy.AttrConstClass object>
    attr = AttrConstClass()

    # callback = <gurobipy.CallbackClass object>
    callback = CallbackClass()

    # error = <gurobipy.ErrorConstClass object>
    error = ErrorConstClass()

    # param = <gurobipy.ParamConstClass object>
    param = ParamConstClass()

    # status = <gurobipy.StatusConstClass object>
    status = StatusConstClass()
