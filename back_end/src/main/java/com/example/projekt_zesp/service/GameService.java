package com.example.projekt_zesp.service;

import com.example.projekt_zesp.models.Game;
import com.example.projekt_zesp.models.User;

import java.util.List;

public interface GameService {
    Game createGame(Game game);
    Game addPlayerToGame(String gameId, User player);
    Game removePlayerFromGame(String gameId, String playerId);
    void removeGame(String gameId);
    Game getGameInfo(String gameId);
    List<Game> getAllGamesByOwner(String owner);
}
