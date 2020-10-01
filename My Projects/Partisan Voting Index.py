import csv
import numpy as np
import pandas as pd

DEM1 = int(input("DEM votes from first election: "))
REP1 = int(input("DEM votes from first election: "))
DEM2 = int(input("REP votes from second election: "))
REP2 = int(input("REP votes from second election: "))

DEM_US1 = int(input("DEM USA votes from first election: "))
REP_US1 = int(input("REP USA votes from first election: "))
DEM_US2 = int(input("DEM USA votes from second election: "))
REP_US2 = int(input("REP USA votes from second election: "))

D_percent1 = (DEM1/(DEM1+REP1))*100
D_percent2 = (DEM2/(DEM2+REP2))*100
R_percent1 = (REP1/(DEM1+REP1))*100
R_percent2 = (REP2/(DEM2+REP2))*100

D_USA_percent1 = (DEM_US1/(DEM_US1+REP_US1))*100
D_USA_percent2 = (DEM_US2/(DEM_US2+REP_US2))*100
R_USA_percent1 = (REP_US1/(DEM_US1+REP_US1))*100
R_USA_percent2 = (REP_US2/(DEM_US2+REP_US2))*100

DEM_PVI = ((D_percent1+D_percent2)/2) - ((D_USA_percent1+D_USA_percent2)/2)
REP_PVI = ((R_percent1+R_percent2)/2) - ((R_USA_percent1+R_USA_percent2)/2)

print("D+", round(DEM_PVI, 2),sep='')
print("R+", round(REP_PVI, 2),sep='')
