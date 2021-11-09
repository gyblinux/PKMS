import './App.css';
import { Header } from './components/Header.js';
import { TopNavBar } from './components/TopNavBar.js';
import { Footer } from './components/Footer.js';
import { Wiki } from './pages/Wiki.js';
import { Blog } from './pages/Blog.js';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <TopNavBar />

        <Routes>
          <Route path='/wiki' element={<Wiki />} />
          <Route path='/blog' element={<Blog />} />
        </Routes>

        <Footer />
      </div>
    </Router>
  );
};

export default App;
