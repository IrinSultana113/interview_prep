# When a function wants to accept any number of keyword arguments, you can use **kwargs.
# **kwargs is stored as a dictionary by default.


def employee(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


employee(Name = "Ritu", Id = 3)

    