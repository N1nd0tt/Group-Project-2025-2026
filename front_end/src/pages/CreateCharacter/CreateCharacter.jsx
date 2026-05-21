import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { UserPlus, ArrowLeft } from 'lucide-react';
import Button from '../../components/Button';
import Input from '../../components/Input';
import { useCharacters } from '../../hooks/useCharacters';
import styles from './CreateCharacter.module.css';

const CreateCharacter = () => {
    const navigate = useNavigate();
    const { addCharacter } = useCharacters();

    const [name, setName] = useState('');
    const [race, setRace] = useState('Human');
    const [charClass, setCharClass] = useState('Fighter');
    const [weapon, setWeapon] = useState('');
    const [features, setFeatures] = useState('');
    const [unusualFact, setUnusualFact] = useState('');

    const races = ['Human', 'Elf', 'Dwarf', 'Orc', 'Halfling', 'Dragonborn'];
    const classes = ['Fighter', 'Wizard', 'Rogue', 'Cleric', 'Paladin', 'Barbarian', 'Ranger', 'Bard'];

    const handleSubmit = (e) => {
        e.preventDefault();
        
        if (!name.trim()) return;

        addCharacter({
            name,
            race,
            class: charClass,
            weapon,
            features,
            unusualFact
        });

        // Go back to the previous screen (Dashboard or New Game)
        navigate(-1);
    };

    return (
        <div className={styles.container}>
            <div className={styles.content}>
                <Button 
                    variant="ghost" 
                    className={styles.backBtn}
                    onClick={() => navigate(-1)}
                >
                    <ArrowLeft size={20} />
                    Back
                </Button>

                <div className={styles.iconWrapper}>
                    <UserPlus size={48} className={styles.icon} />
                </div>

                <h1 className={styles.title}>Create Character</h1>
                <p className={styles.subtitle}>Define your new hero</p>

                <form onSubmit={handleSubmit} className={styles.form}>
                    <Input
                        label="Character Name"
                        placeholder="e.g. Gandalf"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                    />

                    <div className={styles.selectGroup}>
                        <label className={styles.label}>Race</label>
                        <select 
                            className={styles.select}
                            value={race}
                            onChange={(e) => setRace(e.target.value)}
                        >
                            {races.map(r => (
                                <option key={r} value={r}>{r}</option>
                            ))}
                        </select>
                    </div>

                    <div className={styles.selectGroup}>
                        <label className={styles.label}>Class</label>
                        <select 
                            className={styles.select}
                            value={charClass}
                            onChange={(e) => setCharClass(e.target.value)}
                        >
                            {classes.map(c => (
                                <option key={c} value={c}>{c}</option>
                            ))}
                        </select>
                    </div>

                    <Input
                        label="Weapon"
                        placeholder="e.g. Rusty Longsword"
                        value={weapon}
                        onChange={(e) => setWeapon(e.target.value)}
                    />

                    <Input
                        label="Distinctive Features"
                        placeholder="e.g. Scar on the left eye"
                        value={features}
                        onChange={(e) => setFeatures(e.target.value)}
                    />

                    <div className={styles.selectGroup}>
                        <label className={styles.label}>Unusual Fact</label>
                        <textarea 
                            className={styles.textarea}
                            placeholder="Tell something unusual about your hero..."
                            value={unusualFact}
                            onChange={(e) => setUnusualFact(e.target.value)}
                            rows={3}
                        />
                    </div>

                    <Button type="submit" size="lg" className={styles.submitBtn}>
                        Create Hero
                    </Button>
                </form>
            </div>
        </div>
    );
};

export default CreateCharacter;
