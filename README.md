# How to Analyse an A/B Test

## Generating the data

We simulate server hits, and use the random module to pick which exposure and
conversion events to log.

### Each hit

- Increment (optionally) the time
- Choose a user
- Choose which test groups (s)he will land in
- Choose some conversion events to occur just then - with probabilities
## Analysis

### Metrics

Number of conversion events per person, per exposure
