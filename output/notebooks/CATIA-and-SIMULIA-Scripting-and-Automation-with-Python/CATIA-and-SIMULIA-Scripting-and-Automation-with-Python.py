# -*- coding: utf-8 -*-
"""
Developed by:
Neal Gordon
NobleTek
nealagordon@gmail.com

Requires a CATIA license with the Generative Part Analysis (GPS) to run
"""

# import python modules
import os
from win32com.client import Dispatch

# Connecting to windows COM 
CATIA = Dispatch('CATIA.Application')
# optional CATIA visibility
CATIA.Visible = True

# Create an empty part
partDocument1 = CATIA.Documents.Add("Part")

# Create the point that the plane and sketch reference
Xcoord=100
Ycoord=100
Zcoord=100
NewPoint = CATIA.ActiveDocument.Part.HybridShapeFactory.AddNewPointCoord(Xcoord, Ycoord, Zcoord)
Mainbody = CATIA.ActiveDocument.Part.MainBody
Mainbody.InsertHybridShape(NewPoint)

# Create reference plane for sketch
AxisXY = CATIA.ActiveDocument.Part.OriginElements.PlaneXY
Referenceplane = CATIA.ActiveDocument.Part.CreateReferenceFromObject(AxisXY)
Referencepoint = CATIA.ActiveDocument.Part.CreateReferenceFromObject(NewPoint)
NewPlane = CATIA.ActiveDocument.Part.HybridShapeFactory.AddNewPlaneOffsetPt(Referenceplane, Referencepoint)
Mainbody.InsertHybridShape(NewPlane)

# create sketch
sketches1 = CATIA.ActiveDocument.Part.Bodies.Item("PartBody").Sketches
reference1 = partDocument1.part.OriginElements.PlaneXY
NewSketch = sketches1.Add(reference1)
CATIA.ActiveDocument.Part.InWorkObject = NewSketch

#Drawing the sketch
NewSketch.OpenEdition()
#                                  Start (H,   V)  End(H,V)
NewLine1 = NewSketch.Factory2D.CreateLine(0  , 0  , 0   ,50)
NewLine2 = NewSketch.Factory2D.CreateLine(0  , 50 , 50  ,50)
NewLine3 = NewSketch.Factory2D.CreateLine(50 , 50 , 50  ,55)
NewLine4 = NewSketch.Factory2D.CreateLine(50 , 55 , 150 ,55)
NewLine5 = NewSketch.Factory2D.CreateLine(150, 55 , 150  ,-5)
NewLine6 = NewSketch.Factory2D.CreateLine(50, -5 , 50  ,0)
NewLine7 = NewSketch.Factory2D.CreateLine(50 , -5 , 75  ,-5)
NewLine8 = NewSketch.Factory2D.CreateLine(150 , -5 , 125  ,-5)
NewLine9 = NewSketch.Factory2D.CreateLine(125 , -5 , 125  ,25)
NewLine0 = NewSketch.Factory2D.CreateLine(125 , 25 , 75  ,25)
NewLine11 = NewSketch.Factory2D.CreateLine(75 , 25 , 75  ,-5)
NewLine12 = NewSketch.Factory2D.CreateLine(50 , 0  , 0   ,0)
NewSketch.CloseEdition()

# Create a pad from sketch
LengthBlock=50
NewBlock = CATIA.ActiveDocument.Part.ShapeFactory.AddNewPad (NewSketch, LengthBlock)
CATIA.ActiveDocument.Part.Update()

# Assign Material
MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
hk=CATIA.ActiveDocument.Part.MainBody
systempath= CATIA.SystemService.Environ("CATDocView")
path= "C:\\Program Files\\Dassault Systemes\\B23\win_b64\\startup\\materials\\Catalog.CATMaterial"
MatDoc=CATIA.Documents.Open(path)
oMaterial=MatDoc.Families.Item("Metal").Materials.Item("Steel")
MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
MatDoc.Close()


# Activate the Generative Structural Analysis (GPS) Workbench
PartDoc=CATIA.ActiveDocument
CATIA.StartWorkbench ("GPSCfg")
CATIA.ActiveDocument.Analysis.Import(PartDoc)
CATIA.ActiveDocument.Analysis.AnalysisModels.Item(1).RunTransition ("CATGPSStressAnalysis_template")
CATIA.ActiveWindow.ActiveViewer.Reframe ()

# Create a Mesh
mesh=CATIA.ActiveDocument.Analysis.AnalysisModels.Item(1).MeshManager.AnalysisMeshParts.Item(1)
mesh.SetGlobalSpecification ("SizeValue", "2.5 mm")
mesh.SetGlobalSpecification ("AbsoluteSag", 2)
mesh.SetGlobalSpecification ("AbsoluteSagValue", "1.0 mm")
mesh.SetGlobalSpecification ("ElementOrder", "Parabolic")
mesh.Update()

# Define Constraints
analysisSet1 = CATIA.ActiveDocument.Analysis.AnalysisModels.Item(1).AnalysisCases.Item(1).AnalysisSets.Item(1, 3)
analysisEntity1 = analysisSet1.AnalysisEntities.Add("SAMClamp")
reference1 = partDocument1.Part.CreateReferenceFromName("Selection_RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;12)));None:();Cf11:());Pad.1_ResultOUT;Last;Z0;G4720)")
analysisEntity1.AddSupportFromProduct (partDocument1.Product, reference1)

# Defining the Load
analysisSet2 = CATIA.ActiveDocument.Analysis.AnalysisModels.Item(1).AnalysisCases.Item(1).AnalysisSets.Item(2, 3)
analysisEntity2 = analysisSet2.AnalysisEntities.Add("SAMDistributedForce")
reference2 = partDocument1.Part.CreateReferenceFromName("Selection_RSur:(Face:(Brp:(Pad.1;0:(Brp:(Sketch.1;5)));None:();Cf11:());Pad.1_ResultOUT;Last;Z0;G4720)")
analysisEntity2.AddSupportFromProduct (partDocument1.Product, reference2) #partDocument1 aus "leeres Part erstellen"
basicComponent1 = analysisEntity2.BasicComponents.GetItem("SAMForceAxis.1")
basicComponent1.SetValue ("Values", 0, 0, 0, 1)
basicComponent2 = analysisEntity2.BasicComponents.GetItem("SAMForceVector.1")
basicComponent2.SetDimensions (3, 1, 1)
basicComponent2.SetValue ("Values", 1, 1, 1, 1000.0)
basicComponent2.SetValue ("Values", 2, 1, 1, 1000.0)
basicComponent2.SetValue ("Values", 3, 1, 1, 1000.0)

# Perform Calculation
print('Performing Calculaution')
CATIA.ActiveDocument.Analysis.AnalysisModels.Item(1).AnalysisCases.Item(1).Compute()
print('Calculaution Complete')

# Export text file with von-mises stress
analysisSet1 = CATIA.ActiveDocument.Analysis.AnalysisModels.Item(1).AnalysisCases.Item(1).AnalysisSets.Item(3, 3)
analysisImage1 = analysisSet1.AnalysisImages.Add("StressVonMises_Iso_Smooth", True, False, False)
Folder = CATIA.FileSystem.GetFolder(os.getcwd())
analysisImage1.ExportDataInGlobalAxis(Folder, "mises", "txt", 0, False)
print("Created stress text file")

