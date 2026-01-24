import React from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { Sword, Scroll, Users, LogOut, LayoutDashboard } from 'lucide-react';
import Button from './Button';
import './Layout.css';

const Layout = ({ children }) => {
    const navigate = useNavigate();

    // Placeholder logout
    const handleLogout = () => {
        navigate('/login');
    };

    return (
        <div className="layout-container">
            <nav className="navbar">
                <div className="nav-brand">
                    <Sword className="brand-icon" size={28} />
                    <span className="brand-text">D&D Manager</span>
                </div>

                <div className="nav-links">
                    <NavLink to="/" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
                        <LayoutDashboard size={20} />
                        <span>Dashboard</span>
                    </NavLink>

                    <NavLink to="/history" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
                        <Scroll size={20} />
                        <span>History</span>
                    </NavLink>

                    <NavLink to="/friends" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
                        <Users size={20} />
                        <span>Friends</span>
                    </NavLink>
                </div>

                <div className="nav-actions">
                    <div className="user-profile">
                        <div className="avatar">DM</div>
                        <span className="username">Dungeon Master</span>
                    </div>
                    <Button variant="ghost" size="sm" onClick={handleLogout} title="Logout">
                        <LogOut size={20} />
                    </Button>
                </div>
            </nav>

            <main className="main-content">
                {children}
            </main>
        </div>
    );
};

export default Layout;
