<!-- background: #fff4e3-->
<!-- color: #2d2422 -->
<!-- font: univers -->

<!-- Available online at: https://swipe.to/8881s -->

# Quantitative Design

* * *

### Zahan Malkani

Growth @ Facebook

* * *

# Demographics

Let's start with a look at the demographics of this set of people.

    # if only this would work
    select * from people;

The dimensions to look at distributions include

- age
- gender

* * *

# Active Users

Don't forget to see how how your population divides among _active_ users. Obviously, you need to define what _active_ means in your context.

- mean # of actions per person
- Weekly active, monthly active

We made a big assumption here to simplify matters, that people are equally likely to return. In reality having cohorts who differ in their likelihood of returning complicates your test analysis.

* * *

# Metrics

We have three different metrics in this dataset. Let's examine what they are, and their properties.

We will look at the following for people not currently in tests

- how likely they are to happen, i.e. proportion of all conversion events
- what the age distribution of people taking this action is
- what the gender distribution of people taking this action is

* * *

### Metric A

Think of this as a 'status update' event. We care about it a bit.

### Metric B

Think of this as a 'athletic activity' event. About as important to us as A.

### Metric C

Think of this as a 'uploaded a photo' event. We care about it *a lot*.

* * *

# SQL

You really should understand these next few lines. `SQL` is an indispensable tool in industry.

    select c.metric
    from conversions as c
    join exposures as e
    on c.uid = e.uid
    where e.test1 = 0 and e.test2 = 0

* * *

# Finally, the Tests

We are running two tests on this unfortunate group of guinea pigs. We are going to examine the results for each, and their impact on the metrics that we care about.

* * *

### Test 1

Let's say this is a big promotion for the Amgen Tour of California on the homepage.

### Test 2

Let's make the status update button bigger. We want more people to be sharing their thoughts.

* * *

< Stacked bar charts for each metric > test1, test2

< Stacked bar charts for gender > test1, test2
we don't expect the tests to affect age groups differently

* * *

# But wait, aren't we forgetting something?

* * *

# Confidence Intervals

We need to know how confident we should be of these results.

* * *

# Overlap effects

What happens when you look at people in both tests? It all goes to pieces.

* * *

# [github.com/zahanm/abtest-learn](https://github.com/zahanm/abtest-learn)

* * *
