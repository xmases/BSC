# BSC Path Mapper Algorithm
> For a full integration use of the algorithm we recommend [BSC Moonlight Version]()

This algorithm takes a starting point and a ending point and creates the best route via obsticles.

## Input guide BSC Main via sys
> The positions are relative to the arguments needed for execution, if more arguments need to be added the code must be modified

| **main.py** 	|    1   	|    2   	|    3   	|    4   	|  5 	|      6+      	|
|:------------:	|:------:	|:------:	|:------:	|:------:	|:--:	|:------------:	|
|  Init Cords  	| X Axis 	| Y Axis 	|        	|        	|    	|              	|
|   End Cords  	|        	|        	| X Axis 	| Y Axis 	|    	|              	|
|    Frames    	|        	|        	|        	|        	| N° 	|              	|
|   Obstacles  	|        	|        	|        	|        	|    	| Pos per Axis 	|
## Output interpretation BSC
The output of the algorithm will come in a text file default name ```cords.txt```
> Name of the output file can be changed if necessary 

The structure will be as follows: 
```python
cords = [X Cords, Y Cords, Frame N°]
```

The structure is intended to be executed in a python code for knowing the position on an exact frame, the code for the rendering of this file as an actual path can be found in the ```rendering.py``` file.

## Position Input Placement

For practical purposes the program only accepts ascending positions in a x/y (2D) scale. The rendering program is able to render backwards if desired but in order to create the render the lower point must be the starting point. Be aware of this condition while using the algorithm. 

## Basic & Semi Integration Guide
We encourage the use of the Main version for Semi-Integration purposes, all the request to the algorithm are made in the main.py file via sys.argv (System Arguments)

```bash
python3 main.py args1 args2 args3 …
```
