
# Unreadable error

```python3
with open_session as session:
    session.getVersion("")  # Will show low-level arpeggio traceback
```

# absolute TypeName handling

`.Modelica.Math` v.s. `Modelica.Math`

```python3
>>> TypeName(".Modelica.Math").parts
(".", "Modelica", "Math")
>>> TypeName("Modelica.Math").parts
("Modelica", "Math")
```

# Use `getComponents` (not `getComponentsTest`) for bootstrap

```modelica
>>> getVersion()
"OMCompiler v1.13.0"

>>> getComponentsTest(OpenModelica.Scripting.getComponentsTest)
{}

>>> getComponents(OpenModelica.Scripting.getComponentsTest)
{{OpenModelica.$Code.TypeName,name,"", "public", false, false, false, false, "unspecified", "none", "input",{}},{OpenModelica.Scripting.getComponentsTest.Component,components,"", "public", false, false, false, false, "unspecified", "none", "output",{:}}}

>>> getComponentsTest(OpenModelica.Scripting.simulate)
{}

>>> getComponents(OpenModelica.Scripting.simulate)
{{OpenModelica.$Code.TypeName,className,"the class that should simulated", "public", false, false, false, false, "unspecified", "none", "input",{}},{Real,startTime,"the start time of the simulation. <default> = 0.0", "public", false, false, false, false, "unspecified", "none", "input",{}},{Real,stopTime,"the stop time of the simulation. <default> = 1.0", "public", false, false, false, false, "unspecified", "none", "input",{}},{Real,numberOfIntervals,"number of intervals in the result file. <default> = 500", "public", false, false, false, false, "unspecified", "none", "input",{}},{Real,tolerance,"tolerance used by the integration method. <default> = 1e-6", "public", false, false, false, false, "unspecified", "none", "input",{}},{String,method,"integration method used for simulation. <default> = dassl", "public", false, false, false, false, "unspecified", "none", "input",{}},{String,fileNamePrefix,"fileNamePrefix. <default> = \"\"", "public", false, false, false, false, "unspecified", "none", "input",{}},{String,options,"options. <default> = \"\"", "public", false, false, false, false, "unspecified", "none", "input",{}},{String,outputFormat,"Format for the result file. <default> = \"mat\"", "public", false, false, false, false, "unspecified", "none", "input",{}},{String,variableFilter,"Filter for variables that should store in result file. <default> = \".*\"", "public", false, false, false, false, "unspecified", "none", "input",{}},{String,cflags,"cflags. <default> = \"\"", "public", false, false, false, false, "unspecified", "none", "input",{}},{String,simflags,"simflags. <default> = \"\"", "public", false, false, false, false, "unspecified", "none", "input",{}},{OpenModelica.Scripting.simulate.SimulationResult,simulationResults,"", "public", false, false, false, false, "unspecified", "none", "output",{}}}

>>>
```

# `omc4py.session.bootstrap.profile.abc.AbstractProfile`

Is it needed to change AbstractProfile.find_element from static-method to method?