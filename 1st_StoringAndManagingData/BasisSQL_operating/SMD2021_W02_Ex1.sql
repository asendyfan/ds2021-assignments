/*
From the material, create 13 entity tables and 10 relationship tables, the table name and descriptions and listed below.
Entity
1. Experiment: Store each experiment, it describe the experimental context, like question, hypothesis and aim.
2. Researcher: The people who conduct the experiment.
3. Factor: The factor that influence the experiment result.
4. SimpleFactor: Inherited from Factor, directly manipulated by the researcher, during the experiment.
5. CoFactor: Inherited from Factor, fixed to ensure that they do change during the experiment.
6. ConfoundingFactor: Inherited from Factor, those neither manipulated nor controlled but which may have an effect on the outcomes of the experiment.
7. Level: The number value for simple factor.
8. PairSimpleFactorLevel: Store pairs of each Simple Factor and Level.
9. Treatment: It is several pairs of SimpleFactor and Level.
10. ExperimentalUnit: Store the subjects.
11. Session: Data acquisitions processes by sampling from the experimental unit.
12. Endpoint: Store the scalar observations of sessions.
13. Group: according allocation methods, to have different groups.

Relationship
14. ObservesEndpoint: Experiment(1) observes (N)Endpoint
15. Conducts: Researcher(s)(M) conduct(s) (N)Experiment
16. HasFactors: Experiment(1) observes (N)Factors
17. HasTreatment: Experiment(1) has (N)Treatments
18. TreatmentLevels: treatment(1) R (N)PairSimpleFactorLevel
19. OrganisesIntoSession: Experiment(1) organises into (N)Session
20. MeasuresUnit: Session(M) measure(s) (N)ExperimentalUnit
21. AdminstersTreatment: Session(M) adminster(s) (N)Treatment
22. GroupsUnit: Group(1) groups (N)ExperimentalUnit
23. GetObservedValue: ExperimentalUnit(M) get (N)Endpoint
*/

-- create database
CREATE DATABASE "smdYXP027ScientificExperimentsManagement"; 
-- connect it
\c "smdYXP027ScientificExperimentsManagement"

/*
type: entity
*/
CREATE TABLE "Experiment" (
    "Title" VARCHAR(100) NOT NULL,
    "ResearchQuestion" VARCHAR(100) NOT NULL,
    "Hypothesis" VARCHAR(100) NOT NULL,
    "Goal" VARCHAR(100) NOT NULL,
    "TypeByNumberOfSessions" VARCHAR(30) NOT NULL,
    "TypeByAllocation" VARCHAR(30) NOT NULL,
    "ExperimentID" serial NOT NULL,
    PRIMARY KEY ("ExperimentID")
);

/*
type: entity
*/
CREATE TABLE "Researcher"
(
    "Name" VARCHAR(30) NOT NULL,
    "Surname" VARCHAR(30) NOT NULL,
    "ResearcherID" serial NOT NULL,
    PRIMARY KEY ("ResearcherID")
);

/*
type: entity
explain: subentity of Factor
*/
CREATE TABLE "SimpleFactor"
(
    "SimpleFactorID" serial NOT NULL,
    PRIMARY KEY ("SimpleFactorID")
);

/*
type: entity
explain: subentity of Factor
*/
CREATE TABLE "CoFactor"
(
    "CoFactorID" serial NOT NULL,
    "Level" INT NOT NULL,
    PRIMARY KEY ("CoFactorID")
);

/*
type: entity
explain: subentity of Factor
*/
CREATE TABLE "ConfoundingFactor"
(
    "ConfoundingFactorID" serial NOT NULL,
    PRIMARY KEY ("ConfoundingFactorID")
);

/*
type: entity
explain: superfactor, store common attributes and subentities' primary keys as foreign keys
*/ 
CREATE TABLE "Factor"
(
    "FactorID" serial NOT NULL,
    "Name" VARCHAR(30) NOT NULL,
    "SimpleFactorID" INT,
    "CoFactorID" INT,
    "ConfoundingFactorID" INT,
    PRIMARY KEY ("FactorID"),
    FOREIGN KEY ("SimpleFactorID") REFERENCES "SimpleFactor" ("SimpleFactorID"),
    FOREIGN KEY ("CoFactorID") REFERENCES "CoFactor" ("CoFactorID"),
    FOREIGN KEY ("ConfoundingFactorID") REFERENCES "ConfoundingFactor" ("ConfoundingFactorID")
);

/*
type: entity
explain: store simple factors' levels
*/
CREATE TABLE "Level"
(
    "LevelID" serial NOT NULL,
    "Value" INT NOT NULL,
    PRIMARY KEY ("LevelID")
);

/*
type: entity
explain: store pairs of each Simple Factor and Level
*/
CREATE TABLE "PairSimpleFactorLevel"
(
    "PairFactorLevelID" serial NOT NULL,
    "SimpleFactorID" INT NOT NULL,
    "LevelID" INT NOT NULL,
    FOREIGN KEY ("SimpleFactorID") REFERENCES "SimpleFactor" ("SimpleFactorID"),
    FOREIGN KEY ("LevelID") REFERENCES "Level" ("LevelID"),
    PRIMARY KEY ("PairFactorLevelID")
);

/*
type: entity
explain: treatment is several pairs of SimpleFactor and Level
*/
CREATE TABLE "Treatment"
(
    "TreatmentID" serial NOT NULL,
    "TreatmentName" VARCHAR(100) NOT NULL,
    PRIMARY KEY ("TreatmentID")
);

/*
type: entity
*/
CREATE TABLE "ExperimentalUnit"
(
    "ExperimentalUnitID" serial NOT NULL,
    "Description" VARCHAR(100) NOT NULL,
    PRIMARY KEY ("ExperimentalUnitID")
);

/*
type: entity
explain: data acquisitions processes by sampling from the experimental unit
*/
CREATE TABLE "Session"
(
    "SessionID" serial NOT NULL,
    "AcquisitionDate" DATE NOT NULL, -- format (yyyy-mm-dd) 
    "AcquisitionTime" TIME NOT NULL, -- format (HH:MM:SS)
    PRIMARY KEY ("SessionID")
);

/*
type: entity
explain: the result of each session
*/
CREATE TABLE "Endpoint"
(
    "EndpointID" serial NOT NULL,
    "Name" VARCHAR(30) NOT NULL,
    "ObservedValue" FLOAT NOT NULL, -- observed measured variables, and only consider scalar observations
    PRIMARY KEY ("EndpointID")
);

/*
type: entity
*/
CREATE TABLE "Group"
(
    "GroupID" serial NOT NULL,
    "TreatmentID" INT NOT NULL,
    "AllocationMethod" VARCHAR(30) NOT NULL,
    PRIMARY KEY ("GroupID"),
    FOREIGN KEY ("TreatmentID") REFERENCES "Treatment" ("TreatmentID")
);


/*
type: relationship
relation:  Experiment(1) observes (N)Endpoint
*/
CREATE TABLE "ObservesEndpoint"
(
    "EndpointID" INT NOT NULL,
    "ExperimentID" INT NOT NULL,
    PRIMARY KEY ("EndpointID", "ExperimentID"),
    FOREIGN KEY ("EndpointID") REFERENCES "Endpoint" ("EndpointID"),
    FOREIGN KEY ("ExperimentID") REFERENCES "Experiment" ("ExperimentID")
);

/*
type: relationship
relation:  researcher(s)(M) conduct(s) (N)Experiment
*/
CREATE TABLE "Conducts"
(
    "ExperimentID" INT NOT NULL,
    "ResearcherID" INT NOT NULL,
    PRIMARY KEY ("ExperimentID", "ResearcherID"),
    FOREIGN KEY ("ExperimentID") REFERENCES "Experiment" ("ExperimentID"),
    FOREIGN KEY ("ResearcherID") REFERENCES "Researcher" ("ResearcherID")
);

/*
type: relationship
relation:  Experiment(1) observes (N)Factors
*/
CREATE TABLE "HasFactors"
(
    "FactorID" INT NOT NULL,
    "ExperimentID" INT NULL,
    PRIMARY KEY ("FactorID", "ExperimentID"),
    FOREIGN KEY ("FactorID") REFERENCES "Factor" ("FactorID"),
    FOREIGN KEY ("ExperimentID") REFERENCES "Experiment" ("ExperimentID")
);

/*
type: relationship
relation:  Experiment(1) has (N)Treatments
*/
CREATE TABLE "HasTreatment"
(
    "TreatmentID" INT NOT NULL,
    "ExperimentID" INT NOT NULL,
    PRIMARY KEY ("TreatmentID", "ExperimentID"),
    FOREIGN KEY ("TreatmentID") REFERENCES "Treatment" ("TreatmentID"),
    FOREIGN KEY ("ExperimentID") REFERENCES "Experiment" ("ExperimentID")
);

/*
type: relationship
relation: treatment(1) R (N)PairSimpleFactorLevel
*/
CREATE TABLE "TreatmentLevels"
(
    "TreatmentID" INT NOT NULL,
    "PairFactorLevelID" INT NOT NULL,
    PRIMARY KEY ("TreatmentID", "PairFactorLevelID"),
    FOREIGN KEY ("TreatmentID") REFERENCES "Treatment" ("TreatmentID"),
    FOREIGN KEY ("PairFactorLevelID") REFERENCES "PairSimpleFactorLevel" ("PairFactorLevelID")
);

/*
type: relationship
relation:  Experiment(1) organises into (N)Session
*/
CREATE TABLE "OrganisesIntoSession"
(
    "SessionID" INT NOT NULL,
    "ExperimentID" INT NOT NULL,
    PRIMARY KEY ("SessionID", "ExperimentID"),
    FOREIGN KEY ("SessionID") REFERENCES "Session" ("SessionID"),
    FOREIGN KEY ("ExperimentID") REFERENCES "Experiment" ("ExperimentID")
);

/*
type: relationship
relation:  Session(M) measure(s) (N)ExperimentalUnit
*/
CREATE TABLE "MeasuresUnit"
(
    "SessionID" INT NOT NULL,
    "ExperimentalUnitID" INT NOT NULL,
    PRIMARY KEY ("SessionID", "ExperimentalUnitID"),
    FOREIGN KEY ("SessionID") REFERENCES "Session" ("SessionID"),
    FOREIGN KEY ("ExperimentalUnitID") REFERENCES "ExperimentalUnit" ("ExperimentalUnitID")
);

/*
type: relationship
relation:  Session(M) adminster(s) (N)Treatment
*/
CREATE TABLE "AdminstersTreatment"
(
    "SessionID" INT NOT NULL,
    "TreatmentID" INT NOT NULL,
    PRIMARY KEY ("SessionID", "TreatmentID"),
    FOREIGN KEY ("SessionID") REFERENCES "Session" ("SessionID"),
    FOREIGN KEY ("TreatmentID") REFERENCES "Treatment" ("TreatmentID")
);

/*
type: relationship
relation:  Group(1) groups (N)ExperimentalUnit
*/
CREATE TABLE "GroupsUnit"
(
    "ExperimentalUnitID" INT NOT NULL,
    "GroupID" INT NOT NULL,
    PRIMARY KEY("ExperimentalUnitID", "GroupID"),
    FOREIGN KEY ("ExperimentalUnitID") REFERENCES "ExperimentalUnit" ("ExperimentalUnitID"),
    FOREIGN KEY ("GroupID") REFERENCES "Group" ("GroupID")
);

/*
type: relationship
relation:  ExperimentalUnit(M) get (N)Endpoint
*/
CREATE TABLE "GetObservedValue"
(
    "ExperimentalUnitID" INT NOT NULL,
    "EndpointID" INT NOT NULL,
    PRIMARY KEY ("ExperimentalUnitID", "EndpointID"),
    FOREIGN KEY ("ExperimentalUnitID") REFERENCES "ExperimentalUnit" ("ExperimentalUnitID"),
    FOREIGN KEY ("EndpointID") REFERENCES "Endpoint" ("EndpointID")
);
