[![Build Status](https://app.travis-ci.com/palec87/towards_computer_vision.svg?branch=main)](https://app.travis-ci.com/palec87/towards_computer_vision)

# My first Kaggle comp learning path
* Beginner transmits to beginners.
* collection of commented scripts showing what I have actually learned.
* To make it into a documentary, I might comment back on previously written stuff, but I will NEVER delete any piece of errors which are gonna appear here.

## My initial plan
1. Before even trying any deep learning games I will write my own rudimentary model including the underlying algos
2. One day I might submit it against the comp data. That is going to be my benchmark
3. Only then I start to deploy tens of crazy AI models running all night on my laptop.
  * If get that far, I might be technically breaking the comp rules of public sharing of code outside of Kaggle, but at this point I consider it very improbable:)

## List of scripts so far
## Day 1
1. 01_label_img_dfs_recursion.py
    * surprise that beautiful recursion DFS will not work for 4k x 4k images
2. 02_label_img_dfs_iterative.py
    * Changing the algo to iterative version.
    * TODO: I should time things, but pressure of too far-away goal says f... it.

## Day 3
I got scared that I have a bug in the DFS from day 1. Therefore, the lesson is to write bloody tests.
* Simple and cool pytest module allows to parametrize test inputs and asserts.
* You can check tests/test_s01.py and tests/test_s02.py.

The feared bug was in the end a featere. Imagine labelled 2D array of uniformly distributed integers by a threshold value.

3. 03-stats.py
  * What is the distribution of sizes of these areas? You can see it as a cool way to create interesting distributions with outliers.



