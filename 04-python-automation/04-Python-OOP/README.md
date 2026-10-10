# Python Object-Oriented Programming (OOP)

A deep-dive into Python's Object-Oriented Programming paradigms, covering classes, constructors, encapsulation, aggregation, inheritance, polymorphism, and magic methods—with direct practical applications to DevOps infrastructure modeling.

## About This Course

- **Course:** Object-Oriented Programming in Python (Full Deep-Dive)
- **Focus:** Complete OOP architecture: classes, objects, `self`, constructors (`__init__`), encapsulation, pass-by-reference semantics, class vs. instance attributes, `@staticmethod`, aggregation ("has-a"), inheritance ("is-a"), polymorphism, the `super()` keyword, and method/operator overloading.
- **Why It Is Useful:** In DevOps and Infrastructure as Code (IaC), infrastructure components are rarely simple strings. They are complex entities with state and behavior (e.g., a `Server` has an IP, status, and actions like `start()`, `stop()`, or `deploy()`). Understanding OOP enables writing structured tools, custom CLI commands, and SDK abstractions.
- **Where It Fits in the DevOps Journey:** Step 04 in the learning path. Having previously understood basic procedural Python scripts, this course introduces the software engineering principles required to design scalable automation tools.

## Topics Covered

| Status | Topic | Details |
|---|---|---|
| ✅ | Classes & Objects | Defining classes, instantiating objects, instance state |
| ✅ | Constructor & `self` | `__init__` initialization, understanding the `self` instance reference |
| ✅ | Practical Infrastructure Modeling | Building `Server`, `CloudServer`, and `Deployment` classes |
| ✅ | Objects in Collections | Managing lists and dictionaries of object instances |
| ✅ | Encapsulation & Data Hiding | Private variables (`__pin`, `__balance`), getters and setters |
| ✅ | Memory & Pass by Reference | How Python passes object references and mutates shared state |
| ✅ | Static Variables & Methods | Class-level variables, `@staticmethod` for utility functions (e.g., IP validation) |
| ✅ | Class Aggregation ("Has-A") | Combining objects: `Deployment` has a `Server`, `Customer` has an `Address` |
| ✅ | Inheritance ("Is-A") | Single, Multilevel, Hierarchical, Multiple, and Hybrid inheritance patterns |
| ✅ | The `super()` Keyword | Calling parent constructors and parent methods from derived subclasses |
| ✅ | Polymorphism & Method Overriding | Uniform interfaces across different classes, overriding parent behavior |
| ✅ | Method Overloading Simulation | Achieving flexible parameter handling via default args and `*args` |
| ✅ | Operator Overloading | Implementing magic/dunder methods (`__str__`, `__add__`, `__gt__`) |

## Practical Examples

| Script / Exercise | Purpose | Python Concept | Why It Is Useful |
|---|---|---|---|
| [02_atm_class.py](Day-01/02_atm_class.py) | Interactive ATM with PIN creation, deposit, withdraw | Class definition, methods, instance state | Foundation of object state mutation and interaction |
| [02_server_class.py](Day-02/02_server_class.py) | Models a server with name, IP, and lifecycle actions | Classes, `__init__`, methods (`start`, `stop`) | Directly models physical or virtual servers in code |
| [05_devops_serverPractice.py](Day-02/05_devops_serverPractice.py) | Manages Linux/Windows servers with service deployment | Class methods, conditionals, status tracking | Practical DevOps server inventory management tool |
| [fraction.py](Day-03/01_fraction_based_classed/fraction.py) | Custom math data type with dunder methods | Magic methods (`__str__`, `__add__`, `__truediv__`) | Understanding how Python objects behave natively |
| [01_atm_class.py (Encapsulation)](Day-03/02_encapsulation/01_atm_class.py) | Protects sensitive PIN and balance variables | Private attributes (`__pin`), getter/setter | Secure data handling preventing unintended tampering |
| [05_@method_check_ip_method.py](Day-03/04_static%20Variable%20&%20methods/05_@method_check_ip_method.py) | Validates IPv4 address string formatting | `@staticmethod`, string parsing | Utility function bundled inside a class without requiring an instance |
| [04_deployment+server.py](Day-04/01_Class%20relationship%20-%20Aggregation/04_deployment+server.py) | Associates a deployment object with a target server | Class Aggregation ("Has-A" relationship) | Modeling CI/CD pipelines deploying to specific host nodes |
| [03_server_webserver.py](Day-04/02_Inheritance/03_server_webserver.py) | `WebServer` inherits from base `Server` class | Inheritance ("Is-A" relationship) | Reusing base server capabilities for specialized server roles |
| [03_devops_example.py (Super)](Day-04/04_Super_keyword/03_devops_example.py) | `CloudServer` extends `Server` with provider and instance type | `super().__init__()`, method extension | Modeling AWS/GCP/Azure compute instances cleanly |
| [01_method_overloading.py](Day-05/01_method_overloading/01_method_overloading.py) | Flexible method signatures | Default arguments, `*args` | Writing adaptable functions that take variable inputs |
| [01_+operator.py](Day-05/02_operator_overloading/01_+operator.py) | Overloads `+` operator to combine custom objects | `__add__` dunder method | Elegant object arithmetic and aggregation |

## Python Concepts Learned

- **State vs. Behavior:** Classes encapsulate data attributes (state) and functions (behavior) into a single entity.
- **`self` Reference:** Explicit instance reference that points to the specific object currently executing a method.
- **Access Control & Name Mangling:** Prefixing variables with `__` (double underscore) activates Python's name mangling to protect internal state.
- **Aggregation vs. Inheritance:**
  - *Aggregation:* When an object *has* another object (e.g., a `Deployment` *has* a `Server`).
  - *Inheritance:* When a class *is a specialized version* of another class (e.g., a `WebServer` *is a* `Server`).
- **`super()` Mechanism:** Enables a child class to call parent constructors and methods, preventing duplicate initialization code.
- **Dunder / Magic Methods:** Special methods prefixed and suffixed with double underscores (e.g., `__init__`, `__str__`, `__add__`) that hook into Python's native syntax.

## DevOps Relevance

- **Infrastructure Modeling:** Tools like Terraform and Pulumi treat servers, VPCs, and firewalls as resource objects. Learning OOP provides the conceptual foundation for understanding how modern cloud infrastructure is structured programmatically.
- **Extensible Automation Frameworks:** By creating a base `Server` class, teams can create specialized subclasses like `DatabaseServer`, `WebServer`, or `KubernetesWorker` that inherit common SSH, monitoring, and backup methods while customizing specific behaviors.
- **Clean CLI & SDK Development:** When building custom internal CLI utilities for a DevOps team, classes keep configuration, API authentication, and execution state organized cleanly.

## Learning Notes

- Python does not support classic method overloading (declaring the same function name multiple times with different parameter types). The last defined method overwrites previous definitions. Python achieves overloading via default arguments (`arg=None`) or variable-length arguments (`*args`, `**kwargs`).
- Unlike Java or C++, Python does not have strict `private` keywords. Variables prefixed with `__` undergo name mangling (`_ClassName__attribute`), which provides protection against accidental overwrites rather than absolute security.
- Pass-by-object-reference: Modifying a mutable object (like a list or dictionary) inside a method modifies the original object outside the method as well.

## Projects / Exercises

### Day 01 — Classes & ATM Simulation
- [01_class.py](Day-01/01_class.py)
- [02_atm_class.py](Day-01/02_atm_class.py)
- [03_atm_practice_01.py](Day-01/03_atm_practice_01.py)

### Day 02 — Server Modeling, Constructors & DevOps Practice
- [01_atm_class.py](Day-02/01_atm_class.py)
- [02_server_class.py](Day-02/02_server_class.py)
- [03_self_&_contructor.py](Day-02/03_self_&_contructor.py)
- [04_self+init.py](Day-02/04_self+init.py)
- [05_devops_serverPractice.py](Day-02/05_devops_serverPractice.py)

### Day 03 — Encapsulation, Reference Semantics & Static Methods
- [01_collection_in_objects.py](Day-03/01_collection_in_objects.py)
- **Fraction Class:** [fraction.py](Day-03/01_fraction_based_classed/fraction.py) & [02_called_fraction.py](Day-03/01_fraction_based_classed/02_called_fraction.py)
- **Encapsulation:** [01_atm_class.py](Day-03/02_encapsulation/01_atm_class.py) & [02_bank_account.py](Day-03/02_encapsulation/02_bank_account.py)
- **Pass By Reference:** [01_pass_by_ref.py](Day-03/03_passByRefrence/01_pass_by_ref.py), [02_list_psss.py](Day-03/03_passByRefrence/02_list_psss.py), [03_dic_pass.py](Day-03/03_passByRefrence/03_dic_pass.py), [04_object_example.py](Day-03/03_passByRefrence/04_object_example.py)
- **Static Variables & Methods:** [01_static_bank_name.py](Day-03/04_static%20Variable%20&%20methods/01_static_bank_name.py), [02_count_objects.py](Day-03/04_static%20Variable%20&%20methods/02_count_objects.py), [05_@method_check_ip_method.py](Day-03/04_static%20Variable%20&%20methods/05_@method_check_ip_method.py), [06_@method_devops-calculation.py](Day-03/04_static%20Variable%20&%20methods/06_@method_devops-calculation.py)

### Day 04 — Aggregation, Inheritance, Polymorphism & Super
- **Aggregation:** [01_class_aggregation.py](Day-04/01_Class%20relationship%20-%20Aggregation/01_class_aggregation.py), [04_deployment+server.py](Day-04/01_Class%20relationship%20-%20Aggregation/04_deployment+server.py)
- **Inheritance:** [01_user_reg.py](Day-04/02_Inheritance/01_user_reg.py), [03_server_webserver.py](Day-04/02_Inheritance/03_server_webserver.py)
- **Inheritance Types:** [01-single.py](Day-04/02_Inheritance/Types_of_inheritance/01-single.py), [02-multilevel.py](Day-04/02_Inheritance/Types_of_inheritance/02-multilevel.py), [04_multiple.py](Day-04/02_Inheritance/Types_of_inheritance/04_multiple.py)
- **Polymorphism:** [01_sameMethod_diff_classes.py](Day-04/03_Polymorphism/01_sameMethod_diff_classes.py), [03_adv_poly.py](Day-04/03_Polymorphism/03_adv_poly.py)
- **Super Keyword:** [01_super_with_constructor.py](Day-04/04_Super_keyword/01_super_with_constructor.py), [03_devops_example.py](Day-04/04_Super_keyword/03_devops_example.py)

### Day 05 — Method & Operator Overloading
- **Method Overloading:** [01_method_overloading.py](Day-05/01_method_overloading/01_method_overloading.py), [02_args.py](Day-05/01_method_overloading/02_args.py)
- **Operator Overloading:** [01_+operator.py](Day-05/02_operator_overloading/01_+operator.py), [02_operator_greater.py](Day-05/02_operator_overloading/02_operator_greater.py)

## What I Learned

Deepened understanding of Object-Oriented design in Python. Learned how constructors initialize state, how inheritance and aggregation allow code reuse, and how to represent real-world DevOps resources (servers, deployments, cloud instances) as maintainable Python classes.

## Next Step

Explore [05-Python-for-DevOps-Abhishek](../05-Python-for-DevOps-Abhishek/README.md) for real-world enterprise DevOps scenarios, log analysis, and advanced exception handling workflows.
