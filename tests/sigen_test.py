from pySIGEN.sigenWrapper import runSIGEN, runSIGENSmoothing
from tempfile import TemporaryDirectory
from pySIGEN.auxFuncs import tifStack2ImageSeq
import pathlib
from filecmp import cmp

testFilesPath = pathlib.Path("tests/testFiles")

def sigenWrapper_test():

    testImage = str(testFilesPath / "GMR_57C10_AD_01-Two_recombinase_flipouts_A-m-A-20111103_3.tif")
    tempDir = TemporaryDirectory(dir=str(testFilesPath))
    tifStack2ImageSeq(testImage, tempDir.name)
    testOutput = str(testFilesPath/"testOutput.swc")

    if pathlib.os.path.isfile(testOutput):
        pathlib.os.remove(testOutput)
    runSIGEN(inDir=tempDir.name,
             outFile=testOutput,
             VT=5,
             DT=0,
             C=0,
             S=0)
    expectedOutput = str(testFilesPath / "expectedOutput.swc")


    with open(expectedOutput, "r") as exof:
        expOpStr = exof.read()

    with open(testOutput, 'r') as testof:
        testOpStr = testof.read()

    diffLines = []
    for exLine, testLine in zip(expOpStr.split("\n"), testOpStr.split("\n")):
            if exLine != testLine:
                diffLines.append((exLine, testLine))

    assert len(diffLines) == 1 and diffLines[0][0].startswith("# RAW") and diffLines[0][1].startswith("# RAW")


def sigenSmoothing_test():

    testSWC = str(testFilesPath / "expectedOutput.swc")
    smoothingLevel = 5
    testOutput = str(testFilesPath / "expectedOutput_S05.swc")
    expectedOutput = str(testFilesPath / "expectedOutput_S05HandMade.swc")

    runSIGENSmoothing(testSWC, testOutput, smoothingLevel)
    assert cmp(testOutput, expectedOutput)

