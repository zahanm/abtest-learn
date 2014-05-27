<!-- background: #f39b12 -->
<!-- color: #fff -->
<!-- font: frutiger -->

<!-- Available online at: https://swipe.to/8881s -->

# Hello World!

* * *

# Zahan Malkani

Growth Hacker @ Facebook

Stanford: BS Physics 2012, MS Computer Science 2013

* * *

<!-- font: monaco -->

    hello.world()

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

Don't forget to see how how your population divides among __active__ users. Obviously, you need to define what __active__ means in your context.

- mean # of actions per person
- Weekly active, monthly active

## Simplification

Made a big simplification assumption here. People are equally likely to return. In reality having cohorts who are more likely to return completely changes your test analysis.

* * *

# Metrics

We have three different metrics in this dataset. Let's examine what they are, and their properties.

We will look at the following for people not currently in tests

- how likely they are to happen, i.e. proportion of all conversion events
- what the age distribution of people taking this action is
- what the gender distribution of people taking this action is

* * *

## Metric A

Think of this as a 'status update' event. We care about it a bit.

## Metric B

Think of this as a 'athletic activity' event. About as important to us as A.

## Metric C

Think of this as a 'uploaded a photo' event. We care about it *a lot*.

* * *

# SQL

This is important. You should understand the next few lines.

    select c.metric
    from conversions as c
    join exposures as e
    on c.uid = e.uid
    where e.test1 = 0 and e.test2 = 0

* * *
