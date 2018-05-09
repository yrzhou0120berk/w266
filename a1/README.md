# Assignment 1: Information Theory, TF Introduction and Dynamic Programming, oh my!

This assignment consists of three unrelated parts:

* [Infomation Theory Review](information_theory.ipynb)
* [Dynamic Programming](dp/dynamic_programming.ipynb)
* [TensorFlow Introduction](tensorflow/tensorflow.ipynb)

We strongly recommend that you do that [Assignment 0](../a0/) first to verify that you're all set up with Python and TensorFlow.

**Hint:** James will be going through Assignment 1 in the extra office hour in Week 1 (May 8 2018 at 8pm Pacific). Please come with your questions!

These notebook is designed to be self-contained and not depend on the async or readings. The async, however, will reference a number of concepts from them - so we hope that it serves as useful background!

We anticipate you will spend most of your time on the TensorFlow introduction.
TensorFlow is a somewhat different programming model than you may be used to. 
Similar to MapReduce, it breaks constructing the computational graph and executing it into two separate steps. 
Some students describe this introduction as the hardest 10 lines of code they've had to write - but we promise that it gets a *lot* easier from there!

## Submission instructions 

As with Assignment 0, please submit by running the submit script, only with -a 1 (since this is assignment 1).
```
./assignment/submit.sh -u your-github-username -a 1
```

It is your responsibility to check that your work has made it to your GitHub repository in the a1-submit branch.  As always, a small number of points will be given in each assignment for submitting in the right place.

It will be tempting, if you are familiar with Git, to do something more complicated.  Try to resist.  The only step in the submission process is to run that command.  Don't send pull requests, don't merge to master, don't git merge.  Just commit to your local repo and run the submit command.  If you want to get yourself into a weird state despite this warning, please at least take the time to read and understand the submit.sh script above!
