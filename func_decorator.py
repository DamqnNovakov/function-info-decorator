import time
import sys
import inspect
from typing import Callable, Any, Dict

class FunctionInfo:
    def size_of_value(self, value):
        value_size = sys.getsizeof(value)
        return value_size
    
    def check_size_based_on_value_type(self, argument): 
        if isinstance(argument, list):
            size = self.size_of_value(argument)
            message = f'-> Size of list {argument} -> {size} bytes'
        elif isinstance(argument, dict):
            size = self.size_of_value(argument)
            message = f'-> Size of dict {argument} -> {size} bytes'
        elif isinstance(argument, set):
            size = self.size_of_value(argument)
            message = f'-> Size of set {argument} -> {size} bytes'
        elif isinstance(argument, tuple):
            size = self.size_of_value(argument)
            message = f'-> Size of tuple {argument} -> {size} bytes'
        elif isinstance(argument, str):
            size = self.size_of_value(argument)
            message = f'-> Size of str {argument} -> {size} bytes'
        elif isinstance(argument, int):
            size = self.size_of_value(argument)
            message = f'-> Size of int {argument} -> {size} bytes'    
        elif isinstance(argument, float):
            size = self.size_of_value(argument)
            message = f'-> Size of float {argument} -> {size} bytes'
        elif isinstance(argument, bool):
            size = self.size_of_value(argument)
            message = f'-> Size of boolean {argument} -> {size} bytes'
        else:
            size = self.size_of_value(argument)
            message = f'-> Unsapported type {argument} -> {type(argument)}: {size} bytes'

        return message

    def check_return_type(self, func):
        signiture = inspect.signature(func)
        return_type = signiture.return_annotation

        if return_type is not inspect.Signature.empty:
            return f"Return type is annotated as: {return_type}"
        else: 
            return "Return type is not annotated."
        
    def check_parameter_type(self, func):
        signiture = inspect.signature(func)
        parameters = signiture.parameters

        parameters_types = []
        for param in parameters.values():
            
            if param.annotation is not inspect.Parameter.empty:
                param_type = f'{param.name} has a set type of {param.annotation}'
                parameters_types.append(param_type) 
            else:
                parameters_types.append(f"Parameter: {param.name} has no type annotation")

        if not parameters_types:
            return 'No parameters have set type notation'
        
        return parameters_types            
                
            
    def my_decorator(self, func: Callable[..., Dict[str, Any]]) -> Callable[..., Any]:
        return_type = self.check_return_type(func)
        parameters_types = self.check_parameter_type(func)

        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time

            func_size = self.size_of_value(func)

            num_of_arguments = len(args) + len(kwargs)

            messages = []

            for arg in args:
                messages.append(self.check_size_based_on_value_type(arg))
            
            for _ , value in kwargs.items():
                messages.append(self.check_size_based_on_value_type(value))

            print("=" * 50)  # Add a separator for neatness
            print(f'Function Name(args_number): {func.__name__}({num_of_arguments})')
            print("-" * 50)
            print("Function Arguments:")
            print(f"    1. Positional arguments {len(args)} args: {args}")
            print(f"    2. Keyword arguments {len(kwargs)} kwargs: {kwargs}")
            print("=" * 50)
            print(f'Function Size    : {func_size} bytes')
            print("-" * 50)
            print("Argument Sizes:")
            print("\n".join(messages))  # Print all messages
            print("-" * 50)
            print(f'Execution Time: {execution_time:.8f} seconds')
            print("-" * 50)
            print(f"Function expects: {return_type}")
            print("=" * 50)
            print(f"Function expects parameters type:{parameters_types}")

            

            return result
        return wrapper



dec = FunctionInfo()

@dec.my_decorator
def func_exp(a, b, name):
    print('Hello World')
    print(name)
    return a + b

func_exp(3, 3.12, 'Damqn')
    



