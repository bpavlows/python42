#!/usr/bin/env python3
import sys


def ft_score_analytics(args: list[int]):
    total_players = len(args)
    total_score = sum(args)
    if total_players > 0:
        print(f"Scores processed: {args}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {total_score/total_players}")
        print(f"High score: {max(args)}")
        print(f"Low score: {min(args)}")
        print(f"Score range: {max(args)-min(args)}")
    else:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )


def main() -> None:
    print("=== Player Score Analytics ===")
    valid_scores: list[int] = []
    for item in sys.argv[1:]:
        try:
            valid_scores = valid_scores + [int(item)]
        except ValueError:
            print(f"Invalid parameter: '{item}'")
            pass
    ft_score_analytics(valid_scores)


if __name__ == "__main__":
    main()
