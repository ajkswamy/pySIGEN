import subprocess
from .executables import sigenMorphExtractor, sigenSmoothing
import logging
from .auxFuncs import log_subprocess_output


def runSIGEN(inDir: str, outFile: str, VT: int, DT: int, C: int, S: int,
             XY_scale: float, Z_scale: float, threshold: int):

    toRun = [
              "mono", sigenMorphExtractor,
              "-i", inDir,
              "-o", outFile,
              "-t", "1",
              "-v", str(VT),
              "-d", str(DT),
              "-a", str(C),
              "-s", str(S),
              "-x", str(XY_scale),
              "-z", str(Z_scale),
              "-b", str(threshold)
            ]

    logging.info("[runSIGEN] Running {}".format(toRun))
    compProc = subprocess.run(toRun,
                   timeout=30 * 60,
                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log_subprocess_output(compProc.stdout, "SIGENMorphExtractor")


def runSIGENSmoothing(inFile: str, outFile: str, smoothingLevel: int):


    toRun = [
        "mono", sigenSmoothing,
        inFile, outFile, str(smoothingLevel)
    ]

    logging.info("[runSIGENSmoothing] Running {}".format(toRun))
    compProc = subprocess.run(toRun,
                              timeout=30 * 60,
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log_subprocess_output(compProc.stdout, "SIGENSmoothing")