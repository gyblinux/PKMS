import './App.css';
import {Header} from "./components/Header.js"
import {PostGenerator} from "./components/PostGenerator.js"
function App() {
  return (
    <div className="App">
      <Header />
      <PostGenerator />
    </div>
  );
}

export default App;
