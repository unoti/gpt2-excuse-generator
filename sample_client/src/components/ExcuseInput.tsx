import React, { FunctionComponent } from 'react';
import { Label } from 'office-ui-fabric-react/lib/Label';
import { TextField } from 'office-ui-fabric-react/lib/TextField';

type ExcuseInputProps = {
    assignment: string,
}

export const ExcuseInput: FunctionComponent<ExcuseInputProps> = ({assignment}) => {
    const assignmentFieldId = 'assignmentField';
    return (
        <aside>
            <h1>Excuse</h1>
            <Label htmlFor={assignmentFieldId}>My assignment was to</Label>
            <TextField id={assignmentFieldId} />
        </aside>
    );
}
 