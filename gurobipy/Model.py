class Model():
    """
          Gurobi model object.  Commonly used methods on this object are:
            getConstrs(): Get a list of constraints in the model
            getParamInfo(paramname): Get information on a model parameter.
            getVars(): Get a list of variables in the model
            optimize(): Optimize the model.
            printAttr(attrname, filter): Print attribute values.
            printQuality(): Print solution quality statistics.
            printStats(): Print model statistics.
            read(filename): Read model data (MIP start, basis, etc.) from a file
            reset(): Discard any resident solution information.
            resetParams(): Reset all parameters to their default values.
            setParam(paramname, newval): Set a model parameter to a new value.
            write(filename): Write model data to a file.

          Models have a number of attributes that can be queried or modified.
          For example, "print model.objval" prints the objective value of
          the current solution.  Commonly used model attributes are:
            numConstrs: Number of constraints in model
            numVars: Number of variables in model
            status: Optimization status
            objVal: Objective of current solution
          Type "help(GRB.attr)" for a complete list.

          Additional methods on this object are:
            addConstr(), addGenConstrMax(), addGenConstrMin(), addGenConstrAbs(),
            addGenConstrAnd(), addGenConstrOr(), addGenConstrIndicator(),
            addRange(), addSOS(), addVar(), chgCoeff(), computeIIS(),
            copy(), fixed(), getCoeff(), getCol(), getRow(), message(), presolve(),
            relax(), terminate(), update()

          Additional help can be obtained on any of these methods (e.g.,
          help(Model.optimize)).

          Methods defined here:

          __del__(self)

          __dir__(self)

          __getattr__(self, name)

          __init__(self, name='', env=None, cmodel=None)

          __repr__(self)

          __setattr__(self, name, value)
    """

    def __init__(name='', env=None, cmodel=None):
        pass

    def addConstr(self, lhs, sense=None, rhs=None, name=''):
        """
        ROUTINE:
          addConstr(lhs, sense, rhs, name)

        PURPOSE:
          Add a constraint to the model.

        ARGUMENTS:
          lhs (float, Var, LinExpr or TempConstr): Left-hand side
          sense (char): Constraint sense (e.g., GRB.LESS_EQUAL)
          rhs (float, Var, or LinExpr): Right-hand side
          name (string): Constraint name (default is no name)

        RETURN VALUE:
          The created Constr object.

        EXAMPLE:
          c = model.addConstr(x + y <= 1)
          c = model.addConstr(x + y + z == [1, 2])
          c = model.addConstr(x*x + y*y <= 1)
          c = model.addConstr(z == and_(y, x, w))
          c = model.addConstr(z == min_(x, y))
          c = model.addConstr((w == 1) >> (x + y <= 1))
        """
        pass

    def addConstrs(self, constrs, name=''):
        """
        addConstrs(constrs, name="")

        Add constraints in bulk, using a generator expression.  Returns a dictionary
        of Constr objects, indexed by the values (or tuples of values) used by the
        generator expression.

        If you specify a name, the constraints will get that name.  If name is a scalar
        string, the names will be subscripted by the generator index.  If name
        equals the underscore character ("_"), then the names will equal the index value.
        """
        pass

    def addGenConstrAbs(self, resvar, argvar, name=''):
        """
        ROUTINE:
          addGenConstrAbs(resvar, argvar, name)

        PURPOSE:
          Add a general constraint of type ABS to the model.

        ARGUMENTS:
          resvar (Var): Resultant variable of ABS constraint
          argvar (Var): Argument variable of ABS constraint
          name (string): Constraint name (default is no name)

        RETURN VALUE:
          The created general constraint object.

        EXAMPLE:
          genconstr = model.addGenConstrAbs(z, x1, "myAbsConstr")
        """
        pass

    def addGenConstrAnd(self, resvar, vars, name=''):
        """
                ROUTINE:
          addGenConstrAnd(resvar, vars, name)

        PURPOSE:
          Add a general constraint of type AND to the model.

        ARGUMENTS:
          resvar (Var): Resultant variable of AND constraint
          vars (list of Var, or tupledict): Argument variables of AND constraint
          name (string): Constraint name (default is no name)

        RETURN VALUE:
          The created general constraint object.

        EXAMPLE:
          genconstr = model.addGenConstrAnd(z, [x1, x2, x3], "myAndConstr")
        :param resvar:
        :param vars:
        :param name:
        :return:
        """
        pass

    def addGenConstrIndicator(self, binvar, binval, lhs, sense=None, rhs=None, name=''):
        """
		ROUTINE:
          addGenConstrIndicator(binvar, binval, lhs, sense, rhs, name)

        PURPOSE:
          Add a general constraint of type INDICATOR to the model.

        ARGUMENTS:
          GRB.GENCONSTR_INDICATOR (option 1):
            binvar (Var): Antecedent variable of indicator constraint
            binval (Boolean): Value of antecedent variable that activates the linear constraint
            lhs (float, Var, or LinExpr): Linear expression of constraint triggered by the indicator
            sense (char): Sense of constraint triggered by the indicator (e.g., GRB.LESS_EQUAL)
            rhs (float): Right-hand side of linear constraint triggered by the indicator
            name (string): Constraint name (default is no name)

          GRB.GENCONSTR_INDICATOR (option 2):
            binvar (Var): Antecedent variable of indicator constraint
            binval (Boolean): Value of antecedent variable that activates the linear constraint
            lhs (TempConstr): Linear constraint triggered by indicator
            name (string): Constraint name (default is no name)

        RETURN VALUE:
          The created general constraint object.

        EXAMPLE:
          genconstr = model.addGenConstr(z, 0, 2*x1 - 1.5*x2 + 3.0*x3 == 4.5, name="myIndicatorConstr")
		"""
        pass


    def addGenConstrMax(self, resvar, vars, constant=None, name=''):
        """
        ROUTINE:
          addGenConstrMax(resvar, vars, constant, name)

        PURPOSE:
          Add a general constraint of type MAX to the model.

        ARGUMENTS:
          resvar (Var): Resultant variable of MAX constraint
          vars (list of Var, or tupledict): Argument variables of MAX constraint
          constant (float, optional): Constant of MAX constraint
          name (string, optional): Constraint name (default is no name)

        RETURN VALUE:
          The created general constraint object.

        EXAMPLE:
          genconstr = model.addGenConstrMax(z, [x1, x2, x3], 17.5, "myMaxConstr")
        """
        pass


    def addGenConstrMin(self, resvar, vars, constant=None, name=''):
        """
        ROUTINE:
          addGenConstrMin(resvar, vars, constant, name)

        PURPOSE:
          Add a general constraint of type MIN to the model.

        ARGUMENTS:
          resvar (Var): Resultant variable of MIN constraint
          vars (list of Var, or tupledict): Argument variables of MIN constraint
          constant (float, optional): Constant of MIN constraint
          name (string, optional): Constraint name (default is no name)

        RETURN VALUE:
          The created general constraint object.

        EXAMPLE:
          genconstr = model.addGenConstrMin(z, [x1, x2, x3], 17.5, "myMinConstr")
        """
        pass


    def addGenConstrOr(self, resvar, vars, name=''):
        """
        ROUTINE:
          addGenConstrOr(resvar, vars, name)

        PURPOSE:
          Add a general constraint of type OR to the model.

        ARGUMENTS:
          resvar (Var): Resultant variable of OR constraint
          vars (list of Var, or tupledict): Argument variables of OR constraint
          name (string): Constraint name (default is no name)

        RETURN VALUE:
          The created general constraint object.

        EXAMPLE:
          genconstr = model.addGenConstrOr(z, [x1, x2, x3], "myOrConstr")
        """
        pass


    def addLConstr(self, lhs, sense=None, rhs=None, name=''):
        """
        ROUTINE:
          addLConstr(lhs, sense, rhs, name)

        PURPOSE:
          Add a linear constraint to the model.

        ARGUMENTS:
          lhs (float, Var, LinExpr or TempConstr): Left-hand side
          sense (char): Constraint sense (e.g., GRB.LESS_EQUAL)
          rhs (float, Var, or LinExpr): Right-hand side
          name (string): Constraint name (default is no name)

        RETURN VALUE:
          The created Constr object.

        EXAMPLE:
          c = model.addLConstr(x + y <= 1)
          c = model.addLConstr(LinExpr([1.0,1.0], [x,y]), GRB.LESS_EQUAL, 1)
          c = model.addLConstr(lhs = 5 * x + y, sense = GRB.LESS_EQUAL, rhs = 3 * z, name = "C1")
        """
        pass


    def addQConstr(self, lhs, sense=None, rhs=None, name=''):
        """
        ROUTINE:
          addQConstr(lhs, sense, rhs, name)

        PURPOSE:
          Add a quadratic constraint to the model.

        ARGUMENTS:
          lhs (float, Var, LinExpr, or QuadExpr): Left-hand side
          sense (char): Constraint sense (e.g., GRB.LESS_EQUAL)
          rhs (float, Var, LinExpr, or QuadExpr): Right-hand side
          name (string): Constraint name (default is no name)

        RETURN VALUE:
          The created QConstr object.

        EXAMPLE:
          qc = model.addQConstr(x*x + y*y <= 1)
        """
        pass


    def addRange(self, expr, lower, upper, name=''):
        """
        ROUTINE:
          addRange(expr, lhs, rhs, name)

        PURPOSE:
          Add a range constraint to the model.

        ARGUMENTS:
          expr (Var, or LinExpr): Linear expression being constrained
          lower (float): Lower bound on linear expression
          upper (float): Upper bound on linear expression
          name (string): Constraint name (default is no name)

        RETURN VALUE:
          The created Constr object.

        EXAMPLE:
          c = model.addRange(x + y, 1.0, 2.0)
        """
        pass


    def addSOS(self, type, vars, wts=None):
        """
        ROUTINE:
          addSOS(type, vars, wts)

        PURPOSE:
          Add an SOS constraint to the model.

        ARGUMENTS:
          type (Int): SOS type 1 (GRB.SOS_TYPE1) or type 2 (GRB.SOS_TYPE2)
          vars (list of Var): Variables in SOS
          wts (list of float): Weights for variables in SOS

        RETURN VALUE:
          The created SOS object.

        EXAMPLE:
          sos = model.addSOS(GRB.SOS_TYPE1, [x, y, z])
        """
        pass


    def addVar(self, lb=0.0, ub=1e+100, obj=0.0, vtype='C', name='', column=None):
        """
        ROUTINE:
          addVar(lb, ub, obj, vtype, name, column)

        PURPOSE:
          Add a variable to the model.

        ARGUMENTS:
          lb (float): Lower bound (default is zero)
          ub (float): Upper bound (default is infinite)
          obj (float): Objective coefficient (default is zero)
          vtype (string): Variable type (default is GRB.CONTINUOUS)
          name (string): Variable name (default is no name)
          column (Column): Initial coefficients for column (default is None)

        RETURN VALUE:
          The created Var object.

        EXAMPLE:
          v = model.addVar(ub=2.0, name="NewVar")
        """
        pass


    def addVars(self, *indexes, **kwargs):
        """
        addVars(*indexes, lb=0.0, ub=GRB.INFINITY, obj=0.0, vtype=GRB.CONTINUOUS,
                   name="")

        Add variables in bulk, given one or more lists or integers that serve as
        indexes for the variables.  Returns a dictionary of Var objects, indexed by
        the values (or tuples of values) from the index set.

        The optional parameters (lb, ub, obj, vtype, name) work similar
        to the addVar() method, with the following exceptions:
        1. The parameter name is required (ex: vtype=GRB.BINARY)
        2. You can specify the value as a scalar, a list or a dictionary.  For a scalar,
           the value will be used for all variables; for a list, the values must be
           in the same order as the index set; for a dictionary, they must be indexed
           by the variable index.
        3. If you specify a scalar string for name, the variable name will be
           subscripted automatically.
        """
        pass


    def cbCut(self, lhs, sense=None, rhs=None):
        pass


    def cbGet(self, what):
        pass


    def cbGetNodeRel(self, vars):
        pass


    def cbGetSolution(self, vars):
        pass


    def cbLazy(self, lhs, sense=None, rhs=None):
        pass


    def cbSetSolution(self, vars, solution):
        pass


    def cbStopOneMultiObj(self, objnum):
        """
        ROUTINE:
          cbStopOneMultiObj(objnum)

        PURPOSE:
          terminate individual optimization for the multi-objectives of the MIP model (from a callback).

        ARGUMENTS:
          objnum

        RETURN VALUE:
          None

        EXAMPLE:
          model.cbStopOneMultiObj(objnum)
        """
        pass


    def cbUseSolution(self):
        pass


    def chgCoeff(self, constr, var, newvalue):
        """
        ROUTINE:
          chgCoeff(constr, var, newvalue)

        PURPOSE:
          Change a coefficient in the constraint matrix.

        ARGUMENTS:
          constr (Constr): The constraint for the changed coefficient
          var (Var): The variable for the changed coefficient
          newvalue (float): Desired new value

        RETURN VALUE:
          None.

        EXAMPLE:
          model.chgCoeff(model.getConstrs()[0], model.getVars()[0], 1.0)
        """
        pass


    def computeIIS(self):
        """
        ROUTINE:
          computeIIS()

        PURPOSE:
          Compute an Irreducible Infeasible Subsystem (IIS).

        ARGUMENTS:
          None.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.computeIIS()
        """
        pass


    def copy(self):
        """
        ROUTINE:
          copy()

        PURPOSE:
          Create an exact copy of a model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          The copied Model object.

        EXAMPLE:
          copy = model.copy()
          copy.optimize()
        """
        pass


    def discardConcurrentEnvs(self):
        """
        ROUTINE:
          discardConcurrentEnvs()

        PURPOSE:
          Discard concurrent environments previously created through
          getConcurrentEnv(), thus restoring the concurrent optimizer
          to its default behavior.

        ARGUMENTS:
          None.

        RETURN VALUE:
          None.

        EXAMPLE:
          env0 = model.getConcurrentEnv(0)
          env1 = model.getConcurrentEnv(1)

          env0.setParam('Method', 0)
          env1.setParam('Method', 1)

          model.optimize()

          model.discardConcurrentEnvs()
        """
        pass


    def discardMultiobjEnvs(self):
        """
        ROUTINE:
          discardMultiobjEnvs()

        PURPOSE:
          Discard multiobj environments previously created through
          getMultiobjEnv(), thus restoring the multiobj optimizer
          to its default behavior.

        ARGUMENTS:
          None.

        RETURN VALUE:
          None.

        EXAMPLE:
          env0 = model.getMultiobjEnv(0)
          env1 = model.getMultiobjEnv(1)

          env0.setParam('Method', 0)
          env1.setParam('Method', 1)

          model.optimize()

          model.discardMultiobjEnvs()
        """
        pass


    def display(self, obj=None):
        pass


    def feasRelax(self, relaxobjtype, minrelax, vars, lbpen, ubpen, constrs, rhspen):
        """
        ROUTINE:
          feasRelax(relaxobjtype, minrelax, vars, lbpen, ubpen, constrs, rhspen)

        PURPOSE:
          Perform a feasibility relaxation on the model.  Add penalty
          variables and a penalty objective.  Consider using feasRelaxS()
          if you want a simpler argument list.

        ARGUMENTS:
          relaxobjtype (int): Select the relaxation objective function.  Options
                              are linear (0), quadratic (1), or cardinality (2).
          minrelax (Boolean): Indicate whether to solve feasrelax model to
                              enforce minimal relaxation
          vars (list of Var): Variable that are allowed to violate bounds
          lbpen (list of float): Penalties for lower bound violations
          ubpen (list of float): Penalties for upper bound violations
          constrs (list of Constr): Constraints that can be violated
          rhspen (list of float): Penalties for constraint violations

        RETURN VALUE:
          feasRelax model objective value, if minimal relaxation is enforced,
          0 otherwise

        EXAMPLE:
          if model.status == GRB.INFEASIBLE:
            vars = model.getVars()
            ubpen = [1.0]*model.numVars
            model.feasRelax(1, False, vars, None, ubpen, None, None)
            model.optimize()
        """
        pass


    def feasRelaxS(self, relaxobjtype, minrelax, vrelax, crelax):
        """
        ROUTINE:
          feasRelaxS(relaxobjtype, minrelax, vrelax, crelax)

        PURPOSE:
          Perform a feasibility relaxation on the model.  Add penalty
          variables and a penalty objective.  Simple version; consider using
          feasRelax() if you want more control over the relaxation.

        ARGUMENTS:
          relaxobjtype (int): Select the relaxation objective function.  Options
                              are linear (0), quadratic (1), or cardinality (2).
          minrelax (Boolean): Indicate whether to solve feasrelax model to
                              enforce minimal relaxation
          vrelax (Boolean): If True, variable bound violations are allowed
          crelax (Boolean): If True, constraint violations are allowed

        RETURN VALUE:
          feasRelax model objective value, if minimal relaxation is enforced,
          0 otherwise

        EXAMPLE:
          if model.status == GRB.INFEASIBLE:
            model.feasRelaxS(1, False, False, True)
            model.optimize()
        """
        pass


    def feasibility(self):
        """
        ROUTINE:
          feasibility()

        PURPOSE:
          Return the feasibility version of the MIP model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A copy of the given model with a cancelled objective function.

        EXAMPLE:
          feasibility = model.feasibility()
          feasibility.optimize()
        """
        pass


    def fixed(self):
        """
        ROUTINE:
          fixed()

        PURPOSE:
          Return the fixed version of the MIP model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A new model, containing the fixed version of the MIP model.

        EXAMPLE:
          fixed = model.fixed()
          fixed.optimize()
        """
        pass


    def getAttr(self, attrname, arg2=None):
        """
        ROUTINE:
          getAttr(attrname), or
          getAttr(attrname, objects)

        PURPOSE:
          Request the value of an attribute.

        ARGUMENTS:
          attrname (string): The name of the requested attribute.
          objects (optional): List or dictionary of variables or constraints

        RETURN VALUE:
          The attribute value.  If argument 'objects' is present,
          a list of values is returned.

        EXAMPLE:
          print model.getAttr("modelName")
          print model.getAttr("lb", model.getVars())
          print model.getAttr("qcrhs", model.getQConstrs())

        NOTES:
          Type "help(GRB.attr)" for a list of all available attributes.
        """
        pass


    def getCoeff(self, constr, var):
        """
        ROUTINE:
          getCoeff(constr, var)

        PURPOSE:
          Retrieve a coefficient from the constraint matrix.

        ARGUMENTS:
          constr (Constr): Constraint of interest
          var (Var): Variable of interest

        RETURN VALUE:
          The coefficient for 'var' in 'constr'

        EXAMPLE:
          coeff = model.getCoeff(model.getConstrs()[0], model.getVars()[0])
        """
        pass


    def getCol(self, var):
        """
        ROUTINE:
          getCol(var)

        PURPOSE:
          Obtain all terms associated with a Var.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A Column object containing a list of terms associated with the Var.

        EXAMPLE:
          col = model.getCol(model.getVars()[0])
          for i in range(col.size()):
            print col.getCoeff(i), expr.getConstr(i)
        """
        pass


    def getConcurrentEnv(self, num):
        """
        ROUTINE:
          getConcurrentEnv()

        PURPOSE:
          Retrieve a concurrent environment.  This is used to manually
          configure the parameter settings used by different threads
          in the concurrent optimizer (for LP models).   You should make
          multiple calls to getConcurrentEnv() with integer arguments from
          0 through n-1, where n is the number of different solves you
          would like to launch,  You can set parameters on each concurrent
          environment to capture the desired behavior of each concurrent
          thread.

        ARGUMENTS:
          Concurrent environment number.

        RETURN VALUE:
          An Env object.

        EXAMPLE:
          env0 = model.getConcurrentEnv(0)
          env1 = model.getConcurrentEnv(1)

          env0.setParam('Method', 0)
          env1.setParam('Method', 1)

          model.optimize()
        """
        pass


    def getConstrByName(self, name):
        """
        ROUTINE:
          getConstrByName()

        PURPOSE:
          Retrieve a linear constraint with the specified name from the model.

        ARGUMENTS:
          Constraint name.

        RETURN VALUE:
          A Constr object, or None if no matching variable is found.

        EXAMPLE:
          constr = model.getConstrByName("c1")
        """
        pass


    def getConstrs(self):
        """
        ROUTINE:
          getConstrs()

        PURPOSE:
          Obtain a list of linear constraints in the model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A list of Constr objects.

        EXAMPLE:
          constrs = model.getConstrs()
          for c in constrs:
            print c.ConstrName, c.Slack
        """
        pass


    def getGenConstrAbs(self, genconstr):
        """
        ROUTINE:
          getGenConstrAbs(genconstr)

        PURPOSE:
          Obtain all data associated with a general constraint of type ABS.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A tuple (resvar, argvar) that contains the data for the general constraint.
            resvar (Var): Resultant variable of ABS constraint
            argvar (Var): Argument variable of ABS constraint

        EXAMPLE:
          (resvar, argvar) = model.getGenConstrAbs(model.getGenConstrs()[0])
        """
        pass


    def getGenConstrAnd(self, genconstr):
        """
        ROUTINE:
          getGenConstrAnd(genconstr)

        PURPOSE:
          Obtain all data associated with a general constraint of type AND.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A tuple (resvar, vars) that contains the data for the general constraint.
            resvar (Var): Resultant variable of AND constraint
            vars (list of Var): Operand variables of AND constraint

        EXAMPLE:
          (resvar, vars) = model.getGenConstrAnd(model.getGenConstrs()[0])
        """
        pass


    def getGenConstrIndicator(self, genconstr):
        """
        ROUTINE:
          getGenConstrIndicator(genconstr)

        PURPOSE:
          Obtain all data associated with a general constraint of type INDICATOR.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A tuple (binvar, binval, vars, vals, sense, rhs) that contains the data for the general constraint.
            binvar (Var): Antecedent variable of indicator constraint
            binval (Boolean): Value of antecedent variable that activates the linear constraint
            expr (LinExpr): LinExpr object containing the left-hand side of the constraint triggered by the indicator
            sense (char): Sense of linear constraint triggered by the indicator (e.g., GRB.LESS_EQUAL)
            rhs (float): Right-hand side of linear constraint triggered by the indicator

        EXAMPLE:
          (binvar, binval, expr, sense, rhs) = model.getGenConstr(model.getGenConstrs()[0])
        """
        pass


    def getGenConstrMax(self, genconstr):
        """
        ROUTINE:
          getGenConstrMax(genconstr)

        PURPOSE:
          Obtain all data associated with a general constraint of type MAX.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A tuple (resvar, vars, constant) that contains the data for the general constraint.
            resvar (Var): Resultant variable of MAX constraint
            vars (list of Var): Operand variables of MAX constraint
            constant (float): Constant of MAX constraint

        EXAMPLE:
          (resvar, vars, constant) = model.getGenConstrMax(model.getGenConstrs()[0])
        """
        pass


    def getGenConstrMin(self, genconstr):
        """
        ROUTINE:
          getGenConstrMin(genconstr)

        PURPOSE:
          Obtain all data associated with a general constraint of type MIN.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A tuple (resvar, vars, constant) that contains the data for the general constraint.
            resvar (Var): Resultant variable of MIN constraint
            vars (list of Var): Operand variables of MIN constraint
            constant (float): Constant of MIN constraint

        EXAMPLE:
          (resvar, vars, constant) = model.getGenConstrMin(model.getGenConstrs()[0])
        """
        pass


    def getGenConstrOr(self, genconstr):
        """
        ROUTINE:
          getGenConstrOr(genconstr)

        PURPOSE:
          Obtain all data associated with a general constraint of type OR.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A tuple (resvar, vars) that contains the data for the general constraint.
            resvar (Var): Resultant variable of OR constraint
            vars (list of Var): Operand variables of OR constraint

        EXAMPLE:
          (resvar, vars) = model.getGenConstrOr(model.getGenConstrs()[0])
        """
        pass


    def getGenConstrs(self):
        """
        ROUTINE:
          getGenConstrs()

        PURPOSE:
          Obtain a list of general constraints in the model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A list of GenConstr objects.

        EXAMPLE:
          genconstrs = model.getGenConstrs()
          for c in genconstrs:
            print c.name
        """
        pass


    def getMultiobjEnv(self, num):
        """
        ROUTINE:
          getMultiobjEnv()

        PURPOSE:
          Retrieve a multiobj environment.  This is used to manually
          configure the parameter settings used in the multiobj
          optimizer.  You should make multiple calls to getMultiobjEnv()
          with integer arguments from 0 through n-1, where n is the
          number of different priorities for the multi-objectives.
          You can set parameters on each multiobj environment to capture
          the desired behavior of the optimization for each objective
          priority

        ARGUMENTS:
          Multiobj environment number.

        RETURN VALUE:
          An Env object.

        EXAMPLE:
          env0 = model.getMultiobjEnv(0)
          env1 = model.getMultiobjEnv(1)

          env0.setParam('Method', 0)
          env1.setParam('Method', 1)

          model.optimize()
        """
        pass


    def getObjective(self, index=None):
        """
        ROUTINE:
          getObjective()

        PURPOSE:
          Query the model objective

        ARGUMENTS:
          None.

        RETURN VALUE:
          Model objective function, returned as either a LinExpr or QuadExpr
          object.

        EXAMPLE:
          expr = model.getObjective()
        """
        pass


    def getPWLObj(self, var):
        """
        ROUTINE:
          getPWLObj(var)

        PURPOSE:
          Retrieves the piecewise-linear objective for a variable

        ARGUMENTS:
          var: the Var whose piecewise objective is returned.

        RETURN VALUE:
          A list of tuples, where each tuple captures a point on
          the piecewise-linear function.

        EXAMPLE:
          print model.getPWLObj(v)
        """
        pass


    def getParamInfo(self, paramname):
        """
        ROUTINE:
          getParamInfo(paramname)

        PURPOSE:
          Get the current value of a parameter.

        ARGUMENTS:
          paramname (string): The name of the parameter.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.getParamInfo("NodeLimit")

        NOTES:
          Returns a tuple, containing the parameter name, the paramter type,
          the current value, the minimum allowed value, the maximum allowed value,
          and the default value.

          Routine paramHelp() provides additional information on the available
          parameters.
        """
        pass


    def getQCRow(self, qc):
        """
        ROUTINE:
          getQCRow(qc)

        PURPOSE:
          Obtain all terms associated with a quadratic constraint.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A QuadExpr object containing the left-hand side of the constraint.

        EXAMPLE:
          expr = model.getQCRow(model.getQConstrs()[0])
          model.addConstr(expr >= 0)
        """
        pass


    def getQConstrs(self):
        """
        ROUTINE:
          getQConstrs()

        PURPOSE:
          Obtain a list of quadratic constraints in the model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A list of QConstr objects.

        EXAMPLE:
          qconstrs = model.getQConstrs()
          for c in qconstrs:
            print c.QCname
        """
        pass


    def getRow(self, constr):
        """
        ROUTINE:
          getRow(constr)

        PURPOSE:
          Obtain all terms associated with a constraint.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A LinExpr object containing the left-hand side of the constraint.

        EXAMPLE:
          expr = model.getRow(model.getConstrs()[0])
          for i in range(expr.size()):
            print expr.getCoeff(i), expr.getVar(i)
        """
        pass


    def getSOS(self, sos):
        """
        ROUTINE:
          getSOS(sos)

        PURPOSE:
          Obtain all variables and weights associated with an SOS constraint.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A tuple that contains the SOS type (1 or 2), the list of member
          Var objects, and the associated SOS weights.

        EXAMPLE:
          (type, vars, weights) = model.getSOS(model.getSOSs()[0])
        """
        pass


    def getSOSs(self):
        """
        ROUTINE:
          getSOSs()

        PURPOSE:
          Obtain a list of SOS constraints in the model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A list of SOS objects.

        EXAMPLE:
          sos = model.getSOSs()
          for s in sos:
            print s
        """
        pass


    def getTuneResult(self, i):
        """
        ROUTINE:
          getTuneResult()

        PURPOSE:
          Retrive tuned parameter settings.

        ARGUMENTS:
          Tuning result number.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.getTuneResult(0)
        """
        pass


    def getVarByName(self, name):
        """
        ROUTINE:
          getVarByName()

        PURPOSE:
          Retrieve a variable with the specified name from the model.

        ARGUMENTS:
          Variable name.

        RETURN VALUE:
          A Var object, or None if no matching variable is found.

        EXAMPLE:
          var = model.getVarByName("x1")
        """
        pass


    def getVars(self):
        """
        ROUTINE:
          getVars()

        PURPOSE:
          Obtain a list of variables in the model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A list of Var objects.

        EXAMPLE:
          vars = model.getVars()
          for v in vars:
            print v.VarName, v.X
        """
        pass


    def linearize(self):
        """
        ROUTINE:
          linearize()

        PURPOSE:
          Return the linearized version of the MIQP model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A new model, containing the linearized version of the original model.

        EXAMPLE:
          linearized = model.linearize()
          linearized.optimize()
        """
        pass


    def message(self, msg):
        """
        ROUTINE:
          message(msg)

        PURPOSE:
          Write a message to the Gurobi log file.

        ARGUMENTS:
          msg (string): Message to append to log file.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.message("Found a new solution with objective " + str(obj))
        """
        pass


    def optimize(self, callback=None):
        """
        ROUTINE:
          optimize()

        PURPOSE:
          Optimize the model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.optimize()

        NOTES:
          The algorithm used to optimize the model depends on the model type and
          on the parameter settings.  A MIP model will always be optimized using
          the branch-and-cut algorithm.  A continuous model will be optimized
          using the dual simplex algorithm by default; the Method parameter
          can be used to choose a different algorithm.
        """
        pass


    def presolve(self):
        """
        ROUTINE:
          presolve()

        PURPOSE:
          Return the presolved version of the model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A new model, containing the presolved version of the original model.

        EXAMPLE:
          presolved = model.presolve()
          presolved.optimize()
        """
        pass


    def printAttr(self, attrname, filter='*'):
        """
        ROUTINE:
          printAttr(attrname, filter)

        PURPOSE:
          Print model attribute data.

        ARGUMENTS:
          attrname (string): The name of the attribute to print.  For attributes
                             with numerical values, only non-zero entries will
                             be printed.  Can be a list of attribute names,
                             in which case all listed attributes will be printed.
          filter (string): Regular expression for filtering results.   Only
                           variables/constraints whose names match the
                           (optional) filter are printed.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.optimize()
          model.printAttr("x", "v*")     # print 'x' when var name begins with 'v'
          model.printAttr(["lb", "ub"])  # print 'lb' and 'ub' attribute values
        """
        pass


    def printQuality(self):
        """
        ROUTINE:
          printQuality()

        PURPOSE:
          Print solution quality statistics.

        ARGUMENTS:
          None.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.optimize()
          model.printQuality()
        """
        pass


    def printStats(self):
        """
        ROUTINE:
          printStats()

        PURPOSE:
          Print model statistics.

        ARGUMENTS:
          None.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.printStats()
        """
        pass


    def read(self, filename):
        """
        ROUTINE:
          read(filename)

        PURPOSE:
          Import model data from a file.  The type of data is determined by
          the file suffix: .mst for MIP start data, .bas for basis
          information, or .prm for parameter settings.

        ARGUMENTS:
          filename (string): The name of the file.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.read("start.mst")

        NOTES:
          The file name may contain the '*' and '?' wildcard characters.  If
          more than one file matches, this routine will read the first match.
        """
        pass


    def relax(self):
        """
        ROUTINE:
          relax()

        PURPOSE:
          Return the relaxed version of the MIP model, in which all integrality
          restrictions, SOS conditions, semi-continuous and semi-integer
          requirements on variables have been relaxed and general constraints
          have been removed.

        ARGUMENTS:
          None.

        RETURN VALUE:
          A new, relaxed model.

        EXAMPLE:
          relaxed = model.relax()
          relaxed.optimize()

        NOTES:
          If the model is already continuous, then this method produces the
          same result as cloning the model.
        """
        pass


    def remove(self, items):
        """
        ROUTINE:
          remove()

        PURPOSE:
          Remove variables, linear constraints, SOS constraints, quadratic
          constraints, or general constraints from the model.

        ARGUMENTS:
          items: Items to remove from model.  The argument can be
                 a single Constr, Var, SOS, QConstr, or GenConstr,
                 or it can be a list, tuple, or dict containing
                 such items.  For a dict, the dict values will be
                 removed, not the keys.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.remove(model.getVars()[0])
          model.remove(model.getConstrs()[0:10])
        """
        pass


    def reset(self, clearall=0):
        """
        ROUTINE:
          reset()

        PURPOSE:
          Discard any solution information.  The next optimize() call starts
          from scratch.

        ARGUMENTS:
          clearall (int, optional): Should additional information such as MIP
                   starts, variable hints, branching priorities, lazy flags,
                   and partition information be cleared?

        RETURN VALUE:
          None.

        EXAMPLE:
          model.reset()
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
          model.resetParams()
        """
        pass


    def setAttr(self, attrname, arg1, arg2=None):
        """
        ROUTINE:
          setAttr(attrname, newvalue), or
          setAttr(attrname, objects, newvalues)

        PURPOSE:
          Change the value(s) of an attribute.

        ARGUMENTS:
          attrname (string): The name of the requested attribute.
          objects(optional): A list of variables or constraints.
          newvalue: The desired new value.  The type of the value should be
                    compatible with the attribute type (e.g., an integer parameter
                    will take an integer value).

        RETURN VALUE:
          The attribute value.

        EXAMPLE:
          model.setAttr("modelSense", -1)
          model.setAttr("lb", [x, y, z], [1, 1, 1])

        NOTES:
          Model attributes that can be set are:
            modelName:  Model name.
            modelSense: Objective sense.

          Attributes changes are handled in a lazy fashion.  The effect of a
          change isn't visible until after the next call to Model.update() or
          Model.optimize().
        """
        pass


    def setObjective(self, expr, sense=None):
        """
        ROUTINE:
          setObjective(expression, sense=None)

        PURPOSE:
          Set the model objective equal to a LinExpr or QuadExpr

        ARGUMENTS:
          expr: The desired objective function.  The objective can be
                a linear expression (LinExpr) or a quadratic expression (QuadExpr).
                This routine will replace the 'Obj' attribute on model variables
                with the corresponding values from the supplied expression.
          sense (optional): Objective sense.  By default, this method uses the
                modelSense model attribute to determine the sense.  Use
                GRB.MINIMIZE or GRB.MAXIMIZE to ignore modelSense and pick a
                specific sense.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.setObjective(x + y)
          model.setObjective(x + y + 2*z, GRB.MAXIMIZE)
        """
        pass


    def setObjectiveN(self, expr, index, priority=0, weight=1.0, abstol=0.0, reltol=0.0, name=''):
        """
        ROUTINE:
          setObjectiveN(expression, index)

        PURPOSE:
          Set the model objective equal to a LinExpr or QuadExpr

        ARGUMENTS:
          expr:     The desired objective function.  The objective can be
                    a linear expression (LinExpr) a variable (Var) or a constant.
                    This routine will replace the 'ObjNVal' attribute on model variables
                    with the corresponding values from the supplied expression for
                    multi-objective 'index'
          index:    Identify which multi-objective to set
          priority: Set the ObjNPriority attribute for this multi-objective (default is zero)
          weight:   Set the ObjNWeight attribute for this multi-objective (default is 1.0)
          abstol:   Set the ObjNAbsTol  attribute for this multi-objective (default is zero)
          reltol:   Set the ObjNRelTol  attribute for this multi-objective (default is zero)
          name:     multi-objective name (default is no name)

        RETURN VALUE:
          None.

        EXAMPLE:
          model.setObjectiveN(x + y, 1)
          model.setObjectiveN(x + y + 2*z, 2)
        """
        pass


    def setPWLObj(self, var, x, y):
        """
        ROUTINE:
          setPWLObj(var, x, y)

        PURPOSE:
          Set a piecewise-linear objective for a variable

        ARGUMENTS:
          var: the Var whose objective is set.
          x: A list of x coordinates.
          y: A list of y coordinates.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.setPWLObj(v, [1, 2, 3], [1, 2, 4])
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
          model.setParam("NodeLimit", 100)
          model.setParam("TimeLimit", "default")

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


    def terminate(self):
        """
        ROUTINE:
          terminate()

        PURPOSE:
          Terminate any optimization in progress (from a callback).

        ARGUMENTS:
          None.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.terminate()
        """
        pass


    def tune(self):
        """
        ROUTINE:
          tune()

        PURPOSE:
          Tune parameter settings

        ARGUMENTS:
          None.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.tune()
        """
        pass


    def update(self):
        """
        ROUTINE:
          update()

        PURPOSE:
          Apply any pending changes to the model.

        ARGUMENTS:
          None.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.update()

        NOTES:
          Model modifications are handled in a lazy fashion.  A bound change, for
          example, isn't reflected in the model until the user either calls
          model.optimize() or model.update().
        """
        pass


    def write(self, filename):
        """
        ROUTINE:
          write(filename)

        PURPOSE:
          Write model data to a file.  The type of data is determined by the
          file suffix: .lp or .mps to write the model itself, .mst to write
          the current solution as a MIP start, .bas to write the current
          simplex basis, or .prm to write the modified parameters.

        ARGUMENTS:
          filename (string): The name of the file to write.

        RETURN VALUE:
          None.

        EXAMPLE:
          model.write("model.lp")
          model.write("model.mst")
        """
        pass

    # ----------------------------------------------------------------------
    # Data descriptors defined here:

    # __dict__
    # dictionary for instance variables (if defined)

    # __weakref__
    # list of weak references to the object (if defined)
