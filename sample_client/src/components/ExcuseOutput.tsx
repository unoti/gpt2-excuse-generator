import React, { FunctionComponent } from 'react';

type ExcuseOutputProps = {
    excuses: string[],
}

function showExcuses(excuses: string[]) {
    return excuses.map(e => '<li>' + e + '</li>');
}

export const ExcuseOutput: FunctionComponent<ExcuseOutputProps> = ({excuses}) => {
    return (
        <div>
            <h1>Generated Excuses</h1>
            <ul>
                {showExcuses(excuses)}
            </ul>
        </div>
    );
}
