package com.example.projekt_zesp.service.impl;

import com.example.projekt_zesp.models.Game;
import com.example.projekt_zesp.models.User;
import com.example.projekt_zesp.repository.GameRepository;
import com.example.projekt_zesp.service.GameService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class GameServiceImpl implements GameService {
    @Autowired
    private GameRepository gameRepository;

    @Override
    public Game createGame(Game game) {
        return gameRepository.save(game);
    }

    @Override
    public Game addPlayerToGame(String gameId, User player) {
        Optional<Game> optionalGame = gameRepository.findById(gameId);
        if (optionalGame.isPresent()) {
            Game game = optionalGame.get();
            game.getPlayers().add(player);
            return gameRepository.save(game);
        }
        throw new RuntimeException("Game not found");
    }

    @Override
    public Game removePlayerFromGame(String gameId, String playerId) {
        Optional<Game> optionalGame = gameRepository.findById(gameId);
        if (optionalGame.isPresent()) {
            Game game = optionalGame.get();
            game.getPlayers().removeIf(player -> player.getId().equals(playerId));
            return gameRepository.save(game);
        }
        throw new RuntimeException("Game not found");
    }

    @Override
    public void removeGame(String gameId) {
        if (gameRepository.existsById(gameId)) {
            gameRepository.deleteById(gameId);
        } else {
            throw new RuntimeException("Game not found");
        }
    }

    @Override
    public Game getGameInfo(String gameId) {
        return gameRepository.findById(gameId)
                .orElseThrow(() -> new RuntimeException("Game not found"));
    }

    @Override
    public List<Game> getAllGamesByOwner(String owner) {
        return gameRepository.findAll().stream()
                .filter(game -> game.getOwner().equals(owner))
                .toList();
    }
}
