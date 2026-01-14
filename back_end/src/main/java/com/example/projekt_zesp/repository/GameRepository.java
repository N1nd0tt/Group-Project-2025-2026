package com.example.projekt_zesp.repository;

import com.example.projekt_zesp.models.Game;
import org.springframework.data.jpa.repository.JpaRepository;

public interface GameRepository extends JpaRepository<Game, String> {

}
