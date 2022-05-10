SELECT Combine."ExperimentalUnitID", Combine."ObservedValue"
FROM
    (
	SELECT "Endpoint"."ObservedValue", "GetObservedValue"."ExperimentalUnitID"
    FROM "Endpoint", "GetObservedValue"
    WHERE "Endpoint"."EndpointID" = "GetObservedValue"."EndpointID"
) Combine
WHERE Combine."ObservedValue" > 1.65 -- refractive index higher than 1.65
ORDER BY Combine."ObservedValue" DESC; -- ordered by Refractive index in descending order
