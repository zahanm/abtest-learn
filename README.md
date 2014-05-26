# How to Analyse an A/B Test

## Generating the data

We simulate server hits, and use the random module to pick which exposure and conversion events to log.

### Each Hit

- Increment (optionally) the time
- Choose a user
- Choose which test groups (s)he will land in
- Choose some conversion events to occur just then - with probabilities

## Metrics Spec

The various conversion events we care about.

### Metric A

Think of this as a 'status update' event. We care about it a little bit. Pretty likely to happen on each hit. Let's say 30% chance.

### Metric B

Think of this as a 'athletic activity' event. Younger males are most likely to do this, 20% likely. Younger females - 15%. Older males - 10%. Older females - 5%.

### Metric C

Think of this as a 'uploaded a photo' event. Doesn't happen very often, but we care about it *a lot*. Let's say baseline is 5% likely in the whole population.

## Test Spec

Each test has a specific effect on metrics, and we need to tease those effects apart.

### Test 1

Let's say this is a big promotion for the Amgen Tour of California on the homepage. B is affected in a big way, since people are associating Facebook with sports.

Let's say it increases metric B by 10% across the board. C gets a bump too, people uploading photos of themselves doing cool stuff, 1% for men. Unfortunately because all the featured pictures are of men, metric C takes a dip for women to the tune of 0.5%. Metric A is unaffected.

This test will be on for the first 20% of the UID space.

### Test 2

This is a pretty simple test, let's make the status update button bigger. We want more people to be sharing their thoughts.

This gets a 2% bump overall in people sharing updates, metric A. Metric C, on the other hand, goes down by 2% because we had to make the photo upload button smaller. Metric B is unaffected.

## Analysis

Number of conversion events per person, per exposure

Tests can have a different effect on different set of people. ie, age, gender.

Tests can have different effects on the different metrics that we care about, and we should be diligent enough to check all of them.

Error bars, super crucial. How confident are we of the test results? Compare to the control conversion level.

Ultimately, we want to make the decision, which tests should launch, and which should not.
