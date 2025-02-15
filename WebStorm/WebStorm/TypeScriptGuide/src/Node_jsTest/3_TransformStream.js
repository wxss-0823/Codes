const zlib = require('zlib');
const fs = require('fs');

// create a readable stream
const readableStream = fs.createReadStream('1_input.txt');

// create a transform stream
const gzip = zlib.createGzip();

// create a writable stream
const writableStream = fs.createWriteStream('1_output.txt.gz');

// pipe readable stream to transform stream, then to writable stream
readableStream.pipe(gzip).pipe(writableStream);

// listen event
writableStream.on('finish', () => {
    console.log('File compressed successfully.');
});
