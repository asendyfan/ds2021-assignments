-- first, need to create a new schema named staging in the same database as the data warehouse layer
-- full implementation of populating the staging area is via Python using psycopg2
----------------------------------------------------------------------------------------------------
create table staging.Experiment(
	ExperimentHashKey text,
	RecordSource varchar(100) NOT NULL,
	ExperimentID varchar(50) NOT NULL,
	Title varchar(100) NOT NULL,
	Goal text,
	TypeByNumberOfSessions typeNumberOfSession NOT NULL,
	TypeByAllocation typeAllocation NOT NULL
	);

create table staging.Session(
	sessionhashkey text,
	recordsource varchar(100), 
	sessionid varchar(50)
	);

create table staging.Stimulus(
	stimulushashkey text,
	recordsource varchar(100),
	stimulusid varchar(50),
	stimuluslevel varchar(50)
	);

create table staging.Patient(
	patienthashkey text,
	recordsource varchar(100), 
	patientid varchar(50),
	patientname varchar(100),
	patientage int,	
	patientsex typeofsex
	);
	
create table staging.EEG(
	hashkey text,
	recordsource varchar(100), 
	eegdataid varchar(50),
	eegdata float[][]
	);

create table staging.FNIRS(
	fnirsdatahashkey text,
	recordsource varchar(100), 
	fnirsdataid varchar(50),
	Oxy text[][],  -- for dataset 1 csv file
	Deoxy text[][],  -- for dataset 1 csv file
	Total text[][],  -- for dataset 1 csv file
	HB bytea,  -- for dataset 2 dat file
	MES text[][],  -- for dataset 1 csv file
	Wavelength1 float[][],  -- for dataset 2 wl1 file
	Wavelength2 float[][]  -- for dataset 2 wl2 file
	);
	
create table staging.LinkOrganised(
	OrganisedHashKey text PRIMARY KEY,
	RecordSource varchar(100) NOT NULL,
	ExperimentHashKey text NOT NULL,
	SessionHashKey text NOT NULL
	);

create table staging.LinkTreatment(
	TreatmentHashKey text PRIMARY KEY,
	RecordSource varchar(100) NOT NULL,
	SessionHashKey text NOT NULL,
	StimulusHashKey text NOT NULL
	);

create table staging.LinkParticipate(
	ParticipateHashKey text PRIMARY KEY,
	RecordSource varchar(100) NOT NULL,
	SessionHashKey text NOT NULL,
	PatientHashKey text NOT NULL
	);
	
create table staging.LinkEEGMeasure(
	EEGMeasureHashKey text PRIMARY KEY,
	RecordSource varchar(100) NOT NULL,
	SessionHashKey text NOT NULL,
	EEGDataHashKey text NOT NULL
	);

create table staging.LinkFNIRSMeasure(
	FNIRSMeasureHashKey text PRIMARY KEY,
	RecordSource varchar(100) NOT NULL,
	SessionHashKey text NOT NULL,
	FNIRSDataHashKey text NOT NULL
	);