import React from 'react';
import { Stack, Text, FontWeights } from 'office-ui-fabric-react';

import './App.css';
import ShrugImage from './images/tanya.png';
import { Generation } from './components';

const boldStyle = { root: { fontWeight: FontWeights.semibold } };

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
      <Generation />
    </Stack>
  );
};
