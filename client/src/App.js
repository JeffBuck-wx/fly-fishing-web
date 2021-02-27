import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Fly Fishing App</h1>
      
      <div className="form">
        <label>Fish Name:</label>
        <input type="text" name="fishName" />
        <label>Fish Details:</label>
        <input type="text" name="fishDetails" />
        <button>Submit</button>
      </div>
    </div>
  );
}

export default App;
