# CO3005-assigment1-testcase

## Setup

Assumed that the initial code give by teachers is in `root` folder (include `src` and `target` folder)

Download and move this repo (CO3005-assigment1-testcase) to `root/` like the file structure below:

    root
    ├── CO3005-assigment1-testcase
    │   ├── lexer
    │   ├── parser
    │   └── ...
    ├── src
    └── target

Open file `root/src/run.py` and add these codes add line 37:

```python
        # line above
        # elif argv[1] == 'ParserSuite':
        #     from ParserSuite import ParserSuite
        #     getAndTest(ParserSuite)
        elif argv[1] == 'CustomLexer':
            sys.path.append('../CO3005-assigment1-testcase/')
            from CustomLexerSuite import LexerSuite
            getAndTest(LexerSuite)
        elif argv[1] == 'CustomParser':     
            sys.path.append('../CO3005-assigment1-testcase/')
            from CustomParserSuite import ParserSuite  
            getAndTest(ParserSuite)
        # line below
        # else:
        #     printUsage()
```

## Run

Change current directory to `root/src` where there is file run.py

Then type to test Lexer

    python run.py test CustomLexer

Then type to test Parser

    python run.py test CustomParser



## Contribute

Testcases are stored as `.txt` file under `root/CO3005-assigment1-testcase/(lexer|parser)/testcases/`.

Filename convention: `{yourname}_{id}.txt`