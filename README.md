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

Auto-commit on 2025-02-21 17:32:25 | rand=24692

Auto-commit on 2025-02-21 17:44:22 | rand=86862

Auto-commit on 2025-02-21 17:56:22 | rand=67978

Auto-commit on 2025-02-21 18:08:21 | rand=19691

Auto-commit on 2025-02-22 00:26:38 | rand=95659

Auto-commit on 2025-02-22 00:38:47 | rand=55020

Auto-commit on 2025-02-22 00:50:48 | rand=66345

Auto-commit on 2025-02-22 01:02:51 | rand=34807

Auto-commit on 2025-02-22 01:14:53 | rand=42163

Auto-commit on 2025-02-22 01:27:00 | rand=38862

Auto-commit on 2025-02-22 01:38:59 | rand=90329

Auto-commit on 2025-02-22 01:51:05 | rand=29331

Auto-commit on 2025-02-22 02:03:04 | rand=11046

Auto-commit on 2025-02-22 02:15:12 | rand=77218

Auto-commit on 2025-02-22 02:27:20 | rand=58869

Auto-commit on 2025-02-22 02:39:28 | rand=68619

Auto-commit on 2025-02-22 02:51:32 | rand=46206

Auto-commit on 2025-02-22 03:03:43 | rand=95961

Auto-commit on 2025-02-22 03:15:54 | rand=48592

Auto-commit on 2025-02-22 14:55:48 | rand=89742

Auto-commit on 2025-02-22 15:07:54 | rand=84959

Auto-commit on 2025-02-22 15:19:58 | rand=37202

Auto-commit on 2025-02-22 15:32:05 | rand=40771

Auto-commit on 2025-02-22 15:44:04 | rand=21019

Auto-commit on 2025-02-22 15:56:11 | rand=80061

Auto-commit on 2025-02-22 16:08:16 | rand=88128

Auto-commit on 2025-02-22 16:20:15 | rand=69501

Auto-commit on 2025-02-22 16:32:16 | rand=25947

Auto-commit on 2025-02-22 16:44:17 | rand=64953

Auto-commit on 2025-02-22 16:56:21 | rand=39720

Auto-commit on 2025-02-22 17:08:20 | rand=32794

Auto-commit on 2025-02-22 17:20:31 | rand=68187

Auto-commit on 2025-02-22 17:32:31 | rand=51659

Auto-commit on 2025-02-22 17:44:36 | rand=47910

Auto-commit on 2025-02-24 13:59:24 | rand=96225

Auto-commit on 2025-02-24 14:11:26 | rand=71384

Auto-commit on 2025-02-24 14:23:26 | rand=49140

Auto-commit on 2025-02-24 14:35:33 | rand=28815

Auto-commit on 2025-02-24 14:47:41 | rand=75680

Auto-commit on 2025-02-24 14:59:41 | rand=25157

Auto-commit on 2025-02-24 15:11:48 | rand=35285

Auto-commit on 2025-02-24 15:23:51 | rand=86979

Auto-commit on 2025-02-24 15:36:00 | rand=70563

Auto-commit on 2025-02-24 15:48:10 | rand=75216

Auto-commit on 2025-02-24 16:00:19 | rand=57419

Auto-commit on 2025-02-24 16:12:19 | rand=91215

Auto-commit on 2025-02-24 16:24:15 | rand=43252

Auto-commit on 2025-02-24 16:36:23 | rand=67965

Auto-commit on 2025-02-24 16:48:27 | rand=6882

Auto-commit on 2025-02-24 18:00:41 | rand=83140

Auto-commit on 2025-02-24 18:12:41 | rand=14239

Auto-commit on 2025-02-24 18:24:46 | rand=63548

Auto-commit on 2025-02-24 18:36:53 | rand=66581

Auto-commit on 2025-02-24 18:48:58 | rand=83082

Auto-commit on 2025-02-24 19:01:02 | rand=46076

Auto-commit on 2025-02-24 19:13:13 | rand=16204

Auto-commit on 2025-02-24 19:25:18 | rand=16898

Auto-commit on 2025-02-24 19:37:16 | rand=11706

Auto-commit on 2025-02-24 19:49:18 | rand=64579

Auto-commit on 2025-02-24 20:01:22 | rand=1364

Auto-commit on 2025-02-24 20:13:27 | rand=16228

Auto-commit on 2025-02-24 20:25:32 | rand=44918

Auto-commit on 2025-02-24 20:37:35 | rand=34459

Auto-commit on 2025-02-24 20:49:35 | rand=98099

Auto-commit on 2025-02-25 12:23:18 | rand=8883

Auto-commit on 2025-02-25 12:35:18 | rand=13917

Auto-commit on 2025-02-25 12:47:26 | rand=36681

Auto-commit on 2025-02-25 12:59:27 | rand=30800

Auto-commit on 2025-02-25 13:11:29 | rand=43485

Auto-commit on 2025-02-25 13:23:37 | rand=90558

Auto-commit on 2025-02-25 13:35:44 | rand=33949

Auto-commit on 2025-02-25 13:47:43 | rand=71535

Auto-commit on 2025-02-25 13:59:47 | rand=77973

Auto-commit on 2025-02-25 14:11:48 | rand=92042

Auto-commit on 2025-02-25 14:23:54 | rand=80183

Auto-commit on 2025-02-25 14:35:57 | rand=75063
