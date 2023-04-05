
```
Searching pattern for uncoupling modules in project.
```

---


**Me:**
do you know programming patterns which allows to connect two independent modules?

---

**ChatGPT:**
Yes, there are several programming patterns that can be used to connect two independent modules. Here are a few:
<li>Adapter Pattern: This pattern is used to adapt the interface of one class to match the interface of another class. It is typically used when two classes have incompatible interfaces, but need to work together. The adapter pattern creates an intermediate adapter class that translates the interface of one class into the interface of the other.</li><li>Bridge Pattern: This pattern decouples an abstraction from its implementation so that the two can vary independently. It is often used when there are multiple implementations of a class, and you want to be able to switch between them without affecting the abstraction.</li><li>Observer Pattern: This pattern is used when one object needs to notify a set of other objects about changes in its state. It is commonly used in event-driven systems, where one object generates events and other objects need to respond to those events.</li><li>Mediator Pattern: This pattern is used to reduce coupling between multiple objects by introducing a mediator object that coordinates communication between them. The mediator object acts as a middleman between the other objects, and encapsulates the logic for how they should interact.</li><li>Facade Pattern: This pattern provides a simplified interface to a complex subsystem. It is often used to hide the complexity of a system and provide a more user-friendly interface. The facade object provides a simple interface that the client code can use to interact with the subsystem, and handles all of the complex interactions behind the scenes.</li>
