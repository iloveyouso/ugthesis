# def generate_apdl_script(circle_data):
#     num_circles = circle_data[0]
#     circles = circle_data[1:]
    
#     script = f"""
# /NOPR   
# KEYW,PR_SET,1   
# KEYW,PR_STRUC,1 
# KEYW,PR_THERM,0 
# KEYW,PR_FLUID,0 
# KEYW,PR_ELMAG,0 
# KEYW,MAGNOD,0   
# KEYW,MAGEDG,0   
# KEYW,MAGHFE,0   
# KEYW,MAGELC,0   
# KEYW,PR_MULTI,0 
# /GO 
# !*  
# /COM,   
# /COM,Preferences for GUI filtering have been set to display:
# /COM,  Structural   
# !*  
# /PREP7  
# !*  
# ET,1,PLANE182   
# !*  
# KEYOPT,1,1,0
# KEYOPT,1,3,3
# KEYOPT,1,6,0
# !*  
# !*  
# R,1,50, 
# !*  
# !*  
# MPTEMP,,,,,,,,  
# MPTEMP,1,0  
# MPDATA,EX,1,,2e5
# MPDATA,PRXY,1,,0.3  
# ! MATERIAL PROPERTIES: Young's modulus: 2e5 N/mm, Poisson: 0.3
# BLC5,0,0,3000,1000  
# SAVE

# ! MODELING: Draw circles and extrude them
# """
#     for circle in circles:
#         x, y, r = circle
#         script += f"CYL4,{x},{y},{r}\n"

#     script += f"""
# FLST,3,{num_circles},5,ORDE,2   
# FITEM,3,2   
# FITEM,3,-{num_circles + 1}  
# ASBA,       1,P51X 
# FINISH  

# ! MESHING
# /SOL
# FINISH  
# /PREP7  
# SMRT,6
# MSHAPE,0,2D 
# MSHKEY,0
# !*  
# CM,_Y,AREA  
# ASEL, , , , {num_circles + 2}
# CM,_Y1,AREA 
# CHKMSH,'AREA'   
# CMSEL,S,_Y  
# !*  
# AMESH,_Y1   
# !*  
# CMDELE,_Y   
# CMDELE,_Y1  
# CMDELE,_Y2  
# !* 
# FINISH

# ! CONSTRAINT for DOF x, y , on the left line
# /SOL
# FLST,2,1,4,ORDE,1   
# FITEM,2,4   
# !*  
# /GO 
# DL,P51X, ,ALL,  

# ! LOADS
# FLST,2,1,4,ORDE,1   
# FITEM,2,2   
# /GO 
# !*  
# SFL,P51X,PRES,10,
# ! pressure is 10Pa/mm^2  

# ! ANALYSIS FOR BUCKLING
# ANTYPE,1
# !*  
# BUCOPT,LANB,1,0,0,CENTER
# !*  
# OUTPR,BASIC,ALL,
# MXPAND,1,0,0,1,0.001,   
# /STATUS,SOLU
# SOLVE    

# ! RESULTS: Von Mises, nodal solution
# /POST1  
# SET, LAST
# !*  
# /EFACET,1   
# PLNSOL, S,EQV, 0,1.0
# """
    
#     with open("log_generator.apdl", "w") as file:
#         file.write(script)
        
# if __name__ == "__main__":
#     circle_data = [7, [60, 0, 25], [0, 0, 25], [-60, 0, 25], [60, 100, 25], [160, 100, 25], [160, 160, 25], [220, 220, 20]]
#     # circle_data = [5, [50, 50, 30], [100, 100, 40], [150, 150, 50], [200, 200, 60], [250, 250, 70]]
#     generate_apdl_script(circle_data)

def generate_apdl_script(circle_data):
    num_circles = circle_data[0]
    circles = circle_data[1:]
    
    script = f"""
/NOPR   
KEYW,PR_SET,1   
KEYW,PR_STRUC,1 
KEYW,PR_THERM,0 
KEYW,PR_FLUID,0 
KEYW,PR_ELMAG,0 
KEYW,MAGNOD,0   
KEYW,MAGEDG,0   
KEYW,MAGHFE,0   
KEYW,MAGELC,0   
KEYW,PR_MULTI,0 
/GO 
!*  
/COM,   
/COM,Preferences for GUI filtering have been set to display:
/COM,  Structural   
!*  
/PREP7  
!*  
ET,1,PLANE182   
!*  
KEYOPT,1,1,0
KEYOPT,1,3,3
KEYOPT,1,6,0
!*  
!*  
R,1,50, 
!*  
!*  
MPTEMP,,,,,,,,  
MPTEMP,1,0  
MPDATA,EX,1,,2e5
MPDATA,PRXY,1,,0.3  
! MATERIAL PROPERTIES: Young's modulus: 2e5 N/mm, Poisson: 0.3
BLC5,0,0,3000,1000  
SAVE

! MODELING: Draw circles and extrude them
"""
    for circle in circles:
        x, y, r = circle
        script += f"CYL4,{x},{y},{r}\n"

    script += f"""
FLST,3,{num_circles},5,ORDE,2   
FITEM,3,2   
FITEM,3,-{num_circles + 1}  
ASBA,       1,P51X 
FINISH  

! MESHING
/SOL
FINISH  
/PREP7  
SMRT,6
MSHAPE,0,2D 
MSHKEY,0
!*  
CM,_Y,AREA  
ASEL, , , , {num_circles + 2}
CM,_Y1,AREA 
CHKMSH,'AREA'   
CMSEL,S,_Y  
!*  
AMESH,_Y1   
!*  
CMDELE,_Y   
CMDELE,_Y1  
CMDELE,_Y2  
!* 
FINISH

! CONSTRAINT for DOF x, y , on the left line
/SOL
FLST,2,1,4,ORDE,1   
FITEM,2,4   
!*  
/GO 
DL,P51X, ,ALL,  

! LOADS
FLST,2,1,4,ORDE,1   
FITEM,2,2   
/GO 
!*  
SFL,P51X,PRES,10,
! pressure is 10Pa/mm^2  

! ANALYSIS FOR STATIC: for prestress
/STATUS,SOLU
SOLVE

! RESULTS: Von Mises, nodal solution
/POST1  
SET, LAST
!*  
/EFACET,1   
PLNSOL, S,EQV, 0,1.0


! ANLYSIS FOR BUCKLING
/SOL
!*  
ANTYPE,1
!*  
BUCOPT,LANB,1,0,0,CENTER
!*  
OUTPR,BASIC,ALL,
MXPAND,1,0,0,1,0.001, 
/STATUS,SOLU
SOLVE   

! RESULTS: Von Mises, nodal solution
/POST1  
SET, LAST
!*  
/EFACET,1   
PLNSOL, S,EQV, 0,1.0
"""
    
    with open("APDL_scipt.apdl", "w") as file:
        file.write(script)
    
    print("APDL script generated. file name: APDL_scipt.apdl" )
        
if __name__ == "__main__":
    # 새로운 원 데이터를 사용합니다.
    circle_data = [7, [60, 0, 25], [0, 0, 25], [-60, 0, 25], [60, 100, 25], [160, 100, 25], [160, 160, 25], [220, 220, 20]]
    # circle_data = [5, [50, 50, 30], [100, 100, 40], [150, 150, 50], [200, 200, 60], [250, 250, 70]]
    generate_apdl_script(circle_data)