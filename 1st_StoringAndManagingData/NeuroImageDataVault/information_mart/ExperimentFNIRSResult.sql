-- Grain: fnir result per experiment per treatment per HB type and per patient, aggregrated by time

CREATE TABLE "FactFNIRSHBResult" ( 
    "ExperimentHashKey" VARCHAR(64) NOT NULL PRIMARY KEY,
    "StimulusHashKey" VARCHAR(64) NOT NULL PRIMARY KEY,
    "PatientHashKey" VARCHAR(64) NOT NULL PRIMARY KEY,
    "Type" VARCHAR(10) PRIMARY KEY,
    "CH1" DECIMAL,
    "CH2" DECIMAL,
    "CH3" DECIMAL,
    "CH4" DECIMAL,
    "CH5" DECIMAL,
    "CH6" DECIMAL,
    "CH7" DECIMAL,
    "CH8" DECIMAL,
    "CH9" DECIMAL,
    "CH10" DECIMAL,
    "CH11" DECIMAL,
    "CH12" DECIMAL,
    "CH13" DECIMAL,
    "CH14" DECIMAL,
    "CH15" DECIMAL,
    "CH16" DECIMAL,
    "CH17" DECIMAL,
    "CH18" DECIMAL,
    "CH19" DECIMAL,
    "CH20" DECIMAL,
    "CH21" DECIMAL,
    "CH22" DECIMAL,
    "CH23" DECIMAL,
    "CH24" DECIMAL
    FOREIGN KEY ("ExperimentHashKey") REFERENCES "DimExperiment"("ExperimentHashKey"),
    FOREIGN KEY ("StimulusHashKey") REFERENCES "DimStimulus"("StimulusHashKey"),
    FOREIGN KEY ("PatientHashKey") REFERENCES "DimPatient"("PatientHashKey"),
    FOREIGN KEY ("Type") REFERENCES "DimHBType"("Type"),
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
)

CREATE TABLE "DimHBType" (
    "HBTypeKey" serial PRIMARY KEY,
    "Description" VARCHAR(20)
);

INSERT INTO "DimHBType" VALUES
(1, "Oxy"),
(2, "Deoxy");


INSERT INTO "FactFNIRSHBResult"
SELECT 
    "FNIRSDataHashKey", "Type", AVG("CH1"), AVG("CH2"), AVG("CH3"), AVG("CH4"), AVG("CH5"), AVG("CH6"), AVG("CH7"), AVG("CH8"), AVG("CH9"), AVG("CH10"), AVG("CH11"), AVG("CH12"), AVG("CH13"), AVG("CH14"), AVG("CH15"), AVG("CH16"), AVG("CH17"), AVG("CH18"), AVG("CH19"), AVG("CH20"), AVG("CH21"), AVG("CH22"), AVG("CH23"), AVG("CH24")
FROM "DataVault"."SatFNIRsHBChannel" sat_channel
LEFT JOIN "DataVault"."HubFNIRSData" hub_fnirs
    ON ("HubFNIRSData"."FNIRSDataHashKey" = "SatFNIRsHBChannel"."FNIRSDataHashKey")
LEFT JOIN "DataVault"."DimExperiment" dim_experiment -- using fk
    ON (hub_fnirs."ExperimentID" = dim_experiment."ExperimentID")
LEFT JOIN "DataVault"."DimStimulus" dim_stimulus
    ON (hub_fnirs."StimulusID" = dim_stimulus."StimulusID")
LEFT JOIN "DataVault"."DimPatient" dim_patient
    ON (hub_fnirs."PatientID" = dim_experiment."PatientID")
LEFT JOIN "DataVault"."DimHBType" dim_hbtype
    ON (sat_channel."Type" = dim_hbtype."HBTypeKey")
GROUP BY "FNIRSDataHashKey", "Type"
