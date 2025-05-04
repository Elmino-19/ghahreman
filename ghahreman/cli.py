#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Command-line module for displaying the trophy.

This module provides a command-line interface for displaying the trophy.

A package for champion (ghahreman) from master (ostad).
"""

import argparse
from .ghahreman_trophy import Hero


def main():
    """
    Main function for running the command-line script.

    This function processes command-line parameters and creates and displays
    a trophy with the specified parameters.
    """
    parser = argparse.ArgumentParser(description='Display the golden trophy')
    parser.add_argument('--height', type=float, default=2.0,
                        help='Height of the upper cone (default: 2.0)')
    parser.add_argument('--radius', type=float, default=1.0,
                        help='Radius of the upper cone (default: 1.0)')
    parser.add_argument('--resolution', type=int, default=60,
                        help='Resolution of the trophy elements (default: 60)')
    parser.add_argument('--background', type=str, default='white',
                        help='Background color (default: white)')
    parser.add_argument('--width', type=int, default=1000,
                        help='Width of the display window (default: 1000)')
    parser.add_argument('--height-window', type=int, default=800,
                        help='Height of the display window (default: 800)')

    args = parser.parse_args()

    # Create an instance of the Hero class with the specified parameters
    hero = Hero(
        height1=args.height,
        radius1=args.radius,
        resolution=args.resolution
    )

    # Display the trophy
    hero.display(
        background_color=args.background,
        window_size=(args.width, args.height_window)
    )

    print("Trophy displayed successfully!")


if __name__ == "__main__":
    main()
