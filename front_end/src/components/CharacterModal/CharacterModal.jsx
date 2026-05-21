import React, { useEffect } from 'react';
import { X, Shield, Heart, Sword } from 'lucide-react';
import Button from '../Button';
import styles from './CharacterModal.module.css';

const CharacterModal = ({ character, onClose }) => {
    // Close on escape key
    useEffect(() => {
        const handleEsc = (e) => {
            if (e.key === 'Escape') onClose();
        };
        window.addEventListener('keydown', handleEsc);
        return () => window.removeEventListener('keydown', handleEsc);
    }, [onClose]);

    if (!character) return null;

    // Helper to render stat
    const StatBox = ({ label, value }) => (
        <div className={styles.statBox}>
            <span className={styles.statLabel}>{label}</span>
            <span className={styles.statValue}>{value}</span>
        </div>
    );

    return (
        <div className={styles.overlay} onClick={onClose}>
            <div className={styles.modal} onClick={e => e.stopPropagation()}>
                <button className={styles.closeBtn} onClick={onClose}>
                    <X size={24} />
                </button>

                <div className={styles.header}>
                    <div className={styles.avatar}>
                        <Shield size={32} />
                    </div>
                    <div>
                        <h2 className={styles.name}>{character.name}</h2>
                        <p className={styles.subtitle}>
                            {character.race} {character.class} • Lvl {character.level}
                        </p>
                    </div>
                </div>

                <div className={styles.combatStats}>
                    <div className={styles.combatStat}>
                        <Heart size={20} className={styles.iconRed} />
                        <div>
                            <span className={styles.cLabel}>HP</span>
                            <span className={styles.cValue}>{character.hp || 10}</span>
                        </div>
                    </div>
                    <div className={styles.combatStat}>
                        <Shield size={20} className={styles.iconBlue} />
                        <div>
                            <span className={styles.cLabel}>AC</span>
                            <span className={styles.cValue}>{character.ac || 10}</span>
                        </div>
                    </div>
                </div>

                <div className={styles.section}>
                    <h3 className={styles.sectionTitle}>Attributes</h3>
                    <div className={styles.attributesGrid}>
                        {character.stats && (
                            <>
                                <StatBox label="Strength" value={character.stats.str} />
                                <StatBox label="Dexterity" value={character.stats.dex} />
                                <StatBox label="Constitution" value={character.stats.con} />
                                <StatBox label="Intelligence" value={character.stats.int} />
                                <StatBox label="Wisdom" value={character.stats.wis} />
                                <StatBox label="Charisma" value={character.stats.cha} />
                            </>
                        )}
                    </div>
                </div>

                <div className={styles.section}>
                    <h3 className={styles.sectionTitle}>Details</h3>
                    <ul className={styles.detailsList}>
                        <li>
                            <Sword size={16} className={styles.dIcon} />
                            <strong>Weapon:</strong> {character.weapon || "Unarmed"}
                        </li>
                        <li>
                            <strong>Features:</strong> {character.features || "None"}
                        </li>
                        {character.unusualFact && (
                            <li className={styles.fact}>
                                <strong>Unusual Fact:</strong> "{character.unusualFact}"
                            </li>
                        )}
                    </ul>
                </div>

            </div>
        </div>
    );
};

export default CharacterModal;
