/* globals PDFJS */

'use strict';

// Simply resolve the promise, signaling all the assets are loaded.
// Used since the assets are all included in coffice bundle
PDFJS.fakeWorkerFilesLoadedCapability.resolve();