import time
import sys
from typing import Callable, Any, Dict
import random




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

    def my_decorator(self, func: Callable[..., Dict[str, Any]]) -> Callable[..., Any]:
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
            print(f'Function Name(args_number)    : {func.__name__}({num_of_arguments})')
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
            print(f'Execution Time   : {execution_time:.8f} seconds')
            print("-" * 50)
            

            return result
        return wrapper



dec = FunctionInfo()

@dec.my_decorator
def func_exp():
    print('Hello World')

func_exp()
    



