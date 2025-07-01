classdef MyClass
    properties
        Name
        Age
    end

    methods
        % Constructor
        function obj = MyClass(name, age)
            if nargin > 0
                obj.Name = name;
                obj.Age = age;
            end
        end

        % Simple method to display info
        function greet(obj)
            fprintf('Hello, my name is %s and I am %d years old.\n', obj.Name, obj.Age);
        end
    end
end