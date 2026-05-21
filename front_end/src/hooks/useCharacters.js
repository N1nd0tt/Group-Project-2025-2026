import { useState, useEffect } from 'react';

const generateStat = (min = 8, max = 16) => Math.floor(Math.random() * (max - min + 1)) + min;

// Default mock characters
const defaultCharacters = [
    { 
        id: 1, 
        name: "Thorne Ironbreaker", 
        class: "Paladin", 
        level: 5, 
        race: "Dwarf",
        hp: 45,
        ac: 18,
        stats: { str: 16, dex: 10, con: 14, int: 8, wis: 12, cha: 15 },
        weapon: "Warhammer",
        features: "Thick braided beard with iron rings",
        unusualFact: "Refuses to drink ale out of anything but a stone mug."
    },
    { 
        id: 2, 
        name: "Elara Moonwhisper", 
        class: "Rogue", 
        level: 3, 
        race: "Elf",
        hp: 24,
        ac: 15,
        stats: { str: 8, dex: 18, con: 12, int: 14, wis: 10, cha: 14 },
        weapon: "Twin Daggers",
        features: "Silver eyes that glow faintly in the dark",
        unusualFact: "Can perfectly mimic the sound of any bird."
    },
    { 
        id: 3, 
        name: "Grimzag", 
        class: "Barbarian", 
        level: 7, 
        race: "Orc",
        hp: 75,
        ac: 14,
        stats: { str: 20, dex: 14, con: 16, int: 8, wis: 10, cha: 9 },
        weapon: "Greataxe",
        features: "Covered in tribal tattoos",
        unusualFact: "Collects shiny rocks and talks to them."
    }
];

export const useCharacters = () => {
    const [characters, setCharacters] = useState(() => {
        const saved = localStorage.getItem('dnd_characters');
        if (saved) {
            return JSON.parse(saved);
        }
        localStorage.setItem('dnd_characters', JSON.stringify(defaultCharacters));
        return defaultCharacters;
    });

    useEffect(() => {
        localStorage.setItem('dnd_characters', JSON.stringify(characters));
    }, [characters]);

    const addCharacter = (newCharacter) => {
        const charWithId = {
            ...newCharacter,
            id: Date.now(),
            level: 1,
            hp: generateStat(8, 14), // Basic level 1 HP
            ac: generateStat(11, 16), // Basic AC
            stats: {
                str: generateStat(),
                dex: generateStat(),
                con: generateStat(),
                int: generateStat(),
                wis: generateStat(),
                cha: generateStat()
            }
        };
        setCharacters(prev => [...prev, charWithId]);
    };

    return {
        characters,
        addCharacter
    };
};
