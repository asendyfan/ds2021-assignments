--select * from staging.experiment;
--select * from staging.patient;
--select * from staging.session;
--select * from staging.stimulus;
--select hashkey,recordsource,eegdataid,eegdata[1][33] from staging.eeg;
--select fnirsdatahashkey,recordsource,fnirsdataid,oxy[1][1],deoxy[1][1],total[1][1],mes[1][1],wavelength1[1][1],wavelength2[1][1] from staging.fnirs order by recordsource;
--select * from staging.linktreatment;
--select * from staging.linkparticipate;
--select * from staging.linkorganised;
--select * from staging.linkeegmeasure;
--select * from staging.linkfnirsmeasure;