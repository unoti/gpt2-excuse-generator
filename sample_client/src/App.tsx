import React from 'react';
import { Stack, Text, FontWeights } from 'office-ui-fabric-react';

import { ExcuseScenario } from './models';
import ShrugImage from './images/tanya.png';
import './App.css';
import { ExcuseInput } from './components/ExcuseInput';

const boldStyle = { root: { fontWeight: FontWeights.semibold } };

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

function onGenerate(scenario: ExcuseScenario) {
  console.log('Generate');
  console.log(scenario);
}

export const App: React.FunctionComponent = () => {
  return (
    <Stack>
      <Stack
        horizontalAlign="center"
        verticalFill
        styles={{
          root: {
            width: '960px',
            margin: '0 auto',
            textAlign: 'center',
            color: '#605e5c'
          }
        }}
        gap={15}
      >
        <img src={ShrugImage} alt="shrug" />
        <Text variant="xxLarge" styles={boldStyle}>
          Excuse Generator
        </Text>
        <div>
          <a href="https://svgsilh.com/png/1641898.png">Tanya</a> image is licensed under&nbsp;
          <a href="https://creativecommons.org/licenses/cc0/1.0/?ref=ccsearch&atype=html">CC 1.0</a>
        </div>
      </Stack>
      <Stack>
        <ExcuseInput scenario={startScenario} onSubmit={onGenerate}/>
      </Stack>
    </Stack>
  );
};

// Creative commons image:
//<img className="cc-icon" src="https://search.creativecommons.org/static/img/cc_icon.svg" />
