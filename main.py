// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Sudoku {
    uint8[9][9] private board;

    event CellUpdated(uint8 row, uint8 col, uint8 value);

    function isValid(uint8 row, uint8 col, uint8 value) private view returns (bool) {
        // Check row
        for (uint8 c = 0; c < 9; c++) {
            if (board[row][c] == value && c != col) {
                return false;
            }
        }

        // Check column
        for (uint8 r = 0; r < 9; r++) {
            if (board[r][col] == value && r != row) {
                return false;
            }
        }

        // Check box
        uint8 boxRow = row / 3 * 3;
        uint8 boxCol = col / 3 * 3;
        for (uint8 r = boxRow; r < boxRow + 3; r++) {
            for (uint8 c = boxCol; c < boxCol + 3; c++) {
                if (board[r][c] == value && (r != row || c != col)) {
                    return false;
                }
            }
        }

        return true;
    }

    function updateCell(uint8 row, uint8 col, uint8 value) public {
        require(row <= 8 && col <= 8 && value <= 9, "Invalid input");

        require(isValid(row, col, value), "Invalid move");

        board[row][col] = value;

        emit CellUpdated(row, col, value);
    }
    function getCellValue(uint8 row, uint8 col) public view returns (uint8) {
        require(row <= 8 && col <= 8, "Invalid input");

        return board[row][col];
    }
}
