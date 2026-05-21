import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Scroll } from 'lucide-react';
import Input from '../../components/Input';
import Button from '../../components/Button';
import styles from './Register.module.css';

const Register = () => {
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        // TODO: Implement actual registration logic
        navigate('/');
    };

    return (
        <div className={styles.container}>
            <div className={styles.card}>
                <div className={styles.header}>
                    <div className={styles.iconWrapper}>
                        <Scroll size={32} className={styles.icon} />
                    </div>
                    <h1 className={styles.title}>Join the Party</h1>
                    <p className={styles.subtitle}>Begin your legend today</p>
                </div>

                <form onSubmit={handleSubmit} className={styles.form}>
                    <Input
                        label="Adventurer Name"
                        type="text"
                        placeholder="Gandalf the Grey"
                        required
                        autoFocus
                    />
                    <Input
                        label="Email"
                        type="email"
                        placeholder="wizard@example.com"
                        required
                    />
                    <Input
                        label="Password"
                        type="password"
                        placeholder="••••••••"
                        required
                    />
                    <Input
                        label="Confirm Password"
                        type="password"
                        placeholder="••••••••"
                        required
                    />

                    <Button type="submit" size="lg" className={styles.submitBtn}>
                        Create Character
                    </Button>
                </form>

                <div className={styles.footer}>
                    <p>Already have an account?</p>
                    <Link to="/login" className={styles.link}>Login</Link>
                </div>
            </div>
        </div>
    );
};

export default Register;
