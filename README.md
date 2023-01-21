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

Open file `root/src/run.py` and add these codes at line 37:

```python
        # line above
        # elif argv[1] == 'ParserSuite':
        #     from ParserSuite import ParserSuite
        #     getAndTest(ParserSuite)
        elif argv[1] == 'CustomLexer':
            sys.path.append('../CO3005-assigment1-testcase/')
            from CustomTestUtils import DETAIL_DIR, SOL_DIR, TEST_DIR
            LexerSuite = getattr(__import__('CustomLexerSuite_'+argv[2],fromlist=['LexerSuite']),'LexerSuite')

            subprocess.run(["rm", "-rf", DETAIL_DIR + "/*.txt"])
            subprocess.run(["rm", "-rf", TEST_DIR + "/*.txt"])
            subprocess.run(["rm", "-rf", SOL_DIR + "/*.txt"])
            
            # getAndTest(LexerSuite)
        elif argv[1] == 'CustomParser':     
            sys.path.append('../CO3005-assigment1-testcase/')
            from CustomTestUtils import DETAIL_DIR, SOL_DIR, TEST_DIR
            ParserSuite = getattr(__import__('CustomParserSuite_'+argv[2],fromlist=['ParserSuite']),'ParserSuite')

            subprocess.run(["rm", "-rf", DETAIL_DIR + "/*.txt"])
            subprocess.run(["rm", "-rf", TEST_DIR + "/*.txt"])
            subprocess.run(["rm", "-rf", SOL_DIR + "/*.txt"])
            
            getAndTest(ParserSuite)
        # line below
        # else:
        #     printUsage()
```

## Run

Change current directory to `root/src` where there is file run.py

Then type to test Lexer

    python run.py test CustomLexer {AuthorName}

ex: `python run.py test CustomLexer HTK`

Then type to test Parser

    python run.py test CustomParser {AuthorName}



## Contribute

Testcases are stored in file `CustomLexerSuite_{AuthorName}.py` and `CustomParserSuite_{AuthorName}.py`

Testcase name convention: `{AuthorName}_{ID}.txt`
