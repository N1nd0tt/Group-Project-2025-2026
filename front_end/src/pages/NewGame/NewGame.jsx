import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Play, Shield, Plus, Sparkles } from 'lucide-react';
import Button from '../../components/Button';
import { useCharacters } from '../../hooks/useCharacters';
import styles from './NewGame.module.css';

const NewGame = () => {
    const navigate = useNavigate();
    const { characters } = useCharacters();
    const [selectedChar, setSelectedChar] = useState(null);

    const handleStart = () => {
        if (!selectedChar) return;
        navigate('/game-chat', { state: { character: selectedChar } });
    };

    return (
        <div className={styles.container}>
            <div className={styles.content}>
                <div className={styles.iconWrapper}>
                    <Sparkles size={48} className={styles.icon} />
                </div>

                <h1 className={styles.title}>Choose Your Hero</h1>
                <p className={styles.subtitle}>Select a character to begin the adventure</p>

                {characters.length === 0 ? (
                    <div className={styles.emptyState}>
                        <p>You have no characters yet.</p>
                        <Button onClick={() => navigate('/create-character')} className={styles.addCharBtn}>
                            <Plus size={20} />
                            Create New Character
                        </Button>
                    </div>
                ) : (
                    <>
                        <div className={styles.characterList}>
                            {characters.map(char => (
                                <div 
                                    key={char.id} 
                                    className={`${styles.characterCard} ${selectedChar?.id === char.id ? styles.selected : ''}`}
                                    onClick={() => setSelectedChar(char)}
                                >
                                    <div className={styles.charIcon}>
                                        <Shield size={24} />
                                    </div>
                                    <div className={styles.charInfo}>
                                        <h3>{char.name}</h3>
                                        <p>{char.race} {char.class} • Lvl {char.level}</p>
                                    </div>
                                </div>
                            ))}
                        </div>

                        <div className={styles.actions}>
                            <Button 
                                variant="outline" 
                                onClick={() => navigate('/create-character')}
                            >
                                <Plus size={16} />
                                New Character
                            </Button>
                            
                            <Button 
                                size="lg" 
                                className={styles.startBtn}
                                onClick={handleStart}
                                disabled={!selectedChar}
                            >
                                <Play size={20} />
                                Enter Dungeon
                            </Button>
                        </div>
                    </>
                )}
            </div>
        </div>
    );
};

export default NewGame;
