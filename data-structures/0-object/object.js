const person1 = {
    name: 'harsh'
}

const greetArrow = () => {
    console.log(`Hello ${this.name}`);
}

function greetFull() {
    console.log(`Hello ${this.name}`);
}

const greetArrowPerson1 = greetArrow.bind(person1);
const greetFullPerson1 = greetFull.bind(person1);

// Property access
console.log(`name: ${person1.name}`);

// "this" in bound and unbound contexts
greetArrow(); // Unbound functions point to the global context
greetArrowPerson1(); // Arrow functions generally cannot be bound to an object
greetFullPerson1();
console.log("---");


class Greeter {
    #ageMirror = undefined; // private variable
    constructor(name) {
        this.name = name;
    }
    
    sayHello() {
        console.log(`Hello ${this.name}!`);
    }

    static sayGoodbye(){
        console.log(`Goodbye!`);
    }
    
    set alt(val) {
        console.log(`Alt was attempted to be set! (but will not be set)`);
    }
    
    set age(value) {
        console.log(`age was "set"!`);
        this.#ageMirror = value; // private variable not necessary, alt: this._ageMirror = value;
    }
    
    get age() {
        console.log(`age was accessed!`);
        return this.#ageMirror;
    }
}

// Object creation
const person2Greeter = new Greeter('yash');

// Property access
console.log(`name: ${person2Greeter.name}`);
// console.log(person2Greeter.#ageMirror) // Will not work because ageMirror is a private member

// Member function invocation
person2Greeter.sayHello();
Greeter.sayGoodbye();
// Greeter.sayHello(); // Will not work sayHello is not a property of the class
// person2Greeter.sayGoodbye(); // Will not work because sayGoodbye is not a property of the object

// New property
person2Greeter.alt = 10
console.log(`alt: ${person2Greeter.alt}`);
delete person2Greeter.alt
console.log(`alt: ${person2Greeter.alt}`);

// Getter/Setter
person2Greeter.age = 20
console.log(`age: ${person2Greeter.age}`);

// Operator overloading
// Can't be done


console.log("---");
