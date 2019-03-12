# Help on class AttrConstClass in module gurobipy:

class AttrConstClass():
    """
    Attributes are used throughout the Gurobi interface to query and
    modify model properties.  You refer to them as you would any
    other object attribute.  For example, "print model.numConstrs"
    prints the number of constraints in a model.  You can assign new values to
    some attributes (e.g., model.ModelName = "New"), while others can only
    be queried.  Note that attribute modification is handled in a lazy fashion,
    so you won't see the effect of a change until after the next call to
    Model.update() or Model.optimize().

    Capitalization is ignored in Gurobi attribute names, so
    model.numConstrs and model.NumConstrs are equivalent.

    Gurobi attributes can be grouped into the following categories:

    General model attributes (e.g., model.numConstrs):

      numConstrs: Number of constraints
      numVars: Number of variables
      numSOS: Number of SOS constraints
      numQConstrs: Number of quadrtic constraints
      numGenConstrs: Number of general constraints
      numNZs: Number of non-zero coefficients
      numQNZs: Number of non-zero quadratic objective coefficients
      numIntVars: Number of integer variables (including binary variables)
      numBinVars: Number of binary variables
      modelName: Model name
      modelSense: Model sense: minimization (1) or maximization (-1)
      objCon: Constant offset for objective function
      objVal: Objective value for current solution
      objBound: Best available lower bound on solution objective
      poolObjBound: Bound on objective for undiscovered solutions
      poolObjVal: Retrieve the objective value of an alternate MIP solution
      MIPGap: Current relative MIP optimality gap
      runtime: Runtime (in seconds) for most recent optimization
      status: Current status of model (help(GRB) gives a list of codes)
      solCount: Number of stored solutions
      iterCount: Number of simplex iterations performed
      nodeCount: Number of branch-and-cut nodes explored
      barIterCount: Number of barrier iterations performed
      isMIP: Indicates whether the model is MIP (1) or not (0)
      isQP: Indicates whether the model has a quadratic objective
      isQCP: Indicates whether the model has quadratic constraints
      isMultiObj: Indicates whether the model has multiple objectives
      IISMinimal: Is computed IIS minimal?
      kappa: Condition number of current LP basis
      maxCoeff: Maximum constraint coefficient (in absolute value)
      minCoeff: Minimum non-zero constraint coefficient (in absolute value)
      maxBound: Maximum finite variable bound (in absolute value)
      minBound: Minimum non-zero variable bound (in absolute value)
      maxObjCoeff: Maximum objective coefficient (in absolute value)
      minObjCoeff: Minimum objective coefficient (in absolute value)
      maxRHS: Maximum linear constraint right-hand side (in absolute value)
      minRHS: Minimum linear constraint right-hand side (in absolute value)
      maxQCRHS: Maximum quadratic constraint right-hand side (in absolute value)
      minQCRHS: Minimum quadratic constraint right-hand side (in absolute value)
      maxQCCoeff: Maximum quadratic constraint coefficient in quadratic part (in absolute value)
      minQCCoeff: Minimum non-zero quadratic constraint coefficient in quadratic part (in absolute value)
      maxQCLCoeff: Maximum quadratic constraint coefficient in linear part (in absolute value)
      minQCLCoeff: Minimum non-zero quadratic constraint coefficient in linear part (in absolute value)
      maxQObjCoeff: Maximum quadratic objective coefficient (in absolute value)
      minQObjCoeff: Minimum quadratic objective coefficient (in absolute value)
      farkasProof: Infeasible amount for Farkas proof for infeasible models
      numStart: number of MIP starts

    Variable attributes (e.g., var.lb):

      lb: Lower bound
      ub: Upper bound
      obj: Objective coefficient
      vType: Variable type (GRB.CONTINUOUS, GRB.BINARY, GRB.INTEGER,
                            GRB.SEMICONT, or GRB.SEMIINT)
      varName: Variable name
      x: Solution value
      rc: Reduced cost
      xn: Solution value in alternate MIP solution
      start: Start vector (use GRB.UNDEFINED to leave a value unspecified)
      vBasis: Basis status
      varHintVal: Variable hint value
      varHintPri: Variable hint priority
      branchPriority: Variable branch priority
      partition: Variable partition
      IISLB: Does LB participate in IIS? (for infeasible models)
      IISUB: Does UB participate in IIS? (for infeasible models)
      SAObjLow: Smallest objective coefficient for which basis remains optimal
      SAObjUp: Largest objective coefficient for which basis remains optimal
      SALBLow: Smallest lower bound for which basis remains optimal
      SALBUp: Largest lower bound for which basis remains optimal
      SAUBLow: Smallest upper bound for which basis remains optimal
      SAUBUp: Largest upper bound for which basis remains optimal
      unbdRay: Unbounded ray
      pStart: Primal solution (for warm-starting simplex)
      preFixVal: The value of the variable (for variables fixed by presolve)
      varPreStat: Status of variable in presolved model

    Constraint attributes (e.g., constr.sense):

      sense: Constraint sense
      rhs: Constraint right-hand side value
      constrName: Constraint name
      pi: Dual value
      slack: Constraint slack
      cBasis: Basis status
      lazy: Lazy constraint flag
      IISConstr: Does constraint participate in IIS? (for infeasible models)
      SARHSLow: Smallest RHS value for which basis remains optimal
      SARHSUp: Largest RHS value for which basis remains optimal
      farkasDual: Farkas dual for infeasible models
      dStart: Dual solution (for warm-starting simplex)

    SOS (e.g., sos.IISSOS):

      IISSOS: Does SOS participate in IIS? (for infeasible models)

    Quadratic constraint attributes (e.g., qc.sense):

      QCsense: Quadratic constraint sense
      QCrhs: Quadratic constraint right-hand side value
      QCname: Quadratic constraint name
      IISQConstr: Does QC participate in IIS? (for infeasible models)
      QCpi: Dual value
      QCslack: Quadratic constraint slack

    GenConstr (e.g., genconstr.IISGenConstr):

      GenConstrType: General constraint type (e.g., GRB.GENCONSTR_MAX)
      GenConstrName: General constraint name
      IISGenConstr: Does general constraint participate in IIS? (for infeasible models)

    Solution quality (e.g., model.constrVio):

      You generally access quality information through Model.printQuality().
      Please refer to the Attributes section of the Gurobi Reference Manual for
      the full list of quality attributes.

    Multi-objectives

      ObjN: objectives of multi-objectives
      ObjNCon: constant terms of multi-objectives
      ObjNPriority: priorities of multi-objectives
      ObjNWeight: weights of multi-objectives
      ObjNRelTol: relative tolerances of multi-objectives
      ObjNAbsTol: absolute tolerances of multi-objectives
      ObjNVal: objective value for multi-objectives
      ObjNName: names of multi-objectives
      NumObj: number of multi-objectives

    Methods defined here:

    __setattr__(self, name, value)

    ----------------------------------------------------------------------
    Data descriptors defined here:

    __dict__
        dictionary for instance variables (if defined)

    __weakref__
        list of weak references to the object (if defined)

    ----------------------------------------------------------------------
    Data and other attributes defined here:
    """


    BarIterCount = 'BarIterCount'

    BarX = 'BarX'

    BoundSVio = 'BoundSVio'

    BoundSVioIndex = 'BoundSVioIndex'

    BoundSVioSum = 'BoundSVioSum'

    BoundVio = 'BoundVio'

    BoundVioIndex = 'BoundVioIndex'

    BoundVioSum = 'BoundVioSum'

    BranchPriority = 'BranchPriority'

    CBasis = 'CBasis'

    ComplVio = 'ComplVio'

    ComplVioIndex = 'ComplVioIndex'

    ComplVioSum = 'ComplVioSum'

    ConstrName = 'ConstrName'

    ConstrResidual = 'ConstrResidual'

    ConstrResidualIndex = 'ConstrResidualIndex'

    ConstrResidualSum = 'ConstrResidualSum'

    ConstrSResidual = 'ConstrSResidual'

    ConstrSResidualIndex = 'ConstrSResidualIndex'

    ConstrSResidualSum = 'ConstrSResidualSum'

    ConstrSVio = 'ConstrSVio'

    ConstrSVioIndex = 'ConstrSVioIndex'

    ConstrSVioSum = 'ConstrSVioSum'

    ConstrVio = 'ConstrVio'

    ConstrVioIndex = 'ConstrVioIndex'

    ConstrVioSum = 'ConstrVioSum'

    DStart = 'DStart'

    DualResidual = 'DualResidual'

    DualResidualIndex = 'DualResidualIndex'

    DualResidualSum = 'DualResidualSum'

    DualSResidual = 'DualSResidual'

    DualSResidualIndex = 'DualSResidualIndex'

    DualSResidualSum = 'DualSResidualSum'

    DualSVio = 'DualSVio'

    DualSVioIndex = 'DualSVioIndex'

    DualSVioSum = 'DualSVioSum'

    DualVio = 'DualVio'

    DualVioIndex = 'DualVioIndex'

    DualVioSum = 'DualVioSum'

    FarkasDual = 'FarkasDual'

    FarkasProof = 'FarkasProof'

    GenConstrName = 'GenConstrName'

    GenConstrType = 'GenConstrType'

    IISConstr = 'IISConstr'

    IISGenConstr = 'IISGenConstr'

    IISLB = 'IISLB'

    IISMinimal = 'IISMinimal'

    IISQConstr = 'IISQConstr'

    IISSOS = 'IISSOS'

    IISUB = 'IISUB'

    IntVio = 'IntVio'

    IntVioIndex = 'IntVioIndex'

    IntVioSum = 'IntVioSum'

    IsMIP = 'IsMIP'

    IsMultiObj = 'IsMultiObj'

    IsQCP = 'IsQCP'

    IsQP = 'IsQP'

    IterCount = 'IterCount'

    JobID = 'JobID'

    Kappa = 'Kappa'

    KappaExact = 'KappaExact'

    LB = 'LB'

    Lazy = 'Lazy'

    LicenseExpiration = 'LicenseExpiration'

    MIPGap = 'MIPGap'

    MaxBound = 'MaxBound'

    MaxCoeff = 'MaxCoeff'

    MaxObjCoeff = 'MaxObjCoeff'

    MaxQCCoeff = 'MaxQCCoeff'

    MaxQCLCoeff = 'MaxQCLCoeff'

    MaxQCRHS = 'MaxQCRHS'

    MaxQObjCoeff = 'MaxQObjCoeff'

    MaxRHS = 'MaxRHS'

    MinBound = 'MinBound'

    MinCoeff = 'MinCoeff'

    MinObjCoeff = 'MinObjCoeff'

    MinQCCoeff = 'MinQCCoeff'

    MinQCLCoeff = 'MinQCLCoeff'

    MinQCRHS = 'MinQCRHS'

    MinQObjCoeff = 'MinQObjCoeff'

    MinRHS = 'MinRHS'

    ModelName = 'ModelName'

    ModelSense = 'ModelSense'

    NodeCount = 'NodeCount'

    NumBinVars = 'NumBinVars'

    NumConstrs = 'NumConstrs'

    NumGenConstrs = 'NumGenConstrs'

    NumIntVars = 'NumIntVars'

    NumNZs = 'NumNZs'

    NumObj = 'NumObj'

    NumPWLObjVars = 'NumPWLObjVars'

    NumQCNZs = 'NumQCNZs'

    NumQConstrs = 'NumQConstrs'

    NumQNZs = 'NumQNZs'

    NumSOS = 'NumSOS'

    NumStart = 'NumStart'

    NumVars = 'NumVars'

    Obj = 'Obj'

    ObjBound = 'ObjBound'

    ObjBoundC = 'ObjBoundC'

    ObjCon = 'ObjCon'

    ObjN = 'ObjN'

    ObjNAbsTol = 'ObjNAbsTol'

    ObjNCon = 'ObjNCon'

    ObjNName = 'ObjNName'

    ObjNPriority = 'ObjNPriority'

    ObjNRelTol = 'ObjNRelTol'

    ObjNVal = 'ObjNVal'

    ObjNWeight = 'ObjNWeight'

    ObjVal = 'ObjVal'

    PStart = 'PStart'

    PWLObjCvx = 'PWLObjCvx'

    Partition = 'Partition'

    Pi = 'Pi'

    PoolObjBound = 'PoolObjBound'

    PoolObjVal = 'PoolObjVal'

    PreFixVal = 'PreFixVal'

    QCName = 'QCName'

    QCPi = 'QCPi'

    QCRHS = 'QCRHS'

    QCSense = 'QCSense'

    QCSlack = 'QCSlack'

    RC = 'RC'

    RHS = 'RHS'

    Runtime = 'Runtime'

    SALBLow = 'SALBLow'

    SALBUp = 'SALBUp'

    SAObjLow = 'SAObjLow'

    SAObjUp = 'SAObjUp'

    SARHSLow = 'SARHSLow'

    SARHSUp = 'SARHSUp'

    SAUBLow = 'SAUBLow'

    SAUBUp = 'SAUBUp'

    Sense = 'Sense'

    Server = 'Server'

    Slack = 'Slack'

    SolCount = 'SolCount'

    Start = 'Start'

    Status = 'Status'

    TuneResultCount = 'TuneResultCount'

    UB = 'UB'

    UnbdRay = 'UnbdRay'

    VBasis = 'VBasis'

    VType = 'VType'

    VarHintPri = 'VarHintPri'

    VarHintVal = 'VarHintVal'

    VarName = 'VarName'

    VarPreStat = 'VarPreStat'

    X = 'X'

    Xn = 'Xn'