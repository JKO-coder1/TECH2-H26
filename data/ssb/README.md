# Norwegian municipalities

Each municipality (*kommune* in Norwegian) belongs to a county (*fylke*).

| Column | Description and unit |
| --- | --- |
| `muni_id` | Official four-character municipality code; a string with leading zeros preserved. |
| `municipality` | Full official municipality name. |
| `county_id` | Official two-character county code (*fylkesnummer*); a string with leading zeros preserved. |
| `county` | Full official Norwegian county (*fylke*) name, including parallel names in other languages where present. |
| `population` | Number of residents on January 1. |
| `land_area` | Land area in km², excluding freshwater. |
| `mean_age` | Mean age of residents, in years, on January 1. |
| `median_age` | Median age of residents, in years, on January 1. |
| `college_share` | Percentage of residents aged 16+ with short or long higher education on October 1. The denominator excludes residents with unknown or no completed education; this is the sum of the two published percentages, on a 0–100 scale. |
| `median_income` | Median annual household income after tax, in NOK. Excludes student households and children under 18 living alone. This is household income, without adjustment for household size. |
| `cars` | Number of registered passenger cars on December 31, across all transport uses and fuels. |
| `electric_cars` | Number of those passenger cars powered by electricity, excluding hybrids. From 2025, vehicles with registered lessees are assigned to the lessee's municipality; earlier figures used the owner's municipality. This change applies to both vehicle counts. |

Empty fields indicate missing or unavailable observations. Source years can differ.
Rows are ordered by population from largest to smallest, then municipality code.
County membership uses the same classification date as the municipality roster.

Preserve both identifier columns as strings when reading the CSV:

```python
pd.read_csv('municipalities.csv', dtype={'muni_id': str, 'county_id': str})
```

Population density is not included. Calculate residents per km² of land as
`population / land_area` when needed. The land area figures are rounded to whole km².

Sources: Statistics Norway (SSB):

- [131: Municipality classification](https://www.ssb.no/en/klass/klassifikasjoner/131)
- [104: County classification](https://www.ssb.no/en/klass/klassifikasjoner/104)
- [11342: Population and area](https://www.ssb.no/en/statbank/table/11342)
- [13536: Mean and median age](https://www.ssb.no/en/statbank/table/13536)
- [09429: Educational attainment](https://www.ssb.no/en/statbank/table/09429)
- [06944: Household income](https://www.ssb.no/en/statbank/table/06944)
- [07849: Registered vehicles by fuel](https://www.ssb.no/en/statbank/table/07849)
