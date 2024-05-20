import argparse
import os
from rich.console import Console
from rich.table import Table, Column
from rich.panel import Panel
from cron_parser import CronParser
from logging_config import logger

PROGRAM_DESCRIPTION = """
This program parses a cron string and expands each field
to show the times at which it will run.

Take for example, this cron string:

    */15 0 1,15 * 1-5 /usr/bin/find

The above cron string will yield the following output:

minute            0 15 30 45
hour              0
day of month      1 15
month             1 2 3 4 5 6 7 8 9 10 11 12
day of week       1 2 3 4 5
command           /usr/bin/find
"""

def main():
    logger.info("Cron parser started...")

    parser = argparse.ArgumentParser(description=PROGRAM_DESCRIPTION)
    parser.add_argument('cron_str', type=str, help='Cron string to be parsed.')
    args = parser.parse_args()

    cron_parser = CronParser(args.cron_str)
    parsed_fields = cron_parser.parse()

    console = Console()
    table = Table(title="Cron Parsing Results:", title_style="bold magenta")
    table.add_column("Cron Fields", style="bold cyan", header_style="bold blue", width=20)
    table.add_column("Expanded Values", style="bold green", header_style="bold blue")

    for name, times in parsed_fields.items():
        if name == "day of week":
            # Handle special formatting for nth day of week
            formatted_times = ' '.join([f"{t[0]}#{t[1]}" if isinstance(t, tuple) else str(t) for t in times])
            table.add_row(name, formatted_times)
        else:
            table.add_row(name, ' '.join(map(str, times)) if isinstance(times, list) else times)

    panel = Panel.fit(table, title="Parsed Cron Fields", title_align="left", border_style="bright_yellow")
    console.print(panel)

    logger.info("Cron parser executed !")

if __name__ == "__main__":
    main()
