package com.example.projekt_zesp.models;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;


@Entity
@Table(name = "games")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Game {
    @Id
    @Column(nullable = false, unique = true)
    private String id;
    @Column(nullable = false, unique = true)
    private String owner;
    @OneToMany(cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    @JoinColumn(name = "game_id")
    private List<User> players;
}
