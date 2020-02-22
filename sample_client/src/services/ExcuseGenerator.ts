import { ExcuseScenario } from '../models';

export class ExcuseGeneratorSession {
    scenario: ExcuseScenario;
    excuses: string[];
    updateCallback: any;

    constructor(scenario: ExcuseScenario, onUpdated: any) {
        this.scenario = scenario;
        this.excuses = [];
        this.updateCallback = onUpdated;
    }

    startGenerating = () => {
        console.log('start');
        setTimeout(this.updateCallback, 1000);
    }

    stopGenerating = () => {
        console.log('stop');
    }
}