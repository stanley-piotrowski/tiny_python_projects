#!/usr/bin/env python3
"""
Author: Stanley Piotrowski <stanley.piotrowski@gmail.com>
Purpose: Say hello
"""

import argparse

# -----------------------------------------------------------------------
def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument("-n", "--name", metavar="name",
                        default="World", help="Name to greet")

    return parser.parse_args()

# -------------------------------------------------------------------------
def main():
    """Define the main function"""

    args = get_args() # Call this function to get the parsed arguments
    print("Hello, " + args.name + "!")

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()