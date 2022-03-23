# What is a Python main function and why do I care?

If you have followed [this guide](project-structure-and-packaging.md) to create the recommended package structure, you will now have multiple ```.py``` files containing your code.
You are probably running your program by calling just one of your ```.py``` files from a command line, like this:

```python
python create_publication.py 
```
or
```python
run create_publication.py
```

If we think about what is going on here, Python is using our various ```.py``` files in two different ways:
* It runs **every** line of code in ```create_publication.py```, treating it as a **script**.
* It imports functions from the other .py files (```processing_steps.py```, ```params.py```, etc), treating them as **modules** and uses them **only** if they are required by ```create_publication.py```.

It is a common convention in Python to define a ```main``` function, which makes this distinction more explicit.
```python
def main():
  print('Hello World!')

if __name__ == '__main__':
  main()
```

This convention allows the ```create_publication.py``` file to be used in both ways: as a script like before, but now also as a module, if we ever wanted to import ```create_publication.py``` and use its functions elsewhere.

What's going on here, is that when we run ```create_publication.py```, Python gives it a special parameter called ```__name__```, and assigns it a value depending on the context. In this case the value assigned is ```__main__```. Otherwise, if ```create_publication``` was imported as a module into another script, its ```__name__``` in this context would be ```create_publication```.

# Passing arguments from the command line

It is sometimes useful to specify in the command line some arguments that we would like to be used in the program. For example we may wish to run the same code on some input data which can be different each time we run it.
```
python create_publication.py input_data__nov_2021
```
To capture the value ```input_data_nov_2021``` Python has an inbuilt list called ```sys.argv```, which we can store as a parameter that is usable within the code,

```python
def main():
  for arg in sys.argv[1:]:
    print('user parameter: ' + arg)
```

Note that we begin the index at 1, rather than 0. This is because ```sys.argv[0]``` contains the ```__name__``` parameter explained above.

<br/><br/>


## Links
* [How to use the Python ```main``` function](https://realpython.com/python-main-function/)
* [How to use ```sys.argv``` in Python](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/)
* [```argparse``` (an alternative to ```sys.argv```)](https://docs.python.org/3/howto/argparse.html)
* [RAP package template](https://nhsd-git.digital.nhs.uk/data-services/analytics-service/iuod/rap-package-template)
