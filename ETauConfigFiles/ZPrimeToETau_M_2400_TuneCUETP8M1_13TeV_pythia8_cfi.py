import FWCore.ParameterSet.Config as cms

# for taus
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import * 
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
        comEnergy = cms.double(13000.0),
        crossSection = cms.untracked.double(1),
        filterEfficiency = cms.untracked.double(1),
        maxEventsToPrint = cms.untracked.int32(0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        pythiaPylistVerbosity = cms.untracked.int32(1),
        ExternalDecays = cms.PSet(Tauola = cms.untracked.PSet(TauolaPolar, TauolaDefaultInputCards ), 
                                                              parameterSets = cms.vstring('Tauola') 
                                                             ), 
        PythiaParameters = cms.PSet(
                pythia8CommonSettingsBlock,
                pythia8CUEP8M1SettingsBlock,
                processParameters = cms.vstring(
                        'NewGaugeBoson:ffbar2gmZZprime= on',         #get new gauge boson process 
                        'Zprime:gmZmode = 3',                        #only Zprime contributions without any interferences
                        '32:m0= 2400',                               #set pole mass of resonancei
                        '32:addChannel= 1 0.1 100 11 -15',
                        '32:addChannel= 1 0.1 100 15 -11',
                        '32:onMode= off',                            #set default to switched-off decay modes
                        '32:onIfMatch= 15 -11',                      #allow decay to Tau + electron  
                        '32:onIfMatch= 11 -15',
                ),
                parameterSets = cms.vstring('pythia8CommonSettings',
                                            'pythia8CUEP8M1Settings',
                                            'processParameters')
        )
)
ProductionFilterSequence = cms.Sequence(generator)
