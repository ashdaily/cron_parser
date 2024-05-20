## Project Cron Parser

The solution is written in python3 utilises docker & docker-compose. 


### Build the solution with docker
Requirement : Docker required system-wide.

```bash
docker-compose build
```

---

### Try the Cron Parser

Example command:

```bash
docker-compose run cron-parser "*/7 0 1,15 * 1-5 /usr/bin/find"
``` 

Example Result:
```fish

Creating deliveroo_cron-parser_run ... done
[03:36:11] INFO     Cron parser started...                                                                   main.py:28
╭─ Parsed Cron Fields ──────────────────────────────────╮
│                 Cron Parsing Results:                 │
│ ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ │
│ ┃ Cron Fields          ┃ Expanded Values            ┃ │
│ ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩ │
│ │ minute               │ 0 7 14 21 28 35 42 49 56   │ │
│ │ hour                 │ 0                          │ │
│ │ day of month         │ 1 15                       │ │
│ │ month                │ 1 2 3 4 5 6 7 8 9 10 11 12 │ │
│ │ day of week          │ 1 2 3 4 5                  │ │
│ │ command              │ /usr/bin/find              │ │
│ └──────────────────────┴────────────────────────────┘ │
╰───────────────────────────────────────────────────────╯
           INFO     Cron parser executed !   

```
---

### Turn on debug logs from docker-compose.yaml file

```bash
# change LOG_LEVEL for cron-parser service in docker-compose.yaml

LOG_LEVEL=INFO # change this to DEBUG to see debug logs

# LOG_LEVEL=INFO will mute most of the logs
```

Try the parser again & you should see something like this:
```fish
Creating deliveroo_cron-parser_run ... done
[03:42:19] INFO     Cron parser started...                                                                   main.py:28
           DEBUG    Initializing CronParser, received cron_str: "*/7 0 1,15 * 1-5 /usr/bin/find"       cron_parser.py:7
           DEBUG    Initializing minute field with string: */7                                        cron_fields.py:12
           DEBUG    Initializing hour field with string: 0                                            cron_fields.py:12
           DEBUG    Initializing day of month field with string: 1,15                                 cron_fields.py:12
           DEBUG    Initializing month field with string: *                                           cron_fields.py:12
           DEBUG    Initializing day of week field with string: 1-5                                   cron_fields.py:12
           DEBUG    Parsing cron_field of type minute with value: */7                                 cron_fields.py:15
           DEBUG    Parsed cron_field of type minute */7 to [0, 7, 14, 21, 28, 35, 42, 49, 56]        cron_fields.py:17
           DEBUG    Parsing cron_field of type hour with value: 0                                     cron_fields.py:15
           DEBUG    Parsed cron_field of type hour 0 to [0]                                           cron_fields.py:17
           DEBUG    Parsing cron_field of type day of month with value: 1,15                          cron_fields.py:15
           DEBUG    Parsed cron_field of type day of month 1,15 to [1, 15]                            cron_fields.py:17
           DEBUG    Parsing cron_field of type month with value: *                                    cron_fields.py:15
           DEBUG    Parsed cron_field of type month * to [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]      cron_fields.py:17
           DEBUG    Parsing cron_field of type day of week with value: 1-5                            cron_fields.py:15
           DEBUG    Parsed cron_field of type day of week 1-5 to [1, 2, 3, 4, 5]                      cron_fields.py:17
           DEBUG    Parsing command field: /usr/bin/find                                              cron_fields.py:75
╭─ Parsed Cron Fields ──────────────────────────────────╮
│                 Cron Parsing Results:                 │
│ ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ │
│ ┃ Cron Fields          ┃ Expanded Values            ┃ │
│ ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩ │
│ │ minute               │ 0 7 14 21 28 35 42 49 56   │ │
│ │ hour                 │ 0                          │ │
│ │ day of month         │ 1 15                       │ │
│ │ month                │ 1 2 3 4 5 6 7 8 9 10 11 12 │ │
│ │ day of week          │ 1 2 3 4 5                  │ │
│ │ command              │ /usr/bin/find              │ │
│ └──────────────────────┴────────────────────────────┘ │
╰───────────────────────────────────────────────────────╯
           INFO     Cron parser executed !                                                                   main.py:53

```

---

### Run the tests

```bash
 docker-compose run cron-parser-test
```

---

### Build and run the solution without docker
Requirement : python3.7 or above and pip3

- `pip3 install -r requirement.txt`
- `python3 src/main.py "*/15 0 1,15 * 1-5 /usr/bin/find"`

---


### Solution Intro
```md
deliveroo/
│
├── Dockerfile
├── docker-compose.yml # composes cli app (cron-parser) & the unit tests (cron-parser)
├── requirements.txt    # Only using two dependencies
                        # Rich pip package (to beautify logs and parsed output in table)
                        # Parameterized pip package (For a theory style tests, to test against many
                        # different inputs for same unit tests and avoid using for loops in unit tests body)
├── src/
│   ├── main.py # will parse the cron job do very little validation and print result from cron_parser.py
│   ├── cron_fields.py # all possible cron fields like minute, day of week, day of month etc
│   ├── cron_factory.py # provides cron_field objects for minute, hour, day of week, day of month, month, cmd.
│   ├── cron_parser.py # does the parsing for all cron_fields present in cron_str by using the cron_factory to get cron_field objects and calling .parse() on them iteratively for all cron_fields present in cron_string
│   ├── logging_config.py # set logging to default INFO if not provided by ENV vars
│   └── strategies.py # bunch of different strategies to deal with cron_field syntax, support *, single integer (for eg: 1), multiple integers eg (1,10) or range (1-10), supports most cases for asterisk, comma, dash, / with one cron_field having multiple symbols (see tests)
├── tests/
│   ├── __init__.py
│   ├── test_cron_parser.py # tests variety of full command cron_string
│   └── tests_cron_fields/ # tests individual fields extensively
└── venv/
```

---


### The good:
- Dash, Slash, Asterisk, Comma in individual cron_field for any date time entity should work.
- Each cron_field is tested properly for happy cases with many random inputs.
- Cron Parser with full cron_string is also tested with many random cron strings.
- Logging gives a useful insight on what happened to each cron_field
- Logging level passed from OS Env so the LOG_LEVEL can be changed easily inside docker-compose.yaml.


Some Examples which are handled gracefully: 
Every 15 minutes:
```bash
*/15 * * * * /path/to/command
```

Every weekday at 8:00 AM:
```bash
0 8 * * 1-5 /path/to/command

```

At 12:00 AM on the first day of every month:
```bash
0 0 1 * * /path/to/command
```

At 5:30 PM on every Friday:
```bash
30 17 * * 5 /path/to/command
```

On the last day of every month at 11:59 PM:
```bash
59 23 L * * /path/to/command
```

On January 1st at midnight:
```bash
0 0 1 1 * /path/to/command
```

Some more complicated once like, every day, once in every two hours until 12pm, after that every 4 hours:
```bash
0 0-12/2,13-23/4 * * *
```

---

### The improvements 
Due to limited time I couldn't work on the following:
- Invalid syntax for cron_string input, in general, is not handled well.
- Symbols that are invalid are not handled gracefully.
- Not very focused on handling errors and validations, does very basic validation around max and min value
- Could better support special symbols like hash, L, W.
- Could introduce test for CLI output part as well.
- Month upper limit 31 is static, while 31 might not be present in a month.
- More edge cases could be handled.