import subprocess

from AnalyzeModule.AnalysisModule.AsmAnalyzer import AsmAnalyzer
from InitializerModule.parser import Parser
from AnalysisModule.AnalysisManager import AnalysisManager
import pandas as pd
import os


def main():
    assert os.path.isdir("REPOS_SAMPLE")

    dirs = os.listdir("REPOS_SAMPLE")

    analyzer = AsmAnalyzer()

    for d in dirs:
        path = os.path.join("REPOS_SAMPLE", d)
        # compile
        subprocess.check_output(f'gcc -fopenmp -O0 *.c', cwd=path, stderr=subprocess.STDOUT,
                                shell=True, encoding='UTF-8')
        exe = os.path.join(path, "a.out")
        assert os.path.isfile(exe)

        analyzer(exe, os.path.join(path, "output.csv"), 3, False)

        os.remove(exe)


if __name__ == '__main__':
    main()
