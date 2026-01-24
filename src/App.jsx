import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

import Layout from './components/Layout';
import Login from './pages/Login/Login';
import Register from './pages/Register/Register';
import Dashboard from './pages/Dashboard/Dashboard';
import GameHistory from './pages/GameHistory/GameHistory';
import Friends from './pages/Friends/Friends';
import NewGame from './pages/NewGame/NewGame';

function App() {
  return (
    <Router>
      <Routes>
        {/* Auth Routes */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Protected Routes (Placeholder wrapper) */}
        <Route path="/" element={<Layout><Dashboard /></Layout>} />
        <Route path="/history" element={<Layout><GameHistory /></Layout>} />
        <Route path="/friends" element={<Layout><Friends /></Layout>} />
        <Route path="/new-game" element={<Layout><NewGame /></Layout>} />

        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

export default App;
