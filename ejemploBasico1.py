# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from ortools.linear_solver import pywraplp

def LPExample():
    
    solver = pywraplp.Solver.CreateSolver('CLP')
    
    x1 = solver.NumVar(0, solver.infinity(), 'x1')
    x2 = solver.NumVar(0, solver.infinity(), 'x2')
    
    print('Numero de varaibles = ', solver.NumVariables())
    
    r1 = solver.Add(0.5*x1 + x2 <= 12.0, 'Humo')
    r2 = solver.Add(x1 + x2 <= 20.0, 'Carga')
    r3 = solver.Add(1.5*x1 + x2 <= 24.0, 'Pulverizador')
    r4 = solver.Add(1200*x1 -800*x2 >= 0.0, 'Azufre')
    
    
    r3 = solver.Constraint(0,20.0, 'Pulverizador')
    r3.SetCoefficient(x1, 1.5)
    r3.SetCoefficient(x2, 1.0)
    
    z = 24*x1 + 20*x2
    
    solver.Maximize(z)
    
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        objetive = solver.Objetive()
        print('Solucion: ')
        print('Objetive value: ', solver.Objetive().Value())
        print('x1 =  ', x1.solution_value())
        print('x2 =  ', x2.solution_value())
        
    