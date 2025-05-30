
import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">OctoFit Tracker</Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item"><Link className="nav-link" to="/users">Users</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/teams">Teams</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/activities">Activities</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/leaderboard">Leaderboard</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/workouts">Workouts</Link></li>
            </ul>
          </div>
        </div>
      </nav>
      <Routes>
        <Route path="/users" element={<Users />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/activities" element={<Activities />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/workouts" element={<Workouts />} />
        <Route path="/" element={
          <div className="container mt-4">
            <div className="card">
              <div className="card-header bg-dark text-white">
                <h2 className="mb-0">Welcome to OctoFit Tracker!</h2>
              </div>
              <div className="card-body">
                <p className="lead">Track your fitness, join teams, and compete on the leaderboard!</p>
                <Link to="/users" className="btn btn-primary m-2">View Users</Link>
                <Link to="/teams" className="btn btn-info m-2">View Teams</Link>
                <Link to="/activities" className="btn btn-primary m-2">View Activities</Link>
                <Link to="/leaderboard" className="btn btn-success m-2">View Leaderboard</Link>
                <Link to="/workouts" className="btn btn-warning m-2">View Workouts</Link>
              </div>
            </div>
          </div>
        } />
      </Routes>
    </Router>
  );
}

export default App;
