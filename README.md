![Async Logo](https://raw.githubusercontent.com/caolan/async/master/logo/async-logo_readme.jpg)

[![Build Status via Travis CI](https://travis-ci.org/caolan/async.svg?branch=master)](https://travis-ci.org/caolan/async)
[![Build Status via Azure Pipelines](https://dev.azure.com/caolanmcmahon/async/_apis/build/status/caolan.async?branchName=master)](https://dev.azure.com/caolanmcmahon/async/_build/latest?definitionId=1&branchName=master)
[![NPM version](https://img.shields.io/npm/v/async.svg)](https://www.npmjs.com/package/async)
[![Coverage Status](https://coveralls.io/repos/caolan/async/badge.svg?branch=master)](https://coveralls.io/r/caolan/async?branch=master)
[![Join the chat at https://gitter.im/caolan/async](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/caolan/async?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![jsDelivr Hits](https://data.jsdelivr.com/v1/package/npm/async/badge?style=rounded)](https://www.jsdelivr.com/package/npm/async)

<!--
|Linux|Windows|MacOS|
|-|-|-|
|[![Linux Build Status](https://dev.azure.com/caolanmcmahon/async/_apis/build/status/caolan.async?branchName=master&jobName=Linux&configuration=Linux%20node_10_x)](https://dev.azure.com/caolanmcmahon/async/_build/latest?definitionId=1&branchName=master) | [![Windows Build Status](https://dev.azure.com/caolanmcmahon/async/_apis/build/status/caolan.async?branchName=master&jobName=Windows&configuration=Windows%20node_10_x)](https://dev.azure.com/caolanmcmahon/async/_build/latest?definitionId=1&branchName=master) | [![MacOS Build Status](https://dev.azure.com/caolanmcmahon/async/_apis/build/status/caolan.async?branchName=master&jobName=OSX&configuration=OSX%20node_10_x)](https://dev.azure.com/caolanmcmahon/async/_build/latest?definitionId=1&branchName=master)| -->

Async is a utility module which provides straight-forward, powerful functions for working with [asynchronous JavaScript](http://caolan.github.io/async/v3/global.html). Although originally designed for use with [Node.js](https://nodejs.org/) and installable via `npm i async`, it can also be used directly in the browser.  A ESM/MJS version is included in the main `async` package that should automatically be used with compatible bundlers such as Webpack and Rollup.

A pure ESM version of Async is available as [`async-es`](https://www.npmjs.com/package/async-es).

For Documentation, visit <https://caolan.github.io/async/>

*For Async v1.5.x documentation, go [HERE](https://github.com/caolan/async/blob/v1.5.2/README.md)*


```javascript
// for use with Node-style callbacks...
var async = require("async");

var obj = {dev: "/dev.json", test: "/test.json", prod: "/prod.json"};
var configs = {};

async.forEachOf(obj, (value, key, callback) => {
    fs.readFile(__dirname + value, "utf8", (err, data) => {
        if (err) return callback(err);
        try {
            configs[key] = JSON.parse(data);
        } catch (e) {
            return callback(e);
        }
        callback();
    });
}, err => {
    if (err) console.error(err.message);
    // configs is now a map of JSON data
    doSomethingWith(configs);
});
```

```javascript
var async = require("async");

// ...or ES2017 async functions
async.mapLimit(urls, 5, async function(url) {
    const response = await fetch(url)
    return response.body
}, (err, results) => {
    if (err) throw err
    // results is now an array of the response bodies
    console.log(results)
})
```

Auto-commit on 2025-02-19 09:53:48 | rand=55860

Auto-commit on 2025-02-19 10:06:39 | rand=61998

Auto-commit on 2025-02-19 10:19:39 | rand=22760

Auto-commit on 2025-02-19 10:32:28 | rand=2472

Auto-commit on 2025-02-19 10:45:20 | rand=7877

Auto-commit on 2025-02-19 10:58:17 | rand=46967

Auto-commit on 2025-02-19 11:11:10 | rand=3936

Auto-commit on 2025-02-19 11:24:08 | rand=95937

Auto-commit on 2025-02-19 18:35:29 | rand=16857

Auto-commit on 2025-02-19 18:48:28 | rand=18008

Auto-commit on 2025-02-19 19:01:25 | rand=57262

Auto-commit on 2025-02-19 19:14:17 | rand=18871

Auto-commit on 2025-02-19 19:27:12 | rand=18450

Auto-commit on 2025-02-19 19:40:06 | rand=74753

Auto-commit on 2025-02-19 19:52:58 | rand=74703

Auto-commit on 2025-02-19 20:05:58 | rand=81211

Auto-commit on 2025-02-19 20:18:49 | rand=30435

Auto-commit on 2025-02-19 20:31:49 | rand=68007

Auto-commit on 2025-02-19 20:44:42 | rand=91298

Auto-commit on 2025-02-19 20:57:38 | rand=11208

Auto-commit on 2025-02-19 21:10:37 | rand=70620

Auto-commit on 2025-02-19 21:23:31 | rand=94346

Auto-commit on 2025-02-19 21:36:29 | rand=48763

Auto-commit on 2025-02-20 09:41:46 | rand=21605

Auto-commit on 2025-02-20 14:17:34 | rand=84054

Auto-commit on 2025-02-20 14:29:40 | rand=1006

Auto-commit on 2025-02-20 14:41:49 | rand=54507

Auto-commit on 2025-02-20 14:53:49 | rand=84147

Auto-commit on 2025-02-20 15:05:46 | rand=92572

Auto-commit on 2025-02-20 15:17:54 | rand=51196

Auto-commit on 2025-02-20 15:29:54 | rand=5591

Auto-commit on 2025-02-20 15:42:00 | rand=99979

Auto-commit on 2025-02-20 15:54:07 | rand=36152

Auto-commit on 2025-02-20 16:06:16 | rand=63709

Auto-commit on 2025-02-20 16:18:18 | rand=22348

Auto-commit on 2025-02-20 16:30:24 | rand=98172

Auto-commit on 2025-02-20 16:42:34 | rand=75264

Auto-commit on 2025-02-20 16:54:37 | rand=51237

Auto-commit on 2025-02-20 17:06:48 | rand=38558

Auto-commit on 2025-02-21 15:20:25 | rand=21404

Auto-commit on 2025-02-21 15:32:30 | rand=20989

Auto-commit on 2025-02-21 15:44:30 | rand=3495

Auto-commit on 2025-02-21 15:56:27 | rand=54560

Auto-commit on 2025-02-21 16:08:22 | rand=58389

Auto-commit on 2025-02-21 16:20:19 | rand=12436

Auto-commit on 2025-02-21 16:32:19 | rand=41478

Auto-commit on 2025-02-21 16:44:23 | rand=93220

Auto-commit on 2025-02-21 16:56:26 | rand=46408

Auto-commit on 2025-02-21 17:08:23 | rand=48717

Auto-commit on 2025-02-21 17:20:24 | rand=11737
