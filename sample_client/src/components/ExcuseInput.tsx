import React, { FunctionComponent, useState } from 'react';
import { Label } from 'office-ui-fabric-react/lib/Label';
import { TextField } from 'office-ui-fabric-react/lib/TextField';
import { PrimaryButton } from 'office-ui-fabric-react';

import { ExcuseScenario } from '../models';

type ExcuseInputProps = {
    scenario: ExcuseScenario,
    onSubmit: any
}

export const ExcuseInput: FunctionComponent<ExcuseInputProps> = ({scenario, onSubmit}) => {
    const assignmentFieldId = 'assignmentField';
    const stepIds = ['step1','step2','step3','step4','step5']
    return (
        <div>
            <h1>Excuse</h1>
            <Label htmlFor={assignmentFieldId}>My assignment was to</Label>
            <TextField id={assignmentFieldId} value={scenario.assignment}/>
            <div>Steps I would take:</div>
            <TextField id={stepIds[0]} value={scenario.tasks[0]}/>
            <TextField id={stepIds[1]} value={scenario.tasks[1]}/>
            <TextField id={stepIds[2]} value={scenario.tasks[2]}/>
            <TextField id={stepIds[3]} value={scenario.tasks[3]}/>
            <TextField id={stepIds[4]} value={scenario.tasks[4]}/>
            <PrimaryButton text="Make Excuses" onClick={onSubmit(scenario)}/>
        </div>
    );
}
