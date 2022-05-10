ALTER TABLE staging.Experiment ADD COLUMN LoadDate timestamp;
UPDATE staging.Experiment SET LoadDate = (SELECT CURRENT_TIMESTAMP);
INSERT INTO HubExperiment(ExperimentHashKey, RecordSource, LoadDate, ExperimentID)
SELECT ExperimentHashKey, RecordSource, LoadDate, ExperimentID FROM staging.Experiment;

ALTER TABLE staging.Session ADD COLUMN LoadDate timestamp;
UPDATE staging.Session SET LoadDate = (SELECT CURRENT_TIMESTAMP);
INSERT INTO HubSession(SessionHashKey, RecordSource, LoadDate, SessionID)
SELECT sessionhashkey, recordsource, LoadDate, sessionid FROM staging.Session;

ALTER TABLE staging.Stimulus ADD COLUMN LoadDate timestamp;
UPDATE staging.Stimulus SET LoadDate = (SELECT CURRENT_TIMESTAMP);
INSERT INTO HubStimulus(StimulusHashKey, RecordSource, LoadDate, StimulusID)
SELECT stimulushashkey, recordsource, LoadDate, stimulusid FROM staging.Stimulus;

ALTER TABLE staging.Patient ADD COLUMN LoadDate timestamp;
UPDATE staging.Patient SET LoadDate = (SELECT CURRENT_TIMESTAMP);
INSERT INTO HubPatient(PatientHashKey, RecordSource, LoadDate, PatientID)
SELECT patienthashkey, recordsource, LoadDate, patientid FROM staging.Patient;

ALTER TABLE staging.EEG ADD COLUMN LoadDate timestamp;
UPDATE staging.EEG SET LoadDate = (SELECT CURRENT_TIMESTAMP);
INSERT INTO HubEEGData(EEGDataHashKey, RecordSource, LoadDate, EEGDataID)
SELECT hashkey, recordsource, LoadDate, eegdataid FROM staging.EEG;

ALTER TABLE staging.FNIRS ADD COLUMN LoadDate timestamp;
UPDATE staging.FNIRS SET LoadDate = (SELECT CURRENT_TIMESTAMP);
INSERT INTO HubFNIRSData(FNIRSDataHashKey, RecordSource, LoadDate, FNIRSDataID)
SELECT fnirsdatahashkey, recordsource, LoadDate, fnirsdataid FROM staging.FNIRS;

ALTER TABLE staging.LinkOrganised ADD COLUMN LoadDate timestamp;
UPDATE staging.LinkOrganised SET LoadDate = (SELECT CURRENT_TIMESTAMP);
INSERT INTO LinkOrganised(OrganisedHashKey, RecordSource, LoadDate, ExperimentHashKey, SessionHashKey)
SELECT OrganisedHashKey, RecordSource, LoadDate, ExperimentHashKey, SessionHashKey FROM staging.LinkOrganised;

ALTER TABLE staging.LinkTreatment ADD COLUMN LoadDate timestamp;
UPDATE staging.LinkTreatment SET LoadDate = (SELECT CURRENT_TIMESTAMP);
INSERT INTO LinkTreatment(TreatmentHashKey, RecordSource, LoadDate, SessionHashKey, StimulusHashKey)
SELECT TreatmentHashKey, RecordSource, LoadDate, SessionHashKey, StimulusHashKey FROM staging.LinkTreatment;

ALTER TABLE staging.LinkParticipate ADD COLUMN LoadDate timestamp;
UPDATE staging.LinkParticipate SET LoadDate = (SELECT CURRENT_TIMESTAMP);
INSERT INTO LinkParticipate(ParticipateHashKey, RecordSource, LoadDate, SessionHashKey, PatientHashKey)
SELECT ParticipateHashKey, RecordSource, LoadDate, SessionHashKey, PatientHashKey FROM staging.LinkParticipate;

ALTER TABLE staging.LinkEEGMeasure ADD COLUMN LoadDate timestamp;
UPDATE staging.LinkEEGMeasure SET LoadDate = (SELECT CURRENT_TIMESTAMP);
INSERT INTO LinkEEGMeasure(EEGMeasureHashKey, RecordSource, LoadDate, SessionHashKey, EEGDataHashKey)
SELECT EEGMeasureHashKey, RecordSource, LoadDate, SessionHashKey, EEGDataHashKey FROM staging.LinkEEGMeasure;

ALTER TABLE staging.LinkFNIRSMeasure ADD COLUMN LoadDate timestamp;
UPDATE staging.LinkFNIRSMeasure SET LoadDate = (SELECT CURRENT_TIMESTAMP);
INSERT INTO LinkFNIRSMeasure(FNIRSMeasureHashKey, RecordSource, LoadDate, SessionHashKey, FNIRSDataHashKey)
SELECT FNIRSMeasureHashKey, RecordSource, LoadDate, SessionHashKey, FNIRSDataHashKey FROM staging.LinkFNIRSMeasure;

ALTER TABLE staging.Experiment ADD COLUMN LoadEndDate timestamp;
UPDATE staging.Experiment SET LoadEndDate = '9999-12-31 23:59:59';
INSERT INTO SatExperiment(ExperimentHashKey, RecordSource, LoadDate, LoadEndDate, Title, Goal, TypeByNumberOfSessions, TypeByAllocation)
SELECT ExperimentHashKey, RecordSource, LoadDate, LoadEndDate, Title, Goal, TypeByNumberOfSessions, TypeByAllocation FROM staging.Experiment;

ALTER TABLE staging.Stimulus ADD COLUMN LoadEndDate timestamp;
UPDATE staging.Stimulus SET LoadEndDate = '9999-12-31 23:59:59';
INSERT INTO SatStimulus(StimulusHashKey, RecordSource, LoadDate, LoadEndDate, StimulusLevel)
SELECT stimulushashkey, recordsource, LoadDate, LoadEndDate, stimuluslevel FROM staging.Stimulus;

ALTER TABLE staging.Patient ADD COLUMN LoadEndDate timestamp;
UPDATE staging.Patient SET LoadEndDate = '9999-12-31 23:59:59';
INSERT INTO SatPatient(PatientHashKey, RecordSource, LoadDate, LoadEndDate, PatientName, PatientAge, PatientSex)
SELECT patienthashkey, recordsource, LoadDate, LoadEndDate, patientname, patientage, patientsex FROM staging.Patient;

ALTER TABLE staging.FNIRS ADD COLUMN LoadEndDate timestamp;
UPDATE staging.FNIRS SET LoadEndDate = '9999-12-31 23:59:59';
INSERT INTO SatHBAData(FNIRSDataHashKey, RecordSource, LoadDate, LoadEndDate, Oxy, Deoxy, Total, HB)
SELECT fnirsdatahashkey, recordsource, LoadDate, LoadEndDate, Oxy, Deoxy, Total, HB FROM staging.FNIRS;

INSERT INTO SatMESData(FNIRSDataHashKey, RecordSource, LoadDate, LoadEndDate, MES, Wavelength1, Wavelength2)
SELECT fnirsdatahashkey, recordsource, LoadDate, LoadEndDate, MES, Wavelength1, Wavelength2 FROM staging.FNIRS;

ALTER TABLE staging.EEG ADD COLUMN LoadEndDate timestamp;
UPDATE staging.EEG SET LoadEndDate = '9999-12-31 23:59:59';
INSERT INTO SatEEGData(EEGDataHashKey, RecordSource, LoadDate, LoadEndDate, EEGData)
SELECT hashkey, recordsource, LoadDate, LoadEndDate, eegdata FROM staging.EEG;