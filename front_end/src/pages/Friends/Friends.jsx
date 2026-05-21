import React from 'react';
import { Search, UserPlus, MessageCircle, MoreVertical } from 'lucide-react';
import Button from '../../components/Button';
import Input from '../../components/Input';
import styles from './Friends.module.css';

const Friends = () => {
    const friends = [
        { id: 1, name: "Legolas Greenleaf", status: "online", activity: "In Character Creation" },
        { id: 2, name: "Gimli Gloinsson", status: "offline", activity: "Last seen 2h ago" },
        { id: 3, name: "Aragorn II Elessar", status: "busy", activity: "In Game: War of Ring" },
        { id: 4, name: "Frodo Baggins", status: "online", activity: "Looking for group" },
        { id: 5, name: "Samwise Gamgee", status: "offline", activity: "Last seen 5m ago" },
    ];

    return (
        <div className={styles.container}>
            <div className={styles.header}>
                <div>
                    <h1>Companions</h1>
                    <p>Your party members and allies</p>
                </div>
                <Button>
                    <UserPlus size={18} style={{ marginRight: '8px' }} />
                    Add Friend
                </Button>
            </div>

            <div className={styles.searchBar}>
                <Input placeholder="Search friends..." className={styles.searchInput} />
            </div>

            <div className={styles.grid}>
                {friends.map(friend => (
                    <div key={friend.id} className={styles.card}>
                        <div className={styles.cardHeader}>
                            <div className={`${styles.avatarAction} ${styles[friend.status]}`}>
                                {friend.name.charAt(0)}
                            </div>
                            <Button variant="ghost" size="sm" className={styles.moreBtn}>
                                <MoreVertical size={16} />
                            </Button>
                        </div>

                        <div className={styles.cardBody}>
                            <h3>{friend.name}</h3>
                            <p className={styles.activity}>{friend.activity}</p>
                        </div>

                        <div className={styles.cardFooter}>
                            <Button variant="outline" size="sm" className={styles.actionBtn}>
                                <MessageCircle size={16} />
                                Message
                            </Button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Friends;
