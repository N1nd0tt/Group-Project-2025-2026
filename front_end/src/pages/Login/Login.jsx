import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Sword } from 'lucide-react';
import Input from '../../components/Input';
import Button from '../../components/Button';
import styles from './Login.module.css';

const Login = () => {
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        // TODO: Implement actual login logic
        navigate('/');
    };

    return (
        <div className={styles.container}>
            <div className={styles.card}>
                <div className={styles.header}>
                    <div className={styles.iconWrapper}>
                        <Sword size={32} className={styles.icon} />
                    </div>
                    <h1 className={styles.title}>Welcome Back</h1>
                    <p className={styles.subtitle}>Enter the realm of adventure</p>
                </div>

                <form onSubmit={handleSubmit} className={styles.form}>
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

                    <Button type="submit" size="lg" className={styles.submitBtn}>
                        Enter Realm
                    </Button>
                </form>

                <div className={styles.footer}>
                    <p>Don't have a character yet?</p>
                    <Link to="/register" className={styles.link}>Create Account</Link>
                </div>
            </div>
        </div>
    );
};

export default Login;
