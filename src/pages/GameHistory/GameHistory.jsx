import React from 'react';
import { Calendar, Clock, Map, Trophy } from 'lucide-react';
import Button from '../../components/Button';
import styles from './GameHistory.module.css';

const GameHistory = () => {
    const games = [
        {
            id: 1,
            title: "The Curse of Strahd",
            date: "Oct 15, 2025",
            duration: "4h 30m",
            location: "Castle Ravenloft",
            status: "Completed",
            outcome: "Victory",
            image: "linear-gradient(to right, #434343, #000000)"
        },
        {
            id: 2,
            title: "Lost Mines of Phandelver",
            date: "Sep 28, 2025",
            duration: "3h 15m",
            location: "Phandalin",
            status: "Aborted",
            outcome: "TPK",
            image: "linear-gradient(to right, #2c3e50, #fd746c)"
        },
        {
            id: 3,
            title: "Storm King's Thunder",
            date: "Aug 10, 2025",
            duration: "5h 00m",
            location: "Northern Coast",
            status: "Completed",
            outcome: "Victory",
            image: "linear-gradient(to right, #000046, #1cb5e0)"
        }
    ];

    return (
        <div className={styles.container}>
            <div className={styles.header}>
                <h1>Adventure Log</h1>
                <p>Chronicles of your past journey</p>
            </div>

            <div className={styles.list}>
                {games.map(game => (
                    <div key={game.id} className={styles.card}>
                        <div className={styles.cardContent}>
                            <div className={styles.cardHeader}>
                                <h2 className={styles.gameTitle}>{game.title}</h2>
                                <span className={`${styles.status} ${styles[game.status.toLowerCase()]}`}>
                                    {game.status}
                                </span>
                            </div>

                            <div className={styles.detailsGrid}>
                                <div className={styles.detailItem}>
                                    <Calendar size={16} className={styles.icon} />
                                    <span>{game.date}</span>
                                </div>
                                <div className={styles.detailItem}>
                                    <Clock size={16} className={styles.icon} />
                                    <span>{game.duration}</span>
                                </div>
                                <div className={styles.detailItem}>
                                    <Map size={16} className={styles.icon} />
                                    <span>{game.location}</span>
                                </div>
                                <div className={styles.detailItem}>
                                    <Trophy size={16} className={styles.icon} />
                                    <span className={styles.outcome}>{game.outcome}</span>
                                </div>
                            </div>
                        </div>

                        <div className={styles.cardActions}>
                            <Button variant="outline" size="sm">View Details</Button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default GameHistory;
