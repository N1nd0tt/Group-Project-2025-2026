import React, { useState, useEffect, useRef } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { LogOut, Send, Sword, User } from 'lucide-react';
import styles from './GameChat.module.css';

const GameChat = () => {
    const location = useLocation();
    const navigate = useNavigate();
    const character = location.state?.character;
    
    const [messages, setMessages] = useState([
        {
            id: 1,
            sender: 'dm',
            text: `Welcome, ${character?.name || 'Traveler'}. The air in the dungeon is damp and smells of ancient decay. Your torch flickers, casting long shadows against the stone walls. Ahead of you lies a heavy wooden door bound in iron. What do you do?`
        }
    ]);
    const [inputValue, setInputValue] = useState('');
    const messagesEndRef = useRef(null);

    // If no character was passed in state, redirect back
    useEffect(() => {
        if (!character) {
            navigate('/new-game');
        }
    }, [character, navigate]);

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    const handleSend = (e) => {
        e.preventDefault();
        if (!inputValue.trim()) return;

        const newUserMessage = {
            id: Date.now(),
            sender: 'player',
            text: inputValue.trim()
        };

        setMessages(prev => [...prev, newUserMessage]);
        setInputValue('');

        // Mock DM response
        setTimeout(() => {
            setMessages(prev => [
                ...prev,
                {
                    id: Date.now() + 1,
                    sender: 'dm',
                    text: 'The DM ponders your action... (AI integration coming soon)'
                }
            ]);
        }, 1000);
    };

    const handleExit = () => {
        if (window.confirm("Are you sure you want to leave the dungeon? Your progress will be saved.")) {
            navigate('/dashboard');
        }
    };

    if (!character) return null;

    return (
        <div className={styles.chatContainer}>
            <header className={styles.header}>
                <div className={styles.headerInfo}>
                    <div className={styles.dmIcon}>
                        <Sword size={24} />
                    </div>
                    <div className={styles.headerTitle}>
                        <h2>Dungeon Master</h2>
                        <p>Playing as {character.name} the {character.race} {character.class}</p>
                    </div>
                </div>
                <button className={styles.exitButton} onClick={handleExit}>
                    <LogOut size={16} />
                    Exit Game
                </button>
            </header>

            <div className={styles.messagesArea}>
                {messages.map(msg => (
                    <div key={msg.id} className={`${styles.messageWrapper} ${styles[msg.sender]}`}>
                        <div className={`${styles.avatar} ${msg.sender === 'dm' ? styles.dmAvatar : styles.playerAvatar}`}>
                            {msg.sender === 'dm' ? <Sword size={20} /> : <User size={20} />}
                        </div>
                        <div className={styles.messageContent}>
                            <span className={styles.messageName}>
                                {msg.sender === 'dm' ? 'Dungeon Master' : character.name}
                            </span>
                            <div className={styles.bubble}>
                                {msg.text}
                            </div>
                        </div>
                    </div>
                ))}
                <div ref={messagesEndRef} />
            </div>

            <div className={styles.inputArea}>
                <form className={styles.inputContainer} onSubmit={handleSend}>
                    <input
                        type="text"
                        className={styles.chatInput}
                        placeholder="Describe your action..."
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                        autoFocus
                    />
                    <button 
                        type="submit" 
                        className={styles.sendButton}
                        disabled={!inputValue.trim()}
                    >
                        <Send size={20} />
                    </button>
                </form>
            </div>
        </div>
    );
};

export default GameChat;
