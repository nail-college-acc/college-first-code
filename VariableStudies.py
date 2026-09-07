from typing import Any

"""
Text type variable
"""
name : str = "Nail"


"""
Number type Variables
"""
age : int = 18
astigmatism : float = 0.75 #float


"""
Boolean type Variables
"""
married : bool = False
needsGlasses : bool = True


"""
Array and List variables
"""
#List contains can contain more than 1 data types and in other languages, it's a lot more dynamic than array
randomList : list[int | str | bool] = ["Kaka", 11, True]

#While arrays stick with 1 data type and has a set index count
friends : list[str] = ["Kaka", "Dzaky", "Farras"]


"""
Dictionaries
"""
yeah : dict[str, Any] = {
    "address" : "Lapangan Bola str, no.12, Srengseng, Kembangan, West Jakarta",
    "education" : [
        {
            "school" : "Raden Umar Said Kudus",
            "joinDate" : "Jul 2023",
            "gradDate" : "Jul 2026"
        },
        {
            "school" : "Diponegoro University",
            "joinDate" : "August 2026",
            "gradDate" : "Some time in 2030"
        }
    ],
    "petCount" : 0
}

print(yeah["education"])