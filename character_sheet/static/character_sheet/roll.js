        function roll(sides, mod) {
            let sign = "";
            if (mod >= 0) {
                sign = "+"
            }
            let result = Math.floor((Math.random() * sides) + 1);
            result_output = `You roll ${result} with a modifier of ${sign}${mod} for a total of ${result + mod}`;
            alert(result_output);
        }