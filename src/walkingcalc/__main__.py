from corecalc import exec
from corecalc.cli.parser import ExerciseParser

from walkingcalc.stats import WalkingStats


def main() -> str:
    """
    Entry point for the runningcalc module.

    Returns
    -------
        the summary of the runningcalc statistics.

    """
    return exec(ExerciseParser(), WalkingStats)


if __name__ == "__main__":
    print(main())
