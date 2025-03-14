import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import RegisterPanel from './components/Register/Register';
import Dealers from './components/Dealers/Dealers';
import Dealer from "./components/Dealers/Dealer";

function App() {
  return (
    <Router>  {/* ✅ Wrap everything in Router */}
      <Routes>
        <Route path="/login" element={<LoginPanel />} />
        <Route path="/register" element={<RegisterPanel />} />
        <Route path="/dealers" element={<Dealers />} />
        <Route path="/dealer/:id" element={<Dealer />} />
      </Routes>
    </Router>
  );
}

export default App;
