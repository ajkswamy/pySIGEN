from pySIGEN.sigenWrapper import runSIGEN, runSIGENSmoothing
from tempfile import TemporaryDirectory
from pySIGEN.auxFuncs import tifStack2ImageSeq
import pathlib
from filecmp import cmp

testFilesPath = pathlib.Path("tests/testFiles")


def sigenOutputEquivalence(file1, file2):
    with open(file1, "r") as exof:
        expOpStr = exof.read()

    with open(file2, 'r') as testof:
        testOpStr = testof.read()

    diffLines = []
    for exLine, testLine in zip(expOpStr.split("\n"), testOpStr.split("\n")):
        if exLine != testLine:
            diffLines.append((exLine, testLine))

    equivalence = len(diffLines) == 1 and diffLines[0][0].startswith("# RAW") and diffLines[0][1].startswith("# RAW")
    return equivalence, diffLines

def sigenWrapper_test():

    "Testing SIGEN with default parameters"
    testImage = str(testFilesPath / "GMR_57C10_AD_01-Two_recombinase_flipouts_A-m-A-20111103_3.tif")
    tempDir = TemporaryDirectory(dir=str(testFilesPath))
    tifStack2ImageSeq(testImage, tempDir.name)
    testOutput = str(testFilesPath/"testOutput.swc")

    if pathlib.os.path.isfile(testOutput):
        pathlib.os.remove(testOutput)
    runSIGEN(inDir=tempDir.name,
             outFile=testOutput,
             VT=0,
             DT=0,
             C=0,
             S=0,
             XY_scale=1.0,
             Z_scale=1.0,
             threshold=128
             )
    expectedOutput = str(testFilesPath / "expectedOutput_default.swc")

    eq, testLines = sigenOutputEquivalence(expectedOutput, testOutput)

    assert eq

def sigenWrapperXY_test():

    "Testing parameters XY_scale of SIGEN"

    testImage = str(testFilesPath / "GMR_57C10_AD_01-Two_recombinase_flipouts_A-m-A-20111103_3.tif")
    tempDir = TemporaryDirectory(dir=str(testFilesPath))
    tifStack2ImageSeq(testImage, tempDir.name)
    testOutput = str(testFilesPath/"testOutput_X2.swc")

    if pathlib.os.path.isfile(testOutput):
        pathlib.os.remove(testOutput)
    runSIGEN(inDir=tempDir.name,
             outFile=testOutput,
             VT=0,
             DT=0,
             C=0,
             S=0,
             XY_scale=2.0,
             Z_scale=1.0,
             threshold=128
             )
    expectedOutput = str(testFilesPath / "expectedOutput_X2.swc")

    eq, testLines = sigenOutputEquivalence(expectedOutput, testOutput)

    assert eq

def sigenWrapperZ_test():
    "Testing parameters Z_scale of SIGEN"

    testImage = str(testFilesPath / "GMR_57C10_AD_01-Two_recombinase_flipouts_A-m-A-20111103_3.tif")
    tempDir = TemporaryDirectory(dir=str(testFilesPath))
    tifStack2ImageSeq(testImage, tempDir.name)
    testOutput = str(testFilesPath / "testOutput_Z2.swc")

    if pathlib.os.path.isfile(testOutput):
        pathlib.os.remove(testOutput)
    runSIGEN(inDir=tempDir.name,
             outFile=testOutput,
             VT=0,
             DT=0,
             C=0,
             S=0,
             XY_scale=1.0,
             Z_scale=2.0,
             threshold=128
             )
    expectedOutput = str(testFilesPath / "expectedOutput_Z2.swc")

    eq, testLines = sigenOutputEquivalence(expectedOutput, testOutput)

    assert eq

def sigenWrapperDT_test():
    "Testing parameters DT of SIGEN"

    testImage = str(testFilesPath / "GMR_57C10_AD_01-Two_recombinase_flipouts_A-m-A-20111103_3.tif")
    tempDir = TemporaryDirectory(dir=str(testFilesPath))
    tifStack2ImageSeq(testImage, tempDir.name)
    testOutput = str(testFilesPath / "testOutput_DT5.swc")

    if pathlib.os.path.isfile(testOutput):
        pathlib.os.remove(testOutput)
    runSIGEN(inDir=tempDir.name,
             outFile=testOutput,
             VT=0,
             DT=5,
             C=0,
             S=0,
             XY_scale=1.0,
             Z_scale=1.0,
             threshold=128
             )
    expectedOutput = str(testFilesPath / "expectedOutput_DT5.swc")

    eq, testLines = sigenOutputEquivalence(expectedOutput, testOutput)

    assert eq

def sigenWrapperVT_test():
    "Testing parameters VT of SIGEN"

    testImage = str(testFilesPath / "GMR_57C10_AD_01-Two_recombinase_flipouts_A-m-A-20111103_3.tif")
    tempDir = TemporaryDirectory(dir=str(testFilesPath))
    tifStack2ImageSeq(testImage, tempDir.name)
    testOutput = str(testFilesPath / "testOutput_VT5.swc")

    if pathlib.os.path.isfile(testOutput):
        pathlib.os.remove(testOutput)
    runSIGEN(inDir=tempDir.name,
             outFile=testOutput,
             VT=5,
             DT=0,
             C=0,
             S=0,
             XY_scale=1.0,
             Z_scale=1.0,
             threshold=128
             )
    expectedOutput = str(testFilesPath / "expectedOutput_VT5.swc")

    eq, testLines = sigenOutputEquivalence(expectedOutput, testOutput)

    assert eq

def sigenWrapperC_test():
    "Testing parameters C of SIGEN"

    testImage = str(testFilesPath / "GMR_57C10_AD_01-Two_recombinase_flipouts_A-m-A-20111103_3.tif")
    tempDir = TemporaryDirectory(dir=str(testFilesPath))
    tifStack2ImageSeq(testImage, tempDir.name)
    testOutput = str(testFilesPath / "testOutput_C5.swc")

    if pathlib.os.path.isfile(testOutput):
        pathlib.os.remove(testOutput)
    runSIGEN(inDir=tempDir.name,
             outFile=testOutput,
             VT=0,
             DT=0,
             C=5,
             S=0,
             XY_scale=1.0,
             Z_scale=1.0,
             threshold=128
             )
    expectedOutput = str(testFilesPath / "expectedOutput_C5.swc")

    eq, testLines = sigenOutputEquivalence(expectedOutput, testOutput)

    assert eq

def sigenWrapperS_test():
    "Testing parameters S of SIGEN"

    testImage = str(testFilesPath / "GMR_57C10_AD_01-Two_recombinase_flipouts_A-m-A-20111103_3.tif")
    tempDir = TemporaryDirectory(dir=str(testFilesPath))
    tifStack2ImageSeq(testImage, tempDir.name)
    testOutput = str(testFilesPath / "testOutput_S5.swc")

    if pathlib.os.path.isfile(testOutput):
        pathlib.os.remove(testOutput)
    runSIGEN(inDir=tempDir.name,
             outFile=testOutput,
             VT=0,
             DT=0,
             C=0,
             S=5,
             XY_scale=1.0,
             Z_scale=1.0,
             threshold=128
             )
    expectedOutput = str(testFilesPath / "expectedOutput_S5.swc")

    eq, testLines = sigenOutputEquivalence(expectedOutput, testOutput)

    assert eq

def sigenWrapperB_test():
    "Testing parameters B of SIGEN"

    testImage = str(testFilesPath / "GMR_57C10_AD_01-Two_recombinase_flipouts_A-m-A-20111103_3.tif")
    tempDir = TemporaryDirectory(dir=str(testFilesPath))
    tifStack2ImageSeq(testImage, tempDir.name)
    testOutput = str(testFilesPath / "testOutput_B100.swc")

    if pathlib.os.path.isfile(testOutput):
        pathlib.os.remove(testOutput)
    runSIGEN(inDir=tempDir.name,
             outFile=testOutput,
             VT=0,
             DT=0,
             C=0,
             S=0,
             XY_scale=1.0,
             Z_scale=1.0,
             threshold=100
             )
    expectedOutput = str(testFilesPath / "expectedOutput_B100.swc")

    eq, testLines = sigenOutputEquivalence(expectedOutput, testOutput)

    assert eq

def sigenSmoothing_test():

    testSWC = str(testFilesPath / "expectedOutput.swc")
    smoothingLevel = 5
    testOutput = str(testFilesPath / "expectedOutput_S05.swc")
    expectedOutput = str(testFilesPath / "expectedOutput_S05HandMade.swc")

    runSIGENSmoothing(testSWC, testOutput, smoothingLevel)
    assert cmp(testOutput, expectedOutput)







