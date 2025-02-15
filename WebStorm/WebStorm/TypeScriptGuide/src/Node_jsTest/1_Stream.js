let fs = require('fs');
let data = '';

// create readable stream
let readerStream = fs.createReadStream('1_input.txt');

// set encoding utf-8
readerStream.setEncoding('utf8');

// process stream event --> data, end, error
readerStream.on('data', function(chunk) {
    data += chunk;
});

readerStream.on('end', function() {
    console.log(data);
});

readerStream.on('error', function(err) {
    console.log(err.stack);
});

console.log("Program is done.");
