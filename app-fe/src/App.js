import './App.css';
import { Header } from './components/header/Header.js';
import { Footer } from './components/footer/Footer.js';
import { TopNavBar } from './components/topnavbar/TopNavBar.js';
import { Wiki } from './pages/Wiki.js';
import { Blog } from './pages/Blog.js';
import { LoginForm } from './pages/LoginForm';
import { Routes, Route} from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Header />
      <TopNavBar />

      <Routes>
        <Route path='/wiki/*' element={<Wiki />} />
        <Route path='/blog' element={<Blog />} />
        <Route path='/login' element={<LoginForm />}/>
      </Routes>

      <Footer />
    </div>
  );
};

export default App;
