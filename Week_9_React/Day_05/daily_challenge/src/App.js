import { useState } from "react";

function App() {
  const [num1, setNum1] = useState('');
  const [num2, setNum2] = useState('');
  const [operation, setOperation] = useState('add');
  const [result, setResult] = useState('');

  const handleNum1Change = (e) => {
    setNum1(e.target.value);
  };

  const handleNum2Change = (e) => {
    setNum2(e.target.value);
  };

  const handleOperationChange = (e) => {
    setOperation(e.target.value);
  };

  const calculateResult = () => {
    const number1 = parseFloat(num1);
    const number2 = parseFloat(num2);

    switch (operation) {
      case 'add':
        setResult(number1 + number2);
        break;
      case 'subtract':
        setResult(number1 - number2);
        break;
      case 'multiply':
        setResult(number1 * number2);
        break;
      case 'divide':
        setResult(number1 / number2);
        break;
      default:
        setResult('Invalid operation');
    }
  };

  return (
    <div>
      <h1>Calc</h1>
      <label>
        Number 1:
        <input type="number" value={num1} onChange={handleNum1Change} />
      </label>
      <br />
      <label>
        Number 2:
        <input type="number" value={num2} onChange={handleNum2Change} />
      </label>
      <br />
      <label>
        Operation:
        <select value={operation} onChange={handleOperationChange}>
          <option value="add">Addition</option>
          <option value="subtract">Subtraction</option>
          <option value="multiply">Multiplication</option>
          <option value="divide">Division</option>
        </select>
      </label>
      <br />
      <button onClick={calculateResult}>Add Them</button>
      <br />
      <p>Result: {result}</p>
    </div>
  );
};

export default App;
