/*
-- queryExperiment.csv
copy (select HubExperiment.ExperimentID, SatExperiment.title, SatExperiment.typebynumberofsessions, SatExperiment.typebyallocation, SatExperiment.loaddate, SatExperiment.loadenddate, SatExperiment.recordsource from HubExperiment INNER JOIN SatExperiment ON HubExperiment.ExperimentHashKey = SatExperiment.ExperimentHashKey)
to 'D:\DATA_SCIENCE\StoringAndManagingData\project\SMD2021_Project_Group08\results\data_vault\queryExperiment.csv' with csv header;
*/

/*
-- queryPatient.csv
copy (select HubPatient.patientid, SatPatient.patientname, SatPatient.patientage, SatPatient.patientsex from HubPatient INNER JOIN SatPatient ON HubPatient.PatientHashkey = SatPatient.PatientHashkey)
to 'D:\DATA_SCIENCE\StoringAndManagingData\project\SMD2021_Project_Group08\results\data_vault\queryPatient.csv' with csv header;
*/

/*
-- queryEEGData.csv
-- This is just an example. The EEG data is stored in 2d array, which could be visited by indexes and slices. Here is just a slice example to verify, as the data is so huge.
copy (
SELECT HUB1.sessionid, HUB2.Stimulusid, SAT1.Stimuluslevel, SAT.recordsource, HubEEGData.eegdataid, SAT.eegdata[1:3][10:10] 
FROM HubEEGData
INNER JOIN SatEEGData AS SAT ON HubEEGData.EEGDataHashKey=SAT.EEGDataHashKey
INNER JOIN LinkEEGMeasure AS LINK ON HubEEGData.EEGDataHashKey=LINK.EEGDataHashKey
INNER JOIN HubSession AS HUB1 ON LINK.SessionHashKey=HUB1.SessionHashKey
INNER JOIN LinkTreatment AS LINK1 ON HUB1.SessionHashKey=LINK1.SessionHashKey
INNER JOIN HubStimulus AS HUB2 ON LINK1.StimulusHashKey=HUB2.StimulusHashKey
INNER JOIN SatStimulus AS SAT1 ON HUB2.StimulusHashKey=SAT1.StimulusHashKey)
to 'D:\DATA_SCIENCE\StoringAndManagingData\project\SMD2021_Project_Group08\results\data_vault\queryEEGData.csv' with csv header;
*/

/*
-- queryFNIRS_MES.csv
-- This is just an example for light measurements of FNIRS data. The data are stored in 2d array, which could be visited by indexes and slices. Here is just a slice example to verify, as the data is so huge.
copy (
SELECT HUB1.sessionid, HUB2.Stimulusid, SAT1.Stimuluslevel, HUB.fnirsdataid, SAT.recordsource, SAT.mes[3:3][1:3], SAT.wavelength1[1][1:3], SAT.wavelength2[1][1:3] 
FROM HubFNIRSData AS HUB 
INNER JOIN SatMESData AS SAT ON HUB.fnirsdatahashkey=SAT.fnirsdatahashkey
INNER JOIN LinkFNIRSMeasure AS LINK ON HUB.fnirsdatahashkey=LINK.fnirsdatahashkey
INNER JOIN HubSession AS HUB1 ON LINK.SessionHashKey=HUB1.SessionHashKey
INNER JOIN LinkTreatment AS LINK1 ON HUB1.SessionHashKey=LINK1.SessionHashKey
INNER JOIN HubStimulus AS HUB2 ON LINK1.StimulusHashKey=HUB2.StimulusHashKey
INNER JOIN SatStimulus AS SAT1 ON HUB2.StimulusHashKey=SAT1.StimulusHashKey
ORDER BY SAT.recordsource)
to 'D:\DATA_SCIENCE\StoringAndManagingData\project\SMD2021_Project_Group08\results\data_vault\queryFNIRS_MES.csv' with csv header;
*/

/*
-- queryFNIRS_HBA.csv
-- This is just an example for HB analysis of FNIRS data. The data are stored in 2d array, which could be visited by indexes and slices. Here is just a slice example to verify, as the data is so huge.
copy (
SELECT HUB1.sessionid,HUB2.Stimulusid,SAT1.Stimuluslevel,HUB.fnirsdataid,SAT.recordsource,SAT.oxy[2:2][1:2],SAT.deoxy[2:2][1:2],SAT.total[2:2][1:2],SAT.hb
FROM HubFNIRSData AS HUB 
INNER JOIN SatHBAData AS SAT ON HUB.fnirsdatahashkey=SAT.fnirsdatahashkey
INNER JOIN LinkFNIRSMeasure AS LINK ON HUB.fnirsdatahashkey=LINK.fnirsdatahashkey
INNER JOIN HubSession AS HUB1 ON LINK.SessionHashKey=HUB1.SessionHashKey
INNER JOIN LinkTreatment AS LINK1 ON HUB1.SessionHashKey=LINK1.SessionHashKey
INNER JOIN HubStimulus AS HUB2 ON LINK1.StimulusHashKey=HUB2.StimulusHashKey
INNER JOIN SatStimulus AS SAT1 ON HUB2.StimulusHashKey=SAT1.StimulusHashKey
WHERE SAT.oxy IS NOT NULL
ORDER BY SAT.recordsource)
to 'D:\DATA_SCIENCE\StoringAndManagingData\project\SMD2021_Project_Group08\results\data_vault\queryFNIRS_HBA.csv' with csv header;
*/