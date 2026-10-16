# Kystverket data

Datasets from Kystverket (the Norwegian Coastal Administration). Each file is
documented separately below.

## `bergen_monthly_calls.csv`

Monthly reported arrivals at Bergen harbour, from January 2013 through September
2026, disaggregated by vessel type. The file contains 14,850 rows covering 165
months and 90 vessel type/category pairs. All field names and classification
labels are in English.

### Fields

| Field | Description |
| --- | --- |
| `month` | Arrival month in Bergen local time (`Europe/Oslo`), formatted as `YYYY-MM`. |
| `vessel_type` | Detailed vessel type, such as `Passenger/Cruise`, `General Cargo Ship`, or `LNG Tanker`. |
| `vessel_category` | Broader category: `Passenger ships`, `Cargo ships`, `Tankers`, `Fishing vessels`, `Offshore and special-purpose vessels`, `Recreational vessels`, or `Unknown`. |
| `calls` | Number of reported arrival records in that month for that vessel type/category pair. Repeat visits by the same ship count separately. |

Each row represents one month and vessel type/category pair. All 90 pairs appear
in every month; a zero means that no corresponding arrival records were returned.
Missing classifications are labeled `Unknown`. Rows are sorted by month, vessel
type, and category. The labels are written directly in the file, so no separate
lookup table is needed.

### Reading with pandas

From the repository root:

```python
import pandas as pd

df_calls = pd.read_csv(
    'data/kystverket/bergen_monthly_calls.csv',
    parse_dates=['month'],
    date_format='%Y-%m',
)
```

Pandas represents each month as its first day, such as `2013-01-01`. To use
monthly periods instead:

```python
df_calls['month'] = df_calls['month'].dt.to_period('M')
```

### Scope and interpretation

- The reporting location is Bergen harbour: Kystdatahuset location ID `2328078`,
  UN/LOCODE `NOBGO`. Nearby ports and separately identified terminals are not
  automatically included.
- The source consists of arrival reports submitted to SafeSeaNet. Small vessels
  and traffic exempt from reporting can be absent. These counts therefore do not
  represent every physical visit to Bergen.
- Months are assigned using the reported arrival timestamp (`eta`), converted
  to `Europe/Oslo`. Only completed months are included.
- From December 2023, reporting expanded to domestic passenger vessels and
  scheduled ferries, affecting comparisons of passenger traffic over time.
- `Passenger/Cruise` includes some coastal-service vessels and differs from the
  dedicated cruise-tourism classification used in Kystverket's cruise statistics.
- Counts retain exact duplicate source records: four duplicate copies in 2013
  and two in 2017. They count reported records rather than deduplicated visits.

### Source and license

Source: Kystverket's Kystdatahuset, SafeSeaNet arrival reports, retrieved on
October 15, 2026. Individual records were selected for Bergen harbour through
the `POST /ws/api/voyage/arrivals/for-locations` API endpoint, aggregated by Oslo
calendar month and vessel type/category, and classification labels were
translated to English. Zero counts were added for absent combinations.

- [Downloadable voyages dataset](https://kystdatahuset.kystverket.no/detail/dataset/8e16b69e-d466-47bd-91d2-179aebdf4f65)
- [Arrivals dashboard and reporting changes](https://kystdatahuset.kystverket.no/detail/dashboard/054018f2-ebb3-489b-aa25-0240dffb1c14)
- [API documentation](https://kystdatahuset.kystverket.no/ws/swagger/index.html)

Contains data under the Norwegian licence for Open Government data (NLOD)
distributed by Kystverket (Norwegian Coastal Administration). The API declares
[NLOD 1.0](https://data.norge.no/nlod/en/1.0). The processing changes are described
above; this is a derived teaching dataset, not an official Kystverket statistical
publication.

The NLOD terms permit reuse, modification, and redistribution with attribution,
a reference to the license, and a description of changes. Retain this source and
license information when sharing the data. The data's NLOD terms apply separately
from any software license used elsewhere in this repository.
