function counter() {
    let count = 0;
    return ++count;
}

console.log(counter());
console.log(counter());

function createCounter() {
    let count = 0;
    return function() {
        count++;
        return count;
    };
}

const Counter = createCounter();
console.log(Counter());
console.log(Counter());

const Counter2 = function() {
    let count = 1;
    count++;
    return count;
};

console.log(Counter2());
console.log(Counter2());


