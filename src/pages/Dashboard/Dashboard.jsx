import React from 'react';
import { User, Shield, Swords, Plus, Settings } from 'lucide-react';
import Button from '../../components/Button';
import styles from './Dashboard.module.css';

const Dashboard = () => {
    // Mock data
    const user = {
        name: "Dungeon Master",
        title: "Level 12 Game Master",
        bio: "Exploring dungeons and slaying dragons since 2015. Always looking for a new adventure.",
        stats: {
            games: 42,
            characters: 8,
            hours: 1250
        }
    };

    const characters = [
        { id: 1, name: "Thorne Ironbreaker", class: "Paladin", level: 5, race: "Dwarf" },
        { id: 2, name: "Elara Moonwhisper", class: "Rogue", level: 3, race: "Elf" },
        { id: 3, name: "Grimzag", class: "Barbarian", level: 7, race: "Orc" }
    ];

    return (
        <div className={styles.container}>
            {/* Profile Header */}
            <div className={styles.profileHeader}>
                <div className={styles.profileCover}></div>
                <div className={styles.profileContent}>
                    <div className={styles.avatarWrapper}>
                        <div className={styles.avatar}>DM</div>
                    </div>
                    <div className={styles.profileInfo}>
                        <div className={styles.nameRow}>
                            <h1 className={styles.name}>{user.name}</h1>
                            <Button variant="outline" size="sm" className={styles.editBtn}>
                                <Settings size={16} />
                                Edit Profile
                            </Button>
                        </div>
                        <p className={styles.title}>{user.title}</p>
                        <p className={styles.bio}>{user.bio}</p>

                        <div className={styles.statsRow}>
                            <div className={styles.stat}>
                                <span className={styles.statValue}>{user.stats.games}</span>
                                <span className={styles.statLabel}>Games</span>
                            </div>
                            <div className={styles.stat}>
                                <span className={styles.statValue}>{user.stats.characters}</span>
                                <span className={styles.statLabel}>Characters</span>
                            </div>
                            <div className={styles.stat}>
                                <span className={styles.statValue}>{user.stats.hours}</span>
                                <span className={styles.statLabel}>Hours Played</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Main Grid */}
            <div className={styles.grid}>
                {/* Characters Section */}
                <div className={styles.section}>
                    <div className={styles.sectionHeader}>
                        <h2>My Characters</h2>
                        <Button size="sm">
                            <Plus size={16} />
                            New Character
                        </Button>
                    </div>
                    <div className={styles.cardGrid}>
                        {characters.map(char => (
                            <div key={char.id} className={styles.characterCard}>
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
                </div>

                {/* Quick Actions / Recent */}
                <div className={styles.section}>
                    <div className={styles.sectionHeader}>
                        <h2>Recent Activity</h2>
                    </div>
                    <div className={styles.activityList}>
                        <div className={styles.activityItem}>
                            <Swords size={20} className={styles.actIcon} />
                            <div>
                                <p className={styles.actText}>Completed <strong>The Lost Mines</strong></p>
                                <span className={styles.actTime}>2 days ago</span>
                            </div>
                        </div>
                        <div className={styles.activityItem}>
                            <User size={20} className={styles.actIcon} />
                            <div>
                                <p className={styles.actText}>Created character <strong>Elara</strong></p>
                                <span className={styles.actTime}>1 week ago</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
