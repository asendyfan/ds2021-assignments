/*
Because this experiment using between subject method. means that each unit only have one observed value. 
So, we can know that the relationship between ExperimentalUnit and Endpoint is 1 to 1
And I use nested query method to get this question's result.
*/
SELECT Combine."ObservedValue"
FROM
    (
	SELECT "Endpoint"."ObservedValue" -- get observations
    FROM "Endpoint", "GetObservedValue" -- get from this two table
    WHERE "Endpoint"."EndpointID" = "GetObservedValue"."EndpointID" -- map in the same raw, use common key
    ORDER BY "GetObservedValue"."ExperimentalUnitID" -- order by unit id
) Combine; -- combine two tables into one, and name as "Combine"
