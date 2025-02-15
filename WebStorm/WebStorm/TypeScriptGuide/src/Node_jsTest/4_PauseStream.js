const fs = require('fs');

const readableStream = fs.createReadStream('1_input.txt', 'utf8');

readableStream.on('data', (chunk) => {
    console.log('Received chunk: ', chunk);
    readableStream.pause();
    setTimeout(() => {
        readableStream.resume();
    }, 1000);
    readableStream.destroy();
});
