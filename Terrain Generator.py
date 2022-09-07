Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import maya.cmds as cmds
from random import uniform as rand

#Providing initial defults for range variables
RIValueX=0.0
RIValueZ=0.0
RIValueH=0.0
RIValueD=0.0
FreqInd=0
ComponentType=0
PW=1.0
PH=1.0
SH=10
SW=10


#Let's create a window for UI
if cmds.window("WinTerrain",exists=True,bgc=(0,1,0)):
    cmds.deleteUI("WinTerrain")

DeformWin=cmds.window("WinTerrain",t="terrain generator",w=450,h=250)
cmds.columnLayout()
cmds.text("Set the size of the plane to create, if needed")
PScaleX=cmds.floatSliderGrp(l='X Size',f=True,min=1,max=100,v=1,cc="PW=cmds.floatSliderGrp(PScaleX,q=True,v=True)")
PScaleZ=cmds.floatSliderGrp(l='Z Size',f=True,min=1,max=100,v=1,cc="PH=cmds.floatSliderGrp(PScaleZ,q=True,v=True)")
cmds.text("Set the size of the plane to create, if needed")
SubDH=cmds.floatSliderGrp(l='H Subdivisions',f=True,min=1,max=100,v=10,cc="SH=cmds.floatSliderGrp(SubDH,q=True,v=True)")
SubDW=cmds.floatSliderGrp(l='W Subdivisions',f=True,min=1,max=100,v=10,cc="SW=cmds.floatSliderGrp(SubDW,q=True,v=True)")
cmds.rowColumnLayout(nc=2)
cmds.button(l='Create plane',w=100,h=40,c="CreatePlane()")
cmds.button(l='Delete plane',w=100,h=40,c="DeletePlane()",align='right')
cmds.setParent('..')
cmds.separator(w=450,bgc=(100,0,0))
cmds.text("Please provide the range you desire")
RIUserX=cmds.floatSliderGrp(l="Range for X",f=True,min=0,max=10,v=0,cc="RIValueX=cmds.floatSliderGrp(RIUserX,q=True,v=True)")
RIUserZ=cmds.floatSliderGrp(l="Range for Z",f=True,min=0,max=10,v=0,cc="RIValueZ=cmds.floatSliderGrp(RIUserZ,q=True,v=True)")
RIUserH=cmds.floatSliderGrp(l="Range for H",f=True,min=0,max=10,v=0,cc="RIValueH=cmds.floatSliderGrp(RIUserH,q=True,v=True)")
RIUserD=cmds.floatSliderGrp(l="Range for D",f=True,min=-10,max=0,v=0,cc="RIValueD=cmds.floatSliderGrp(RIUserD,q=True,v=True)")
cmds.separator(w=450,bgc=(100,0,0))
cmds.text("Please indicate the frequency of noise. higher the number, bigger the area")
FreqUser=cmds.intSliderGrp(l="Frequency Indicator",f=True,min=0,max=500,v=50,cc="FreqInd=cmds.intSliderGrp(FreqUser,q=True,v=True)")
cmds.separator(w=450,bgc=(100,0,0))
cmds.text("Choose based on what component you like to deform")
cmds.radioCollection()
cmds.radioButton(l="Vertex",cc="ComponentType=0",sl=True)
cmds.radioButton(l="Edges",cc="ComponentType=1")
cmds.radioButton(l="Faces",cc="ComponentType=2")
cmds.radioButton(l="Selection",cc="ComponentType=4")
cmds.separator(w=450)
cmds.button(l="Deform",w=100,h=40,c="DeformOBJ()")
cmds.showWindow()


#Start of functions
def DeformOBJ():
    cmds.softSelect(sse=1)
    #Here we identify the component type based on ComponentType value
    if ComponentType==0:
        cmds.ConvertSelectionToVertices()
        AllComp=cmds.ls(sl=True,fl=True)
    elif ComponentType==1:
        cmds.ConvertSelectionToEdges()
        AllComp=cmds.ls(sl=True,fl=True)
    elif ComponentType==2:
        cmds.ConvertSelectionToFaces()
        AllComp=cmds.ls(sl=True,fl=True)
    else:
        AllComp=cmds.ls(sl=True,fl=True)
    print (AllComp)
    
    #At this point we are just deforming 
    for i in range (0,len(AllComp),FreqInd):
        RandSelection=int(rand(0,len(AllComp)))
        cmds.select(cl=True)
        singleComp=AllComp[RandSelection]
        cmds.select(singleComp)
        RandX=rand(-RIValueX,RIValueX)
        RandZ=rand(-RIValueZ,RIValueZ)
        RandY=rand(RIValueD,RIValueH)
        cmds.move(RandX,RandY,RandZ,r=True)

def CreatePlane():
    cmds.polyPlane(n='Land',w=PW,h=PH,sh=SH,sw=SW)

def DeletePlane():
    cmds.delete('Land'+'*')










