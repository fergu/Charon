# Charon
 Reactive python notebook, inspired by Pluto.jl

 This project is very much in its early stages and doesn't do much of anything yet. It is inspired by the reactive notebook design of Pluto, hence this project's name as a moon of Pluto :)

 This project aims to have a very simple, lightweight, reactive notebook similar to Pluto.jl's functionality. Major goals are:

 1) The user should be able to drag/drop/reorder code cells in whatever order makes sense to them, and the notebook should still execute correctly.

 2) The state of the notebook should be completely described by the notebook itself. That is, no hidden variables or unexpected behavior from saved kernel states.

 3) The resulting notebook file should be valid Python code. Ideally the notebook should be structured such that the file can be passed directly to a python interpreter, without Charon, and run without modification.

This is very much an ongoing project, and is being worked on during the random spots of free time and energy I have during my Ph.D :) As such, progress may be quite slow, but if you would like to contribute, please feel free to open an issue to discuss what change you'd like to add!
