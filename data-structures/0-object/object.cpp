#include <string>
#include <iostream>
using std::string;
using std::cin; 
using std::cout;

class Greeter {
    private:
        int age = 0;
    public:
        string name;
        Greeter(string name) {
            this->name = name;
        }

        void sayHello() {
            cout << "Hello " << name << "!\n";
        }

        static void sayGoodbye() {
            cout << "Goodbye!\n";
        }

        // Note: getter/setters for C++ is a topic of much debate: https://stackoverflow.com/questions/51615363/how-to-write-c-getters-and-setters
        int getAge() const {
            return age;
        }

        void setAge(int newAge) {
            age = newAge;
        }

        Greeter operator+(const Greeter& other) const {
            return Greeter(name + " & " + other.name);
        }
};


int main() {
    // Object creation
    Greeter person1Greeter("harsh");

    // Attribute access
    cout << person1Greeter.name << "\n";
    // cout << person1Greeter.age << "\n"; // Will not work because age is a private variable

    // Member function invocation
    person1Greeter.sayHello();
    person1Greeter.sayGoodbye();
    // Greeter::sayHello(); // Will not work because sayHello needs to be bound to an object
    Greeter::sayGoodbye();

    // New property
    // can't be done

    // Getter/Setter
    person1Greeter.setAge(20);
    cout << "age: " << person1Greeter.getAge() << "\n";
    
    // Operator overloading
    Greeter person2Greeter("yash");
    (person1Greeter + person2Greeter).sayHello();
}
