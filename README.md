# rangesum

This is a service that calculates the sum of all the numbers in the range 
0 to 10^7 inclusive.

## To build and run (Linux)

    mkdir venv
    python3 -m venv venv
    . venv/bin/activate
    pip3 install Flask
    export FLASK_APP=rangesum.py
    flask run
    
## To build and run (Windows)
    mkdir venv
    py -3 -m venv venv
    venv\Scripts\activate
    pip install Flask
    set FLASK_APP=rangesum.py
    python -m flask:

## To query
     curl http://localhost:5000/total
Gives the response of:

    {"total":50000005000000}

## To stop
Type control C in the console.

## To Test
    python3 -m unittest sum_of_range_test.py

This tests that the function (using Gauss's formula) used to calculate the result really does return the same result as labouriously adding all the values together.

## Efficiency

The calculation of the sum has an Efficiency of Big O 1. However big the range is (within the bounds of Python Integers) it should take about the same time.

## Assumptions

I have assumed that all the ranges start at 0 that this function will sum. This is what the output of range(number) outputs.
