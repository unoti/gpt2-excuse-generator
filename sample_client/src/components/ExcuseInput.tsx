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
    const stepIds = ['step1','step2','step3','step4','step5'];
    // useState returns 2 values: currentState, and a function that updates it.
    const [sc, setScenario] = useState(scenario);
    function assignmentChange(e:any) {
        let val = e.target.defaultValue;
        setScenario({...sc, assignment: val});
    }
    function taskChange(seq: number, val: string) {
        let tasks = sc.tasks.slice(); // clone list.
        tasks[seq] = val;
        setScenario({...sc, tasks: tasks});
    }
    function updateTask(seq: number) {
        function handler(e: any) {
            let val = e.target.defaultValue;
            taskChange(seq, val);
        }
        return handler;
    }
    function submit() {
        onSubmit(sc);
    }

    return (
        <div>
            <h1>Excuse</h1>
            <Label htmlFor={assignmentFieldId}>My assignment was to</Label>
            <TextField id={assignmentFieldId} value={sc.assignment} onChange={assignmentChange}/>
            <div>Steps I would take:</div>
            <TextField id={stepIds[0]} value={sc.tasks[0]} onChange={updateTask(0)}/>
            <TextField id={stepIds[1]} value={sc.tasks[1]} onChange={updateTask(1)}/>
            <TextField id={stepIds[2]} value={sc.tasks[2]} onChange={updateTask(2)}/>
            <TextField id={stepIds[3]} value={sc.tasks[3]} onChange={updateTask(3)}/>
            <TextField id={stepIds[4]} value={sc.tasks[4]} onChange={updateTask(4)}/>
            <PrimaryButton text="Make Excuses" onClick={submit}/>
        </div>
    );
}
