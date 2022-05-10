--select HubExperiment.ExperimentID,SatExperiment.title,SatExperiment.typebynumberofsessions,SatExperiment.typebyallocation,SatExperiment.loaddate,SatExperiment.loadenddate,SatExperiment.recordsource from HubExperiment INNER JOIN SatExperiment ON HubExperiment.ExperimentHashKey=SatExperiment.ExperimentHashKey;
--select HubPatient.patientid,SatPatient.patientname,SatPatient.patientage,SatPatient.patientsex from HubPatient INNER JOIN SatPatient ON HubPatient.PatientHashkey=SatPatient.PatientHashkey;
--select * from HubSession;
--select * from HubStimulus INNER JOIN SatStimulus ON HubStimulus.StimulusHashkey=SatStimulus.StimulusHashkey;

/*
--example of selecting eeg data
SELECT HUB1.sessionid,HUB2.Stimulusid,SAT1.Stimuluslevel,SAT.recordsource,HubEEGData.eegdataid,SAT.eegdata[1:3][10:10] FROM HubEEGData
INNER JOIN SatEEGData AS SAT ON HubEEGData.EEGDataHashKey=SAT.EEGDataHashKey
INNER JOIN LinkEEGMeasure AS LINK ON HubEEGData.EEGDataHashKey=LINK.EEGDataHashKey
INNER JOIN HubSession AS HUB1 ON LINK.SessionHashKey=HUB1.SessionHashKey
INNER JOIN LinkTreatment AS LINK1 ON HUB1.SessionHashKey=LINK1.SessionHashKey
INNER JOIN HubStimulus AS HUB2 ON LINK1.StimulusHashKey=HUB2.StimulusHashKey
INNER JOIN SatStimulus AS SAT1 ON HUB2.StimulusHashKey=SAT1.StimulusHashKey;
*/

/*
--example of selecting fnirs.mes data
SELECT HUB1.sessionid,HUB2.Stimulusid,SAT1.Stimuluslevel,HUB.fnirsdataid,SAT.recordsource,SAT.mes[3:3][1:3],SAT.wavelength1[1][1:3],SAT.wavelength2[1][1:3] 
FROM HubFNIRSData AS HUB 
INNER JOIN SatMESData AS SAT ON HUB.fnirsdatahashkey=SAT.fnirsdatahashkey
INNER JOIN LinkFNIRSMeasure AS LINK ON HUB.fnirsdatahashkey=LINK.fnirsdatahashkey
INNER JOIN HubSession AS HUB1 ON LINK.SessionHashKey=HUB1.SessionHashKey
INNER JOIN LinkTreatment AS LINK1 ON HUB1.SessionHashKey=LINK1.SessionHashKey
INNER JOIN HubStimulus AS HUB2 ON LINK1.StimulusHashKey=HUB2.StimulusHashKey
INNER JOIN SatStimulus AS SAT1 ON HUB2.StimulusHashKey=SAT1.StimulusHashKey
ORDER BY SAT.recordsource;
*/

/*
--example of selecting fnirs.hba data
SELECT HUB1.sessionid,HUB2.Stimulusid,SAT1.Stimuluslevel,HUB.fnirsdataid,SAT.recordsource,SAT.oxy[2:2][1:2],SAT.deoxy[2:2][1:2],SAT.total[2:2][1:2],SAT.hb
FROM HubFNIRSData AS HUB 
INNER JOIN SatHBAData AS SAT ON HUB.fnirsdatahashkey=SAT.fnirsdatahashkey
INNER JOIN LinkFNIRSMeasure AS LINK ON HUB.fnirsdatahashkey=LINK.fnirsdatahashkey
INNER JOIN HubSession AS HUB1 ON LINK.SessionHashKey=HUB1.SessionHashKey
INNER JOIN LinkTreatment AS LINK1 ON HUB1.SessionHashKey=LINK1.SessionHashKey
INNER JOIN HubStimulus AS HUB2 ON LINK1.StimulusHashKey=HUB2.StimulusHashKey
INNER JOIN SatStimulus AS SAT1 ON HUB2.StimulusHashKey=SAT1.StimulusHashKey
WHERE SAT.oxy IS NOT NULL
ORDER BY SAT.recordsource;
*/

--select SAT.fnirsdatahashkey,SAT.recordsource,HUB.fnirsdataid,SAT.oxy[1][1],SAT.deoxy[1][1],SAT.total[1][1] from HubFNIRSData AS HUB INNER JOIN SatHBAData AS SAT ON HUB.fnirsdatahashkey=SAT.fnirsdatahashkey WHERE SAT.oxy IS NOT NULL ORDER BY SAT.recordsource;
--select SAT.fnirsdatahashkey,SAT.recordsource,HUB.fnirsdataid,SAT.mes[1][1],SAT.wavelength1[1][1],SAT.wavelength2[1][1] from HubFNIRSData AS HUB INNER JOIN SatMESData AS SAT ON HUB.fnirsdatahashkey=SAT.fnirsdatahashkey ORDER BY SAT.recordsource;