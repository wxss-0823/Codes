interface Person {
    name: string;
    age: number;
}

enum Day {
    Mon=1,
    Tue,
    Wed,
    Thu,
    Fri,
    Sat,
    Sun,
}

class Man implements Person {
    constructor(public name: string, public age: number) {}

    print_info() {
        console.log(`Person: ${this.name}, age: ${this.age}`);
    }
}

let man = new Man("wxss", 23);
let day: Day = Day.Fri;

man.print_info();
console.log(day);

let tuple1: [age: number, name: string] = [24, "wxss"];
let tuple2: [email: string, height: number] = ["2198993328@qq.com", 180];

let result = tuple1.concat(tuple2);
let arr: Array<any> = Array.from(tuple1);
let extended_tuple: [...typeof tuple2, ...typeof tuple1] = [...tuple2, ...tuple1];
console.log(arr, result, extended_tuple);
let bool = extended_tuple instanceof Array;
console.log("extended_tuple is a instance of array: " + bool);

let inter: Person = {name: "wxss", age: 24};
console.log(inter.age);

