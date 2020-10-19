
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
