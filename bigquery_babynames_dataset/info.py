ID = 803905626348-1vt89uu0s961d16sogh52utve3jta5r3.apps.googleusercontent.com
key = 4lN0o6t-2hysm-ocxYD97Mza

# Using BigQuery on US babynames in 1994,
# regex to return any names similar to jacob
SELECT
  name,
  count, 
  gender,
  REGEXP_CONTAINS(name, "Ja..b") AS is_valid
FROM
  `babynames.names_1994`
WHERE REGEXP_CONTAINS(name, "Ja..b")
ORDER BY
  count DESC

# London crime stats by year and borough
SELECT
  borough,
  
  year,
  SUM(value) as total
FROM `bigquery-public-data.london_crime.crime_by_lsoa` 
GROUP BY borough, year
ORDER BY borough, year DESC
;