# Inflation expectations: 10% SCE sample

These files contain a prepared subset of the Federal Reserve Bank of New York's
[Survey of Consumer Expectations (SCE)](https://www.newyorkfed.org/microeconomics/sce).
We use respondents' expectations about inflation over the next 12 months.

There are 13 annual files named `SCE_YYYY.csv`, covering June 2013 through September
2025. Together, they contain 18,469 respondent-month observations across 148 survey
months. The first and last years are incomplete. Each row is one respondent's
response in one survey month; a respondent can appear in several months.

## Variables

| Variable | Description |
|----------|-------------|
| `userid` | Respondent identifier, unchanged across survey months. |
| `date` | First day of the survey month, in `YYYY-MM-DD` format. This is a monthly matching date, rather than the respondent's interview day. |
| `female` | Gender indicator: `0` = male, `1` = female. |
| `infl_1y` | Expected inflation over the next 12 months, in percent. Negative values indicate expected deflation. |

For example, `infl_1y = 3.5` means that the respondent expects prices to rise by
3.5% over the next 12 months; `infl_1y = -2` means an expected fall of 2%.

## Preparation and sampling

We start from the processed SCE extract produced by `sce-import`, with deflation
responses already assigned negative signs. We retain survey months through
September 2025 because October 2025 CPI is missing in the course's FRED data. We
then:

1. Keep the identifiers, gender indicator, and one-year inflation forecast, and
   remove rows with missing required fields (798 observations).
2. Compute the 0.1st and 99.9th percentiles of the remaining inflation forecasts,
   pooling all months and both genders. We remove forecasts below the lower
   cutoff or above the upper cutoff, retaining values equal to either cutoff
   (218 observations removed).
3. Draw a random 10% sample within each survey month and gender group, using seed
   `42`. Integer rounding within groups makes the overall fraction approximately
   10%. We sample observations, so the files do not preserve complete respondent
   histories.
4. Construct `date` from the survey-wave identifier and split the sample into
   annual, comma-separated files, omitting the redundant survey-wave identifier.
   Inflation forecasts are written to two decimal places.

The cleaned data contain 184,600 observations before sampling. No survey weights
are included; group averages calculated from these files are unweighted sample
averages.

## Matching with observed inflation

The course's `data/FRED/CPI.csv` contains monthly CPI levels. We can calculate
inflation over the preceding 12 months as

$$
100 \times \left(\frac{CPI_t}{CPI_{t-12}} - 1\right),
$$

where $t$ is the survey month and $CPI_{t-12}$ is the CPI 12 months earlier. We
calculate this change on the monthly CPI data before merging with the survey data.
The SCE `date` column matches the CPI file's `DATE` column.

This comparison relates expectations for the coming year to inflation experienced
over the preceding year. It does not measure forecast accuracy.
