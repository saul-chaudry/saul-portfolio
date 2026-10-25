import {test} from 'node:test';import assert from 'node:assert/strict';import {aggregate,anomaly} from './core.ts';
test('integer cents and team attribution',()=>{assert.deepEqual(aggregate([{team:'a',service:'x',cents:100},{team:'a',service:'y',cents:20}]),[{team:'a',cents:120}]);assert.throws(()=>aggregate([{team:'a',service:'x',cents:1.2}]))});
test('baseline requires evidence',()=>{assert.equal(anomaly(999,[1,2]).alert,false);assert.equal(anomaly(301,[100,100,100]).alert,true);assert.equal(anomaly(100,[100,100,100]).alert,false)});
