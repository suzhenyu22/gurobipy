# Help on class ParamConstClass in module gurobipy:
class ParamConstClass(object):
    """
    Gurobi parameters are used to control the optimization process.  They all
    have default values, but their values can be changed using the setParam()
    function.  Current values can be retrieved using the Model.getParamInfo()
    method.

    Parameters fall into the following categories:

    Termination: affect the termination of an optimize() call
      BarIterLimit: limits the number of barrier iterations performed
      BestBdStop: sets a best bound values at which optimization should stop
      BestObjStop: sets an objective value at which optimization should stop
      Cutoff: sets a target objective value
      IterationLimit: limits the number of simplex iterations performed
      NodeLimit: limits the number of MIP nodes explored
      SolutionLimit: sets a target for the number of feasible solutions found
      TimeLimit: limits the total time expended (in seconds)

    Tolerances: control the allowable feasibility or optimality violations
      BarConvTol: barrier convergence tolerance
      BarQCPConvTol: barrier convergence tolerance for QCP models
      FeasibilityTol: primal feasibility tolerance
      IntFeasTol: integer feasibility tolerance
      MarkowitzTol: threshold pivoting tolerance
      MIPGap: target relative MIP optimality gap
      MIPGapAbs: target absolute MIP optimality gap
      OptimalityTol: dual feasibility tolerance
      PSDTol: QP positive semidefinite tolerance

    Simplex: affect the simplex algorithms
      InfUnbdInfo: makes additional information available for infeasible or
                   unbounded LP models
      NormAdjust: chooses different pricing norm variants
      ObjScale: controls objective scaling
      PerturbValue: controls the magnitude of any simplex perturbations
      Quad: turns quad precision on or off
      ScaleFlag: turns model scaling on or off
      Sifting: dual simplex sifting strategy for LP, MIP root and MIP nodes
      SiftMethod: chooses from dual, primal and barrier to solve sifting
                  subproblems
      SimplexPricing: determines variable pricing strategy

    Barrier: affect the barrier algorithms
      BarCorrectors: limits the number of central corrections
      BarHomogeneous: selects the barrier homogeneous algorithm
      BarOrder: determines the fill reducing ordering strategy
      Crossover: controls barrier crossover
      CrossoverBasis: controls initial crossover basis construction
      QCPDual: enables dual variable computation for continuous QCP models

    MIP: affect the MIP algorithms
      BranchDir: controls the branching node selection
      ConcurrentMIP: enables concurrent MIP optimization
      ConcurrentJobs: enables distributed concurrent optimization
      DegenMoves: limit degenerate simplex moves
      Disconnected: controls the disconnected component strategy
      Heuristics: controls the amount of time spent in MIP heuristics
      ImproveStartGap: gap at which to switch MIP search strategies
      ImproveStartNodes: node count at which to switch MIP search strategies
      ImproveStartTime: time at which to switch MIP search strategies
      MinRelNodes: controls the minimum relaxation heuristic
      MIPFocus: affects the high-level MIP search strategy
      MIQCPMethod: controls whether to solve QCP node relaxation or to use OA
      NodefileDir: determines the directory used to store nodes on disk
      NodefileStart: memory nodes may use (in GB) before being written to disk
      NodeMethod: determines the algorithm used to solve MIP node relaxations
      NoRelHeuristic: determines whether the NoRel heuristic should be used
      PartitionPlace: controls when the partition heursitic runs
      PumpPasses: controls the feasibility pump heuristic
      RINS: sets the frequency of the RINS heuristic
      SolutionNumber: controls access to alternate MIP solutions
      SubMIPNodes: limits the numbers of nodes explored in a RINS sub-MIP
      Symmetry: controls access to alternate MIP solutions
      VarBranch: controls the branch variable selection strategy
      ZeroObjNodes: controls the zero objective heuristic

    Tuning: affect the operation of the tuning tool
      TuneCriterion: specify different tuning criteria
      TuneJobs: enables distributed tuning
      TuneOutput: tuning output level
      TuneResults: number of imroved parameter sets returned
      TuneTimeLimit: tuning time limit
      TuneTrials: number of trial runs with each parameter set

    Multiple solutions: determines how the MIP search looks for solutions
      PoolGap: determines the quality of the retained solutions
      PoolSearchMode: chooses the approach used to search for solutions
      PoolSolutions: determines the number of solutions that are stored

    MIP cuts: affect the generation of MIP cutting planes
      Cuts: global cut generation control
      CliqueCuts: controls clique cut generation
      CoverCuts: controls cover cut generation
      CutAggPasses: limits aggregation during cut generation
      CutPasses: limits the number of cut passes
      FlowCoverCuts: controls flow cover cut generation
      FlowPathCuts: controls flow path cut generation
      GomoryPasses: controls the number of Gomory cut passes
      GUBCoverCuts: controls GUB cover cut generation
      ImpliedCuts: controls implied bound cut generation
      InfProofCuts: controls infeasibility proof cut generation
      MIPSepCuts: controls MIP separation cut generation
      MIRCuts: controls MIR cut generation
      ModKCuts: controls mod-k cut generation
      NetworkCuts: controls network cut generation
      ProjImpliedCuts: controls projected implied bound cut generation
      StrongCGCuts: controls Strong-CG cut generation
      SubMIPCuts: controls sub-MIP cut generation
      ZeroHalfCuts: controls zero-half cut generation

    Compute Server: used for compute server based optimizations
      ComputeServer: server URL to access the cluster
      CSGroup: group name
      CSIdleTimeout: job idle timeout
      CSPriority: compute server job priority
      CSQueueTimeout: queue timeout for new jobs
      CSRouter: router URL
      CSTLSInsecure: TLS security mode
      ServerPassword: cluster client password
      ServerTimeout: network timeout

    Token Server: affect token server parameters
      TokenServer: adress of token server
      TSPort: token server port

    Distributed algorithms: used for distributed optimization
      WorkerPassword: cluster client password
      WorkerPool: server URL to access the cluster

    Cloud: parameters used for cloud-based optimization
      CloudAccessID: Instant Cloud access ID
      CloudPool: Instant Cloud pool name
      CloudSecretKey: Instant Cloud secret key

    Other:
      AggFill: controls the level of presolve aggregation
      Aggregate: turns presolve aggregation on or off
      DisplayInterval: sets the frequency at which log lines are printed
      DualReductions: controls presolve dual reductions
      FeasRelaxBigM: BigM value for feasibility relaxation
      IgnoreNames: indicates whether to ignore names provided by users
      IISMethod: method used to find an IIS
      LazyConstraints: programs that use lazy constraints must set this to 1
      LogFile: sets the name of the Gurobi log file
      LogToConsole: turn logging to the console on or off
      Method: algorithm used to solve a continuous model or the root node of a
              MIP model (auto, primal simplex, dual simplex, barrier, or
              concurrent)
      NumericFocus: controls numerically conservative level
      MultiObjMethod: warm-start method to solve for subsequent objectives
      MultiObjPre: controls initial presolve level on multi-objective models
      ObjNumber: selects the objective index of multi-objectives
      OutputFlag: turn logging on or off
      PreCrush: allows presolve to crush any user cut
      PreDepRow: controls the presolve dependent row reduction
      PreDual: determines whether presolve forms the dual of the input model
      PrePasses: limits the number of presolve passes
      PreQLinearize: controls presolve Q matrix linearization
      Presolve: turns presolve on or off
      PreSOS1BigM: threshold for presolve SOS1 conversion to binary form
      PreSOS2BigM: threshold for presolve SOS2 conversion to binary form
      PreSparsify: enables the presolve sparsify reduction
      PreMIQCPForm: chooses the form for MIQCP presolved model
      Record: enables replay
      ResultFile: result file to write when optimization completes
      Seed: sets the random number seed
      StartNodeLimit: limits nodes in MIP start sub-MIP
      StartNumber: selects the MIP start index
      Threads: sets the number of threads to apply to parallel MIP
      UpdateMode: controls the way how to update a model

    Parameters can be referred to using the Param class (e.g.
    "setParam(GRB.param.threads, 1)"), or by using the name as a string
    (e.g., "setParam('threads', 1)).  You can use the '*' and '?' wildcards
    when inputting parameter names, and text case is ignored
    (so "setParam('thr*', 1)" would also work).

    For further information on any of these parameters, type
    paramHelp('paramname') (e.g., paramHelp("NodeLimit")).  Wildcards
    are also accepted for paramHelp().

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

    AggFill = 'AggFill'

    Aggregate = 'Aggregate'

    BarConvTol = 'BarConvTol'

    BarCorrectors = 'BarCorrectors'

    BarHomogeneous = 'BarHomogeneous'

    BarIterLimit = 'BarIterLimit'

    BarOrder = 'BarOrder'

    BarQCPConvTol = 'BarQCPConvTol'

    BestBdStop = 'BestBdStop'

    BestObjStop = 'BestObjStop'

    BranchDir = 'BranchDir'

    CSGroup = 'CSGroup'

    CSIdleTimeout = 'CSIdleTimeout'

    CSPriority = 'CSPriority'

    CSQueueTimeout = 'CSQueueTimeout'

    CSRouter = 'CSRouter'

    CSTLSInsecure = 'CSTLSInsecure'

    CliqueCuts = 'CliqueCuts'

    CloudAccessID = 'CloudAccessID'

    CloudHost = 'CloudHost'

    CloudPool = 'CloudPool'

    CloudSecretKey = 'CloudSecretKey'

    ComputeServer = 'ComputeServer'

    ConcurrentJobs = 'ConcurrentJobs'

    ConcurrentMIP = 'ConcurrentMIP'

    CoverCuts = 'CoverCuts'

    Crossover = 'Crossover'

    CrossoverBasis = 'CrossoverBasis'

    CutAggPasses = 'CutAggPasses'

    CutPasses = 'CutPasses'

    Cutoff = 'Cutoff'

    Cuts = 'Cuts'

    DegenMoves = 'DegenMoves'

    Disconnected = 'Disconnected'

    DisplayInterval = 'DisplayInterval'

    DistributedMIPJobs = 'DistributedMIPJobs'

    DualReductions = 'DualReductions'

    FeasRelaxBigM = 'FeasRelaxBigM'

    FeasibilityTol = 'FeasibilityTol'

    FlowCoverCuts = 'FlowCoverCuts'

    FlowPathCuts = 'FlowPathCuts'

    GUBCoverCuts = 'GUBCoverCuts'

    GomoryPasses = 'GomoryPasses'

    Heuristics = 'Heuristics'

    IISMethod = 'IISMethod'

    IgnoreNames = 'IgnoreNames'

    ImpliedCuts = 'ImpliedCuts'

    ImproveStartGap = 'ImproveStartGap'

    ImproveStartNodes = 'ImproveStartNodes'

    ImproveStartTime = 'ImproveStartTime'

    InfProofCuts = 'InfProofCuts'

    InfUnbdInfo = 'InfUnbdInfo'

    IntFeasTol = 'IntFeasTol'

    IterationLimit = 'IterationLimit'

    LazyConstraints = 'LazyConstraints'

    LogFile = 'LogFile'

    LogToConsole = 'LogToConsole'

    MIPFocus = 'MIPFocus'

    MIPGap = 'MIPGap'

    MIPGapAbs = 'MIPGapAbs'

    MIPSepCuts = 'MIPSepCuts'

    MIQCPMethod = 'MIQCPMethod'

    MIRCuts = 'MIRCuts'

    MarkowitzTol = 'MarkowitzTol'

    Method = 'Method'

    MinRelNodes = 'MinRelNodes'

    ModKCuts = 'ModKCuts'

    MultiObjMethod = 'MultiObjMethod'

    MultiObjPre = 'MultiObjPre'

    NetworkCuts = 'NetworkCuts'

    NoRelHeuristic = 'NoRelHeuristic'

    NodeLimit = 'NodeLimit'

    NodeMethod = 'NodeMethod'

    NodefileDir = 'NodefileDir'

    NodefileStart = 'NodefileStart'

    NormAdjust = 'NormAdjust'

    NumericFocus = 'NumericFocus'

    ObjNumber = 'ObjNumber'

    ObjScale = 'ObjScale'

    OptimalityTol = 'OptimalityTol'

    OutputFlag = 'OutputFlag'

    PSDTol = 'PSDTol'

    PartitionPlace = 'PartitionPlace'

    PerturbValue = 'PerturbValue'

    PoolGap = 'PoolGap'

    PoolSearchMode = 'PoolSearchMode'

    PoolSolutions = 'PoolSolutions'

    PreCrush = 'PreCrush'

    PreDepRow = 'PreDepRow'

    PreDual = 'PreDual'

    PreMIQCPForm = 'PreMIQCPForm'

    PrePasses = 'PrePasses'

    PreQLinearize = 'PreQLinearize'

    PreSOS1BigM = 'PreSOS1BigM'

    PreSOS2BigM = 'PreSOS2BigM'

    PreSparsify = 'PreSparsify'

    Presolve = 'Presolve'

    ProjImpliedCuts = 'ProjImpliedCuts'

    PumpPasses = 'PumpPasses'

    QCPDual = 'QCPDual'

    Quad = 'Quad'

    RINS = 'RINS'

    Record = 'Record'

    ResultFile = 'ResultFile'

    ScaleFlag = 'ScaleFlag'

    Seed = 'Seed'

    ServerPassword = 'ServerPassword'

    ServerTimeout = 'ServerTimeout'

    SiftMethod = 'SiftMethod'

    Sifting = 'Sifting'

    SimplexPricing = 'SimplexPricing'

    SolutionLimit = 'SolutionLimit'

    SolutionNumber = 'SolutionNumber'

    StartNodeLimit = 'StartNodeLimit'

    StartNumber = 'StartNumber'

    StrongCGCuts = 'StrongCGCuts'

    SubMIPCuts = 'SubMIPCuts'

    SubMIPNodes = 'SubMIPNodes'

    Symmetry = 'Symmetry'

    TSPort = 'TSPort'

    Threads = 'Threads'

    TimeLimit = 'TimeLimit'

    TokenServer = 'TokenServer'

    TuneCriterion = 'TuneCriterion'

    TuneJobs = 'TuneJobs'

    TuneOutput = 'TuneOutput'

    TuneResults = 'TuneResults'

    TuneTimeLimit = 'TuneTimeLimit'

    TuneTrials = 'TuneTrials'

    UpdateMode = 'UpdateMode'

    VarBranch = 'VarBranch'

    WorkerPassword = 'WorkerPassword'

    WorkerPool = 'WorkerPool'

    ZeroHalfCuts = 'ZeroHalfCuts'

    ZeroObjNodes = 'ZeroObjNodes'
