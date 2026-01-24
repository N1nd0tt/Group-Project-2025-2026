import React, { useState } from 'react';
import { Play, Settings, Sparkles } from 'lucide-react';
import Button from '../../components/Button';
import Input from '../../components/Input';
import styles from './NewGame.module.css';

const NewGame = () => {
    const [gameTitle, setGameTitle] = useState('');

    const handleStart = (e) => {
        e.preventDefault();
        // TODO: Initialize game session and redirect to chat
        alert("The adventure begins... (Chat coming soon)");
    };

    return (
        <div className={styles.container}>
            <div className={styles.content}>
                <div className={styles.iconWrapper}>
                    <Sparkles size={48} className={styles.icon} />
                </div>

                <h1 className={styles.title}>New Adventure</h1>
                <p className={styles.subtitle}>Prepare your party and enter the unknown</p>

                <form onSubmit={handleStart} className={styles.form}>
                    <Input
                        label="Adventure Name"
                        placeholder="The Tomb of Horrors"
                        value={gameTitle}
                        onChange={(e) => setGameTitle(e.target.value)}
                        required
                    />

                    <div className={styles.settingsGroup}>
                        <div className={styles.settingItem}>
                            <Settings size={20} className={styles.settingIcon} />
                            <span>Advanced Settings</span>
                        </div>
                        {/* Placeholder for settings controls */}
                    </div>

                    <Button type="submit" size="lg" className={styles.startBtn}>
                        <Play size={20} />
                        Launch Session
                    </Button>
                </form>
            </div>
        </div>
    );
};

export default NewGame;
