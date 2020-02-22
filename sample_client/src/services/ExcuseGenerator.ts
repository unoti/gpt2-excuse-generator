import * as socketIo from 'socket.io-client';

import { ExcuseScenario } from '../models';

const SERVER_URL = 'http://localhost:5000'

export class ExcuseGeneratorSession {
    scenario: ExcuseScenario;
    excuses: string[];
    updateCallback: any;
    socket: any;

    constructor(scenario: ExcuseScenario, onUpdated: any) {
        this.scenario = scenario;
        this.excuses = [];
        this.updateCallback = onUpdated;
        this.socket = null;
    }

    startGenerating = () => {
        console.log('start');
        this.socket = socketIo.connect(SERVER_URL);
        this.socket.on('connect', () => {
            this.socket.emit('my event', {'data': 'I have connected'});
        });
        setTimeout(this.updateCallback, 1000);
    }

    stopGenerating = () => {
        console.log('stop');
    }
}