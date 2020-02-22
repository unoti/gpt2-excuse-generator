import React, { useState } from 'react';
import { Stack } from 'office-ui-fabric-react';

import { ExcuseScenario } from '../models';
import { ExcuseInput, ExcuseOutput } from '../components';
import { ExcuseGeneratorSession } from '../services';

const startScenario: ExcuseScenario = {
  assignment: 'take the trash out and clean the kitchen',
  tasks: [
    'assess the current trash levels',
    'gather up the loose overflow trash items',
    'remove the bag from the can',
    'tie the bag',
    'take it to the outside bin',
    'put a new bag into the can'
  ]
};

export const Generation: React.FunctionComponent = () => {
  const [scenario, setScenario] = useState(startScenario);
  const [excuses, setExcuses] = useState([]);
  const [session, setSession] = useState<ExcuseGeneratorSession | null>(null);

  function generatedExcusesUpdated() {
    console.log('Generated excuses updated');
  }

  function onGenerate(sc: ExcuseScenario) {
    if (session) {
        session.stopGenerating();
    }
    setScenario(sc);
    let s = new ExcuseGeneratorSession(sc, generatedExcusesUpdated)
    setSession(s);
    s.startGenerating();
  }

  return (
    <Stack>
    <ExcuseInput scenario={startScenario} onSubmit={onGenerate}/>
    <ExcuseOutput excuses={excuses}/>
    </Stack>
  );
};
