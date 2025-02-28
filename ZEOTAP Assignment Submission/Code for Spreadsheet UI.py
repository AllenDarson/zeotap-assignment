#Code for Spreadsheet UI (React)
import React, { useState } from "react";

const Spreadsheet = () => {
  const [data, setData] = useState([
    ["", "A", "B", "C"],
    ["1", "", "", ""],
    ["2", "", "", ""],
    ["3", "", "", ""],
  ]);

  return (
    <div>
      <h2>Basic Google Sheets Clone</h2>
      <table border="1">
        <tbody>
          {data.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((cell, colIndex) => (
                <td key={colIndex} contentEditable={rowIndex !== 0}>
                  {cell}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Spreadsheet;
