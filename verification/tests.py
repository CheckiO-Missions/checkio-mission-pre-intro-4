"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [3],
            "answer": 3,
        },
        {
            "input": ["string"],
            "answer": "string",
        },
        {
            "input": [True],
            "answer": True,
        },
    ],
    "Extra": [
        {
            "input": [-15],
            "answer": -15,
        },
        {
            "input": ["another string"],
            "answer": "another string",
        },
        {
            "input": [False],
            "answer": False,
        },
    ]
}
