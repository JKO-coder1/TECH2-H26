# Data

This folder and its sub-folders contain various datasets used during the lectures and workshops.
See README files in sub-folders for documentation and sources.

## Files

- `ames_houses.csv`: Simplified version of the Ames housing dataset which 
    contains 2,930 observations on about 80 features of houses sold in Ames, Iowa, between 2006 and 2010.

    See [https://jse.amstat.org/v19n3/decock/DataDocumentation.txt](https://jse.amstat.org/v19n3/decock/DataDocumentation.txt)
    for detailed documentation of the original dataset.

    *Variables:*

    1. `LotArea`: Lot size in square meters
    2. `Neighborhood`: Physical locations within Ames city limits
    3. `OverallQuality`: Rates the overall material and finish of the house
        (1 = very poor, 10 = excellent)
    4. `OverallCondition`: Rates the overall condition of the house
        (1 = very poor, 10 = excellent)
    5. `YearBuilt`: Original construction date
    6. `YearRemodeled`: Remodel date (same as construction date if no remodeling or additions)
    7. `BuildingType`: Type of dwelling
    8. `CentralAir`: Central air conditioning (string, Y/N)
    9. `LivingArea`: Above grade (ground) living area in square meters
    10. `Bathrooms`: Full bathrooms above grade
    11. `Bedrooms`: Bedrooms above grade (does not include basement bedrooms)
    12. `Fireplaces`: Number of fireplaces
    13. `SalePrice`: Sale price in thousands of USD
    14. `YearSold`: Year sold
    15. `MonthSold`: Month sold
    16. `HasGarage`: Flag indicating whether the property has a garage

- `titanic.csv`: Passenger list of the Titanic's maiden voyage, taken
    from [pandas's data collection](https://github.com/pandas-dev/pandas/blob/main/doc/data/titanic.csv).

    *Variables:*

    1.  `PassengerId`: Passenger ID
    2.  `Survived`: Indicator whether the person survived
    3.  `Pclass`: Accommodation class (first, second, third)
    4.  `Name`: Name of passenger (last name, first name)
    5.  `Sex`: `male` or `female`
    6.  `Age`
    7.  `Ticket`: Ticket number
    8.  `Fare`: Fare in pounds
    9.  `Cabin`: Deck + cabin number
    10. `Embarked`: Port at which passenger embarked:
        `C` - Cherbourg, `Q` - Queenstown, `S` - Southampton


- `NBER_cycle_dates.csv`: US business cycle peaks and troughs as dated by the 
    National Bureau of Economic Research (NBER).

    Source: [https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions](https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions)

    1. `peak`: Peak quarter (last quarter in which GDP was growing)
    2. `trough`: Trough quarter (last quarter in which GDP was declining)
