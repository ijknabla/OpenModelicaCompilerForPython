package Nested

    function level
        output Integer level = 1;
    end level;

    package Nested

        function level
            output Integer level = 2;
        end level;

        package Nested

            function level
                output Integer level = 3;
            end level;

        end Nested;

    end Nested;

end Nested;
