CREATE TABLE HubExperiment (
	ExperimentHashKey text PRIMARY KEY,
	LoadDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	ExperimentID varchar(50) NOT NULL);

CREATE TABLE HubSession (
	SessionHashKey text PRIMARY KEY,
	LoadDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	SessionID varchar(50) NOT NULL);

CREATE TABLE HubStimulus (
	StimulusHashKey text PRIMARY KEY,
	LoadDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	StimulusID varchar(50) NOT NULL);

CREATE TABLE HubPatient (
	PatientHashKey text PRIMARY KEY,
	LoadDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	PatientID varchar(50) NOT NULL);

CREATE TABLE HubEEGData (
	EEGDataHashKey text PRIMARY KEY,
	LoadDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	EEGDataID varchar(50) NOT NULL);

CREATE TABLE HubFNIRSData (
	FNIRSDataHashKey text PRIMARY KEY,
	LoadDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	FNIRSDataID varchar(50) NOT NULL);

CREATE TABLE LinkOrganised (
	OrganisedHashKey text PRIMARY KEY,
	LoadDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	ExperimentHashKey text NOT NULL,
	SessionHashKey text NOT NULL,
	FOREIGN KEY(ExperimentHashKey) REFERENCES HubExperiment(ExperimentHashKey),
	FOREIGN KEY(SessionHashKey) REFERENCES HubSession(SessionHashKey));
	
CREATE TABLE LinkTreatment (
	TreatmentHashKey text PRIMARY KEY,
	LoadDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	SessionHashKey text NOT NULL,
	StimulusHashKey text NOT NULL,
	FOREIGN KEY(SessionHashKey) REFERENCES HubSession(SessionHashKey),
	FOREIGN KEY(StimulusHashKey) REFERENCES HubStimulus(StimulusHashKey));
	
CREATE TABLE LinkParticipate (
	ParticipateHashKey text PRIMARY KEY,
	LoadDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	SessionHashKey text NOT NULL,
	PatientHashKey text NOT NULL,
	FOREIGN KEY(SessionHashKey) REFERENCES HubSession(SessionHashKey),
	FOREIGN KEY(PatientHashKey) REFERENCES HubPatient(PatientHashKey));	
	
CREATE TABLE LinkEEGMeasure (
	EEGMeasureHashKey text PRIMARY KEY,
	LoadDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	SessionHashKey text NOT NULL,
	EEGDataHashKey text NOT NULL,
	FOREIGN KEY(SessionHashKey) REFERENCES HubSession(SessionHashKey),
	FOREIGN KEY(EEGDataHashKey) REFERENCES HubEEGData(EEGDataHashKey));	
	
CREATE TABLE LinkFNIRSMeasure (
	FNIRSMeasureHashKey text PRIMARY KEY,
	LoadDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	SessionHashKey text NOT NULL,
	FNIRSDataHashKey text NOT NULL,
	FOREIGN KEY(FNIRSDataHashKey) REFERENCES HubFNIRSData(FNIRSDataHashKey),
	FOREIGN KEY(SessionHashKey) REFERENCES HubSession(SessionHashKey));	
	
-- create two new enumerate types for two classification methods for "Experiment"
CREATE TYPE typeNumberOfSession AS ENUM ('cross-sectional', 'longitudinal');
CREATE TYPE typeAllocation AS ENUM ('within-subject', 'between-subject');

-- create an enumerate type for sex
CREATE TYPE typeOfSex AS ENUM ('Male', 'Female');

CREATE TABLE SatExperiment (
	ExperimentHashKey text,
	LoadDate timestamp NOT NULL,
	LoadEndDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	Title varchar(100) NOT NULL,
	Goal text,
	TypeByNumberOfSessions typeNumberOfSession NOT NULL,
	TypeByAllocation typeAllocation NOT NULL,
	PRIMARY KEY(ExperimentHashKey, LoadDate),
	FOREIGN KEY(ExperimentHashKey) REFERENCES HubExperiment(ExperimentHashKey));
	
CREATE TABLE SatStimulus (
	StimulusHashKey text,
	LoadDate timestamp NOT NULL,
	LoadEndDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	StimulusLevel varchar(50) NOT NULL,
	PRIMARY KEY(StimulusHashKey, LoadDate),
	FOREIGN KEY(StimulusHashKey) REFERENCES HubStimulus(StimulusHashKey));


CREATE TABLE SatPatient (
	PatientHashKey text,
	LoadDate timestamp NOT NULL,
	LoadEndDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	PatientName varchar(100),
	PatientAge int,
	PatientSex typeOfSex,
	PRIMARY KEY(PatientHashKey, LoadDate),
	FOREIGN KEY(PatientHashKey) REFERENCES HubPatient(PatientHashKey));
	
	
CREATE TABLE SatHBAData (
	FNIRSDataHashKey text,
	LoadDate timestamp NOT NULL,
	LoadEndDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	Oxy text[][],  -- for dataset 1 csv file
	Deoxy text[][],  -- for dataset 1 csv file
	Total text[][],  -- for dataset 1 csv file
	HB bytea,  -- for dataset 2 dat file
	PRIMARY KEY(FNIRSDataHashKey, LoadDate),
	FOREIGN KEY(FNIRSDataHashKey) REFERENCES HubFNIRSData(FNIRSDataHashKey));
	
CREATE TABLE SatMESData (
	FNIRSDataHashKey text,
	LoadDate timestamp NOT NULL,
	LoadEndDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	MES text[][],  -- for dataset 1 csv file
	Wavelength1 float[][],  -- for dataset 2 wl1 file
	Wavelength2 float[][],  -- for dataset 2 wl2 file
	PRIMARY KEY(FNIRSDataHashKey, LoadDate),
	FOREIGN KEY(FNIRSDataHashKey) REFERENCES HubFNIRSData(FNIRSDataHashKey));	
	
CREATE TABLE SatEEGData (
	EEGDataHashKey text,
	LoadDate timestamp NOT NULL,
	LoadEndDate timestamp NOT NULL,
	RecordSource varchar(100) NOT NULL,
	EEGData float[][],  -- for dataset 2 mat file
	PRIMARY KEY(EEGDataHashKey, LoadDate),
	FOREIGN KEY(EEGDataHashKey) REFERENCES HubEEGData(EEGDataHashKey));