const board = document.getElementById('board');
const cells = Array.from(document.getElementsByClassName('cell'));
const resetButton = document.getElementById('reset');
const message = document.getElementById('message');

let boardState = Array(9).fill(null);
let currentPlayer = 'X'; // Player starts with 'X'
let gameOver = false;

                  // Event listener for cell clicks
board.addEventListener('click', (event) => {
    if (gameOver) return;
    const cell = event.target;

    if (cell.classList.contains('cell') && !cell.textContent && currentPlayer === 'X') {
        makeMove(parseInt(cell.dataset.index), 'X');
        if (!gameOver) {
            currentPlayer = 'O';
            setTimeout(makeAIMove, 100); // Small delay to let the player see their move
        }
    }
});

                   // Event listener for reset button
resetButton.addEventListener('click', resetGame);

function makeMove(index, player) {
    if (boardState[index] || gameOver) return;
    boardState[index] = player;
    cells[index].textContent = player;

    if (checkWinner(player)) {
        message.textContent = `${player} wins!`;
        gameOver = true;
    } else if (!boardState.includes(null)) {
        message.textContent = "It's a draw!";
        gameOver = true;
    }
}

function makeAIMove() {
    const bestMove = findBestMove();
    if (bestMove !== null) {
        makeMove(bestMove, 'O');
        currentPlayer = 'X';
    }
}

function findBestMove() {
    let bestVal = -Infinity;
    let bestMove = null;

    for (let i = 0; i < 9; i++) {
        if (!boardState[i]) {
            boardState[i] = 'O';
            let moveVal = minimax(boardState, false);
            boardState[i] = null;

            if (moveVal > bestVal) {
                bestMove = i;
                bestVal = moveVal;
            }
        }
    }

    return bestMove;
}

function minimax(boardState, isMaximizing) {
    let score = evaluate(boardState);

    if (score === 10) return score;
    if (score === -10) return score;
    if (!boardState.includes(null)) return 0;

    if (isMaximizing) {
        let best = -Infinity;
        for (let i = 0; i < 9; i++) {
            if (!boardState[i]) {
                boardState[i] = 'O';
                best = Math.max(best, minimax(boardState, false));
                boardState[i] = null;
            }
        }
        return best;
    } else {
        let best = Infinity;
        for (let i = 0; i < 9; i++) {
            if (!boardState[i]) {
                boardState[i] = 'X';
                best = Math.min(best, minimax(boardState, true));
                boardState[i] = null;
            }
        }
        return best;
    }
}

function evaluate(boardState) {
    const winningCombinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    for (const [a, b, c] of winningCombinations) {
        if (boardState[a] && boardState[a] === boardState[b] && boardState[a] === boardState[c]) {
            return boardState[a] === 'O' ? 10 : -10;
        }
    }

    return 0;
}

function checkWinner(player) {
    return evaluate(boardState) === (player === 'O' ? 10 : -10);
}

function resetGame() {
    boardState.fill(null);
    cells.forEach(cell => cell.textContent = '');
    message.textContent = '';
    currentPlayer = 'X'; // Player starts with 'X'
    gameOver = false;
}
