function one
    type Enum = enumeration(One);
    output Real real;
    output Integer integer;
    output Boolean boolean;
    output String string;
    output Enum enum;
algorithm
    real := 1;
    integer := 1;
    boolean := true;
    string := "1";
    enum := Enum.One;
end one;
