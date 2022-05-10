CREAT TABLE "FactEEGResult"(
    "ExperimentHashKey" VAECHAR(64) NOT NULL PRIMARY KEY,
    FOREIGN KEY("ExperimentHashKey") REFERENCES "DimExperiment"("ExperimentHashKey")
    "StimulusHashKey" VARCHAR(64) NOT NULL PRIMARY KEY,
    FOREIGN KEY ("StimulusHashKey") REFERENCES "DimStimulus"("StimulusHashKey"),
    "PatientHashKey" VARCHAR(64) NOT NULL PRIMARY KEY,
    FOREIGN KEY ("PatientHashKey") REFERENCES "DimPatient"("PatientHashKey"),
    Type VARCHAR(10) PRIMARY KEY,
    FOREIGN KEY ("Type") REFERENCES "DimEEGType"("Type"),
    "Fp1" FLOAT,
    "AF7" FLOAT,
    "AF3" FLOAT,
    "AF4" FLOAT,
    "AF8" FLOAT,
    "F7" FLOAT,
    "F5" FLOAT,
    "F3" FLOAT,
    "F4" FLOAT,
    "F6" FLOAT,
    "F8" FLOAT,
    "FC5" FLOAT,
    "FC3" FLOAT,
    "FC4" FLOAT,
    "FC6" FLOAT,
    "C5" FLOAT,
    "C6" FLOAT,
    "T7" FLOAT,
    "T8" FLOAT,
    "TP7" FLOAT,
    "CP5" FLOAT,
    "CP6" FLOAT,
    "TP8" FLOAT,
    "P7" FLOAT,
    "P5" FLOAT,
    "P6" FLOAT,
    "P8" FLOAT,
    "PO7" FLOAT,
    "PO8" FLOAT
);

CREATE TABLE "DimExperiment" (
    "ExperimentHashKey" VARCHAR(64) PRIMARY KEY,
    "ExperimentID" INT,
    "Title" VARCHAR(100),
	"Goal" VARCHAR(200),
	"TypeByNumberOfSessions" typeNumberOfSessions NOT NULL,
	"TypeByAllocation" typeAllocation NOT NULL,
);


INSERT INTO "DimExperiment"
SELECT
    hub."ExperimentHashKey",
    hub."ExperimentID",
    sat."Title",
    sat."Goal",
    sat."TypeByNumberOfSessions",
    sat."TypeByAllocation"
FROM "DataVault"."HubExperiment" hub
INNER JOIN "DataVault"."SatExperiment" sat ON (
    hub."ExperimentHashKey" = sat."ExperimentHashKey" and sat."LoadEndDate" is NULL
);


CREATE TABLE "DimStimulus" (
    "StimulusHashKey" VARCHAR(64) PRIMARY KEY,
    "StimulusID" VARCHAR(20) NOT NULL,
    "StimulusLevel" VARCHAR(100)
);

INSERT INTO "DimStimulus"
SELECT
    hub."StimulusHashKey",
    hub."StimulusID"
FROM "DataVault"."HubStimulus" hub
INNER JOIN "DataVault"."SatStimulus" sat ON (
    hub."StimulusHashKey" = sat."StimulusHashKey" and sat."LoadEndDate" is NOT NULL
);


CREATE TABLE "DimPatient" (
    "PatientHashKey" VARCHAR(64) PRIMARY KEY,
    "PatientID" VARCHAR(20),
    "Name" VARCHAR(100),
    "Age" INT,
    "Sex" VARCHAR(10)
);

INSERT INTO "DimPatient"
SELECT
    hub."PatientHashKey",
    hub."PatientID",
    sat."PatientName",
    sat."PatientAge",
    sat."PatientSex"
FROM "DataVault"."HubPatient" hub
INNER JOIN "DataVault"."SatPatient" sat ON (
    hub."PatientHashKey" = sat."PatientHashKey" and sat."LoadEndDate" is NULL
);


CREAT TABLE "DimEEGType"(
    "HBTypeKey" serial PRIMARY KEY
);

INSERT INTO "DimHBType" VALUES(1,EEGData);


INSERT INTO "FactEEGResult"
SELECT 
    "EEGDataHashKey", "Type", AVG("Fp1"), AVG("AF7"), AVG("AF3"), AVG("AF4"), AVG("AF8"), AVG("F7"), AVG("F5"), AVG("F3"), AVG("F4"), AVG("F6"), AVG("F8"), AVG("FC5"), AVG("FC3"), AVG("FC4"), AVG("FC6"), AVG("C5"), AVG("C6"), AVG("T7"), AVG("T8"), AVG("TP7"), AVG("CP5"), AVG("CP6"), AVG("TP8"), AVG("P7"),AVG("P5"), AVG("P6"), AVG("P8"), AVG("PO7"), AVG("PO8"),
FROM "DataVault"."SatEEGChannel" sat_channel
LEFT JOIN "DataVault"."HubEEGData" hub_eeg
    ON ("HubFNIRSData"."EEGDataHashKey" = "SatFNIRsHBChannel"."EEGDataHashKey")
LEFT JOIN "DataVault"."DimExperiment" dim_experiment -- using fk
    ON (hub_eeg."ExperimentID" = dim_experiment."ExperimentID")
LEFT JOIN "DataVault"."DimStimulus" dim_stimulus
    ON (hub_eeg."StimulusID" = dim_stimulus."StimulusID")
LEFT JOIN "DataVault"."DimPatient" dim_patient
    ON (hub_eeg."PatientID" = dim_experiment."PatientID")
LEFT JOIN "DataVault"."DimEEGType" dim_eegtype
    ON (sat_channel."Type" = dim_eegtype."EEGTypeKey")
GROUP BY "EEGDataHashKey", "Type"
