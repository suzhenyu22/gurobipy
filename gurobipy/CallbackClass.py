# Help on class CallbackClass in module gurobipy:

class CallbackClass():
    """
    CallbackClass(model, function)

    Callbacks are user methods that are called by the Gurobi solver
    during the optimization.  To use a callback, define a method
    that takes two integer arguments (model and where), and pass it
    as the argument to Model.optimize.  Once optimization begins,
    your method will be called with one of the following 'where' values:

    Possible 'where' values (e.g., where == GRB.Callback.MIP) are:

      POLLING:  Regular polling callback - no user queries allowed
      PRESOLVE: In presolve
      SIMPLEX:  In simplex
      BARRIER:  In barrier
      MIP:      In MIP
      MIPSOL:   New MIP incumbent available
      MIPNODE:  MIP node information available
      MULTIOBJ: In multi-objective optimization
      MESSAGE:  Optimizer output a message

    Your method can call Model.cbGet() to obtain detailed information
    on the progress of the optimization.  Allowed values depend
    on 'where'.  The prefix of the 'what' name indicate which
    ones are allowed for each 'where' (so 'PRE_COLDEL' can only
    be called when where == SIMPLEX).

    Allowed 'what' values (e.g., cbGet(GRB.Callback.MIP_OBJBND) are:

      RUNTIME: Elapsed solver runtime
      PRE_COLDEL: Deleted column count
      PRE_ROWDEL: Deleted row count
      PRE_SENCHG: Changed constraint sense count
      PRE_BNDCHG: Bound change count
      SPX_ITRCNT: Iteration count
      SPX_OBJVAL: Primal objective value
      SPX_PRIMINF: Primal infeasibility
      SPX_DUALINF: Dual infeasibility
      SPX_ISPERT: Has model been perturbed?
      BARRIER_ITRCNT: Barrier iteration count
      BARRIER_PRIMOBJ: Barrier iterate primal objective
      BARRIER_DUALOBJ: Barrier iterate dual objective
      BARRIER_PRIMINF: Barrier iterate primal infeasibility
      BARRIER_DUALINF: Barrier iterate dual infeasibility
      BARRIER_COMPL: Barrier iterate complementarity violation
      MIP_OBJBST: Best known objective bound
      MIP_OBJBND: Best known feasible objective
      MIP_NODCNT: Nodes explored so far
      MIP_SOLCNT: Solutions found so far
      MIP_CUTCNT: Cuts added to the model so far
      MIP_NODLFT: Unexplored nodes
      MIP_ITRCNT: Simplex iterations performed so far
      MIPSOL_SOL: Feasible solution (a vector)
      MIPSOL_OBJ: Objective value for feasible solution
      MIPSOL_OBJBST: Best known objective bound
      MIPSOL_OBJBND: Best known feasible objective
      MIPSOL_NODCNT: Node count for feasible solution
      MIPSOL_SOLCNT: Solutions found so far
      MIPNODE_STATUS: Optimization status of node relaxation
      MIPNODE_REL: Node relaxation solution or ray if unbounded
      MIPNODE_OBJBST: Best known objective bound
      MIPNODE_OBJBND: Best known feasible objective
      MIPNODE_NODCNT: Nodes explored so far
      MIPNODE_SOLCNT: Solutions found so far
      MIPNODE_SBRVAR: Node branching variable
      MULTIOBJ_OBJCNT: Objective count optimized so far
      MULTIOBJ_SOLCNT: Solutions found so far
      MULTIOBJ_SOL: Feasible solution (a vector)
      MSG_STRING: Output message

    Your callback method can call other methods on the model object:
      cbCut(), cbGet(), cbGetNodeRel(), cbGetSolution(), cbSetSolution()

    Methods defined here:

    __init__(self, model, function)

    callback(self, model, cbdata, where)

    ----------------------------------------------------------------------
    Data descriptors defined here:

    __dict__
        dictionary for instance variables (if defined)

    __weakref__
        list of weak references to the object (if defined)

    ----------------------------------------------------------------------
    Data and other attributes defined here:
        """

    def __init__(self, model, function):
        pass

    def callback(self, model, cbdata, where):
        pass

    BARRIER = 7

    BARRIER_COMPL = 7006

    BARRIER_DUALINF = 7005

    BARRIER_DUALOBJ = 7003

    BARRIER_ITRCNT = 7001

    BARRIER_PRIMINF = 7004

    BARRIER_PRIMOBJ = 7002

    MESSAGE = 6

    MIP = 3

    MIPNODE = 5

    MIPNODE_BRVAR = 5007

    MIPNODE_NODCNT = 5005

    MIPNODE_OBJBND = 5004

    MIPNODE_OBJBST = 5003

    MIPNODE_REL = 5002

    MIPNODE_SOLCNT = 5006

    MIPNODE_STATUS = 5001

    MIPSOL = 4

    MIPSOL_NODCNT = 4005

    MIPSOL_OBJ = 4002

    MIPSOL_OBJBND = 4004

    MIPSOL_OBJBST = 4003

    MIPSOL_SOL = 4001

    MIPSOL_SOLCNT = 4006

    MIP_CUTCNT = 3004

    MIP_ITRCNT = 3006

    MIP_NODCNT = 3002

    MIP_NODLFT = 3005

    MIP_OBJBND = 3001

    MIP_OBJBST = 3000

    MIP_SOLCNT = 3003

    MSG_STRING = 6001

    MULTIOBJ = 8

    MULTIOBJ_OBJCNT = 8001

    MULTIOBJ_SOL = 8003

    MULTIOBJ_SOLCNT = 8002

    POLLING = 0

    PRESOLVE = 1

    PRE_BNDCHG = 1003

    PRE_COECHG = 1004

    PRE_COLDEL = 1000

    PRE_ROWDEL = 1001

    PRE_SENCHG = 1002

    RUNTIME = 6002

    SIMPLEX = 2

    SPX_DUALINF = 2003

    SPX_ISPERT = 2004

    SPX_ITRCNT = 2000

    SPX_OBJVAL = 2001

    SPX_PRIMINF = 2002