#!/usr/bin/env python3

import unittest
import sys
import os

from raw_data_parsers.play_by_play.play import get_play_type, get_scoring_type


class TestPlayByPlay(unittest.TestCase):

    def __set_play_consts(self):
        """Set plays to be used by the play tests."""
        # General Plays
        self.plays = (
            # Punt
            "Isaac Newton punts 52 yards, returned by Gottfried Wilhelm von Leibniz for -7 yards (tackle by Royal Society)",
            # Two point conversion with incomplete pass
            "Two Point Attempt: Saul Perlmutter pass incomplete, conversion fails. Penalty on SFO : Illegal Touch Pass (Declined)",
            # Two point conversion with complete pass
            "Two Point Attempt: Wolfgang Amadeus Mozart pass complete to Antonio Salieri, conversion succeeds",
            # Two point conversion with run
            "Two Point Attempt: Pheidippides up the middle, conversion succeeds",
            # Kick off
            "Julius Caesar kicks off 70 yards, muffed catch by Mark Antony, recovered by Gaius Octavius and returned for no gain",
            # Onside kick
            "Neville Chamberlain kicks onside, recovered by the Axis.",
            # Sack
            "Nikolai Yezhov sacked by Joseph Stalin and Ivan Serov for -7 yards",
            # Field Goal
            "Albert Einstein 52 yard field goal no good",
            # Incomplete pass
            "Antinous pass incomplete short middle intended for Penelope. (defended by Odysseus).  Penalty on Odysseus: Defensive Pass Interference, 9 yards (no play)",
            # Pass complete
            "Bill Gates pass complete short right to Steve Ballmer for 9 yards (tackle by Steve Jobs)",
            # Extra point
            "Bruce Springsteen kicks extra point good",
            # Timeout
            "Timeout #1 by The E Street Band",
            # Kneel
            "Superman kneels before Zod for -1 yards",
            # Spike
            "Arthur C. Clarke spiked the ball",
            # Aborted snap
            "Aborted snap. G. Khan fumbles, recovered by K. Tolui at EUR -23 (tackled by Ögödei Kahn ).",
            # Run
            "Isaac Asimov up the middle for 11 yards (tackle by Ray Bradbury)",
            # Not a play
            "What are you even talking about?",
            # Not a play
            "--",
        )

        # Scoring Plays
        self.scoring = (
            # Extra point
            "Edson Arantes do Nascimento (Pelé) kicks extra point good",
            # Kickoff touchdown
            "Sauron punts 52 yards, returned by Frodo for 90 yards, touchdown",
            # Passing touchdown
            "Abraham Lincoln pass complete deep right to Andrew Johnson for 59 yards, touchdown",
            # Safety
            "Hephaestus for no gain. Ares fumbles, recovered by Aphrodite at OLY --8, safety.  Penalty on Hephaestus : Illegal Motion (Declined)",
            # Two point conversion
            "Two Point Attempt: George Washington pass complete to John Adams, conversion succeeds",
            # Field goal
            "Perseus 31 yard field goal good",
            # Not a scoring play
            "Paul McCartney pass incomplete short right intended for Ringo Starr (defended by George Harrison).  Penalty on John Lennon : Defensive Pass Interference, 4 yards (no play)",
        )

    def test_get_play_type(self):
        self.__set_play_consts()
        # Successful
        self.assertEqual(
                get_play_type(self.plays[0]),
                "punt"
                )
        self.assertEqual(
                get_play_type(self.plays[1]),
                "two point conversion with incomplete pass"
                )
        self.assertEqual(
                get_play_type(self.plays[2]),
                "two point conversion with complete pass"
                )
        self.assertEqual(
                get_play_type(self.plays[3]),
                "two point conversion with run"
                )
        self.assertEqual(
                get_play_type(self.plays[4]),
                "kick off"
                )
        self.assertEqual(
                get_play_type(self.plays[5]),
                "onside kick"
                )
        self.assertEqual(
                get_play_type(self.plays[6]),
                "sack"
                )
        self.assertEqual(
                get_play_type(self.plays[7]),
                "field goal"
                )
        self.assertEqual(
                get_play_type(self.plays[8]),
                "incomplete pass"
                )
        self.assertEqual(
                get_play_type(self.plays[9]),
                "complete pass"
                )
        self.assertEqual(
                get_play_type(self.plays[10]),
                "extra point"
                )
        self.assertEqual(
                get_play_type(self.plays[11]),
                "timeout"
                )
        self.assertEqual(
                get_play_type(self.plays[12]),
                "kneel"
                )
        self.assertEqual(
                get_play_type(self.plays[13]),
                "spike"
                )
        self.assertEqual(
                get_play_type(self.plays[14]),
                "aborted snap"
                )
        self.assertEqual(
                get_play_type(self.plays[15]),
                "run"
                )
        # We squelch the warning from this test, we want the warning when
        # running on data, but not when testing
        with open(os.devnull, 'w') as f:
            oldstdout = sys.stdout
            sys.stdout = f
            self.assertEqual(
                    get_play_type(self.plays[16]),
                    None
                    )
            self.assertEqual(
                    get_play_type(self.plays[17]),
                    None
                    )
            # Return stdout
            sys.stdout = oldstdout

    def test_get_score_type(self):
        self.__set_play_consts()
        # Successful
        self.assertEqual(
                get_scoring_type(self.scoring[0]),
                "extra point"
                )
        self.assertEqual(
                get_scoring_type(self.scoring[1]),
                "touchdown"
                )
        self.assertEqual(
                get_scoring_type(self.scoring[2]),
                "touchdown"
                )
        self.assertEqual(
                get_scoring_type(self.scoring[3]),
                "safety"
                )
        self.assertEqual(
                get_scoring_type(self.scoring[4]),
                "two point conversion"
                )
        self.assertEqual(
                get_scoring_type(self.scoring[5]),
                "field goal"
                )
        # We squelch the warning from this test, we want the warning when
        # running on data, but not when testing
        with open(os.devnull, 'w') as f:
            oldstdout = sys.stdout
            sys.stdout = f
            self.assertEqual(
                    get_scoring_type(self.scoring[6]),
                    None
                    )
            # Return stdout
            sys.stdout = oldstdout


if __name__ == '__main__':
    unittest.main()
