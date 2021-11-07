import './App.css';
import {Header} from "./components/Header.js";
import {PostGenerator} from "./components/PostGenerator.js";
import {TopNavBar} from "./components/TopNavBar.js";
function App() {
  return (
    <div className="App">
      <Header />
      <TopNavBar />
      <PostGenerator />
    </div>
  );
};

export default App;
