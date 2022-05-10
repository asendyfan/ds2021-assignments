import insert_Patient
import insert_Experiment
import insert_Stimulus
import insert_Session
import insert_LinkTreatment
import insert_LinkEEGMeasure
import insert_LinkfNIRSMeasure
import insert_LinkOrganised
import insert_LinkParticipate
import insert_fNIRS
import insert_EEG


def stagingData(database='project', user='postgres', password='19980806', port='5432'):
    """populating all tables in staging area"""
    print("------Start populating staging area------\n")
    insert_Patient.insert_Patient(database=database, user=user, password=password, port=port)
    insert_Experiment.insert_Experiment(database=database, user=user, password=password, port=port)
    insert_Stimulus.insert_Stimulus(database=database, user=user, password=password, port=port)
    insert_Session.insert_Session(database=database, user=user, password=password, port=port)
    insert_LinkTreatment.insert_LinkTreatment(database=database, user=user, password=password, port=port)
    insert_LinkEEGMeasure.insert_LinkEEGMeasure(database=database, user=user, password=password, port=port)
    insert_LinkfNIRSMeasure.insert_LinkfNIRSMeasure(database=database, user=user, password=password, port=port)
    insert_LinkOrganised.insert_LinkOrganised(database=database, user=user, password=password, port=port)
    insert_LinkParticipate.insert_LinkParticipate(database=database, user=user, password=password, port=port)
    insert_fNIRS.insert_fNIRS(database=database, user=user, password=password, port=port)
    insert_EEG.insert_EEG(database=database, user=user, password=password, port=port)


if __name__ == "__main__":
    stagingData(database='project', user='postgres', password='19980806', port='5432')
