SELECT Combine."TreatmentName", Combine."PairFactorLevelID" FROM ( -- Retrieve the treatment name together and associated pairFactorlevelID
	SELECT "Treatment".*, "TreatmentLevels"."PairFactorLevelID" FROM "Treatment", "TreatmentLevels" -- get all data from Treatment, and get pair id from treatmentlevels
	WHERE "Treatment"."TreatmentID" = "TreatmentLevels"."TreatmentID" -- map the row
)Combine
WHERE Combine."TreatmentID" = 2; -- give the condition, concentration 10, which its treatment id is 2
