# Rowing Split Calculator

A Python command-line tool that calculates average rowing pace
per 500 meters from distance and total time.

## Features

- Accepts distance in meters and time as minutes:seconds.
- Displays average split as minutes:seconds per 500 meters.
- Rounds the split to the nearest second.
- Checks for invalid input, nonpositive distance, and invalid time values.

## Requirements

Python 3. No additional packages required.

## How to run

Open a terminal in the project folder and run:

```bash
python3 rowing_split.py
```

Enter the distance and total time when prompted.
For 8 minutes and 20 seconds, enter 8:20.

## Example

```text
Distance (meters): 2000
Total time (minutes:seconds): 8:20
Average split: 2:05 /500m
```

## Calculation

Convert elapsed time to seconds, then calculate:

Average split in seconds = total seconds × 500 ÷ distance in meters

Round to the nearest second and format as minutes:seconds.

## Example checks

| Distance | Time | Expected result |
|---|---|---|
| 2000 | 8:20 | 2:05 /500m |
| 500 | 2:05 | 2:05 /500m |
| 0 | 8:20 | Distance error |
| 2000 | 8:75 | Seconds error |
| 2000 | 0:00 | Total-time error |
| 2000 | hello | Input-format error |

## What I practiced

- Collecting and converting user input.
- Splitting a time string into minutes and seconds.
- Handling conversion errors with try and except.
- Validating values with conditional statements.
- Using integer division, remainder, and string formatting.

## Limitations

- Calculates average split for one session at a time.
- Does not save results or compare sessions.
- Time input uses whole minutes and seconds.