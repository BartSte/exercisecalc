from corecalc import exec
from corecalc.cli.parser import ExerciseParser

from runningcalc.stats import RunningStats


def main() -> str:
    """
    Entry point for the runningcalc module.

    Returns
    -------
        the summary of the runningcalc statistics.

    """
    return exec(ExerciseParser(), RunningStats)


if __name__ == "__main__":
    print(main())
