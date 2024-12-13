
document.addEventListener("DOMContentLoaded", () => {
    const initialGrid = createGrid("initial-state");
    const goalGrid = createGrid("goal-state");

    document.getElementById("solve-button").addEventListener("click", () => {
        const initial = getGridValues(initialGrid);
        const goal = getGridValues(goalGrid);

        if (!validateState(initial) || !validateState(goal)) {
            alert("Please enter valid states (0-8, no duplicates).");
            return;
        }

        const solution = solvePuzzle(initial, goal);
        displaySolution(solution);
    });

    function createGrid(id) {
        const container = document.getElementById(id);
        const inputs = [];
        for (let i = 0; i < 9; i++) {
            const input = document.createElement("input");
            input.type = "number";
            input.min = 0;
            input.max = 8;
            container.appendChild(input);
            inputs.push(input);
        }
        return inputs;
    }

    function getGridValues(grid) {
        return grid.map(input => parseInt(input.value || "0"));
    }

    function validateState(state) {
        const unique = new Set(state);
        return state.length === 9 && unique.size === 9 && Math.min(...state) === 0 && Math.max(...state) === 8;
    }

    function solvePuzzle(initial, goal) {
        // Implement the A* algorithm (similar to the Python version)
        // This is a placeholder for now.
        return ["Example Step 1", "Example Step 2"];
    }

    function displaySolution(steps) {
        const container = document.getElementById("solution-steps");
        container.innerHTML = "";
        steps.forEach((step, index) => {
            const stepDiv = document.createElement("div");
            stepDiv.textContent = `Step ${index + 1}: ${step}`;
            container.appendChild(stepDiv);
        });
    }
});
